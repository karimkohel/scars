from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
from helpers import Handler

"""
This script is written specifically for autoscout24 car website which entails the coming points:
- the page number is always maxed out at 20 pages
- each article has to be fetched again once a navigation event has occurred to avoid a stale element 

"""

# start up driver with options
options = Options()
options.page_load_strategy = "normal"
driver = webdriver.Firefox(options=options)
handler = Handler("data/LandRover_defender/raw")

# loop over all pages in the results
starting_page = 1
for page_num in range(starting_page, 21):
    driver.get(f"https://www.autoscout24.com/lst/land-rover/defender?atype=C&desc=0&fregfrom=2023&page={page_num}&search_id=8c0kqi4iws&sort=standard&source=listpage_pagination&ustate=N%2CU")
    print(f"starting page: {page_num}")

    if page_num == starting_page:
        driver.find_element(By.CLASS_NAME, "_consent-accept_1i5cd_111").click()

    time.sleep(1)
    articles = driver.find_elements(By.TAG_NAME, 'article')

    # for each article, find it's link, enter it's page and reverse engineer the image links to download
    for article_num in range(len(articles)-1):
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
            if '.jpg' in imgSrc:
                handler.download_image(imgSrc, imgSrc.split("/")[-1].replace(".jpg", ""))
                print(imgSrc)
            else:
                print("wrong img type, not downloading")
        driver.back()



    # 17->21
    # 21 -> 22
    # 23