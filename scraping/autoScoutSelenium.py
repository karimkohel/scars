"""
This script is written specifically for autoscout24 car website which entails the coming points:
- the page number is always maxed out at 20 pages
- each article has to be fetched again once a navigation event has occurred to avoid a stale element
- the registration year and page number should be placed in the link in only the specified format
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time
from helpers import ScrapingHandler


# start up driver with options
options = Options()
options.page_load_strategy = "normal"
driver = webdriver.Firefox(options=options)

# TODO: add your data location here
handler = ScrapingHandler("data/LandRover_RangeRover_Vogue/raw")

# this is the starting registration year to scrap from, then it will loop until the last possible year (2023)
startingRegistration = 16 # starting year if for any reason the scrapping stopped, here you can start again from whatever year you like
for registrationYear in range(startingRegistration, 24): 
    starting_page = 1 # starting page if for any reason the scrapping stopped, here you can start again from whatever page you like
    for page_num in range(starting_page, 21):
        # TODO: add your link here
        driver.get(f"https://www.autoscout24.com/lst/land-rover/range-rover/re_20{registrationYear}?atype=C&cy=D%2CA%2CB%2CE%2CF%2CI%2CL%2CNL&damaged_listing=exclude&desc=0&page={page_num}&powertype=kw&search_id=1g082rrirkt&sort=standard&source=listpage_pagination&ustate=N%2CU")
        print(f"starting page: {page_num}, on year: {registrationYear}")

        if page_num == starting_page and registrationYear == startingRegistration:
            try:
                driver.find_element(By.CLASS_NAME, "_consent-accept_1i5cd_111").click()
            except Exception as e:
                print(e)

        time.sleep(1)
        articles = driver.find_elements(By.TAG_NAME, 'article')

        # for each article, find it's link, enter it's page and reverse engineer the image links to download
        for article_num in range(len(articles)-1):
            try:
                article = driver.find_elements(By.TAG_NAME, 'article')[article_num]
                article.click()
                articleGallery = driver.find_element(By.CLASS_NAME, "image-gallery-thumbnails-container")
                galleryItems = articleGallery.find_elements(By.CLASS_NAME, "image-gallery-thumbnail-image")
            except Exception as e:
                print(e)
                continue

            for item in galleryItems:
                imgSrc = item.get_attribute('src')
                imgSrc = imgSrc.replace("/120x90.jpg", "")
                if '.jpg' in imgSrc:
                    handler.download_image(imgSrc, imgSrc.split("/")[-1].replace(".jpg", ""))
                    print(imgSrc)
                else:
                    print("wrong img type, not downloading")
            driver.back()