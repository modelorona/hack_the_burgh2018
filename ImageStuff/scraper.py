from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome("./chromedriver_mac")

def returnImageUrls(LINK):

    tries = 0
    driver.get(LINK+"photos/")
    images = None
    while(True):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        soup = BeautifulSoup(driver.page_source)
        time.sleep(5)
        images = [img['src'] for img in soup.find('div',{'class':'_2eec'}).find_all('img')]
        if(len(images)>50 and tries < 20):
            break
        time.sleep(2)
        tries +=1

    return images

    def returnUrlData(LINK):

        tries = 0
        driver.get(LINK + "photos/")
        images = None
        while (True):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            soup = BeautifulSoup(driver.page_source)
            time.sleep(5)
            images = [img['src'] for img in soup.find('div', {'class': '_2eec'}).find_all('img')]
            if (len(images) > 50 and tries < 20):
                break
            time.sleep(2)
            tries += 1

        return images

        driver.get(LINK)
        posts = None

        POSTS = []

        while(True):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            soup = BeautifulSoup(driver.page_source,"lxml")
            posts = soup.find_all('div',{'class':'_q7o'})
            if(len(posts)>30 and tries < 20):
                for post in posts:
                    time_stamp = post.find("span",{"class":"timestampContent"})
                    content = post.find("div",{"class":"userContent"})
                    POSTS.append({"time_stamp":time_stamp.text,"content":content.text})
                break

        return POSTS