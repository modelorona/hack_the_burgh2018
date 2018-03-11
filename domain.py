from selenium import webdriver
from bs4 import BeautifulSoup
import time
URL = "https://www.prepostseo.com/bulk-domain-age-checker"


def check_age(urls):
    driver = webdriver.Chrome("./chromedriver")
    for url in urls:
        driver.get(URL)        
        try:
            driver.find_element_by_id("urls").send_keys(url)
            driver.find_element_by_xpath('//*[@id="checkBtn"]').click()
            soup = BeautifulSoup(driver.page_source)   
            age = soup.find("td",{"id":"age_0"}).text                                                  
            while("loading" in age.strip().lower()):
                soup = BeautifulSoup(driver.page_source)                   
                age = soup.find("td",{"id":"age_0"}).text
            age = soup.find("td",{"id":"age_0"}).text
            update = soup.find("td",{"id":"update_0"}).text
            print(age,update)
        except:
            print("INVALID URL")

from db import bad_sites
check_age(bad_sites)