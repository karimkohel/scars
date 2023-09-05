from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
from helpers import Handler

# start up driver with options
options = Options()
options.page_load_strategy = "normal"
driver = webdriver.Firefox(options=options)
handler = Handler("LandRover_RangeRover_velar")

# loop over all pages in the results
for page_num in range(8, 21):
    driver.get(f"https://www.autoscout24.com/lst/land-rover/range-rover-velar?atype=C&desc=0&page={page_num}&search_id=glqh8818ex&sort=standard&source=listpage_pagination&ustate=N%2CU")
    if page_num == 8:
        driver.find_element(By.CLASS_NAME, "_consent-accept_1i5cd_111").click()
    # loop inside each page and get the car pages urls
    time.sleep(1)
    articles = driver.find_elements(By.TAG_NAME, 'article')
    # get inside each page and maximize the img then download that image and move to the next image until it's done
    for article_num in range(len(articles)):
        try:
            article = driver.find_elements(By.TAG_NAME, 'article')[article_num]
            article.click()
            articleGallery = driver.find_element(By.CLASS_NAME, "image-gallery-thumbnails-container")
            galleryItems = articleGallery.find_elements(By.CLASS_NAME, "image-gallery-thumbnail-image")
        except NoSuchElementException as e:
            print(e)
            break

        for item in galleryItems:
            imgSrc = item.get_attribute('src')
            imgSrc = imgSrc.replace("/120x90.jpg", "")
            print(imgSrc)
            if '.jpg' in imgSrc:
                handler.download_image(imgSrc, imgSrc.split("/")[-1].replace(".jpg", ""))
                handler.log("downloaded img")
            else:
                print("wrong img type, not downloading")
        driver.back()

    # # press next until the pages end
    # bottomNav = driver.find_element(By.CLASS_NAME, "ListPage_pagination__v_4ci")
    # bottomNavButtonsList = bottomNav.find_elements(By.TAG_NAME, 'li')
    # nextPageButton = bottomNavButtonsList[-1]
    # try:
    #     nextPageButton.click()
    # except ElementClickInterceptedException:
    #     print("done")
    #     break
