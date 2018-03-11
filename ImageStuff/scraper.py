from selenium import webdriver
from bs4 import BeautifulSoup
import time



def returnImageUrls(LINK):
    driver = webdriver.Chrome("./chromedriver_mac")
    tries = 0
    driver.get(LINK+"photos/")
    images = None
    time.sleep(1)
    while(True):
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.3)
        soup = BeautifulSoup(driver.page_source)
        images = [img['src'] for img in soup.find('div',{'class':'_2eec'}).find_all('img')]
        if(len(images)>50 and tries < 20):
            break
        tries +=1
    driver.close()
    return images

def returnUrlData(LINK):
    driver = webdriver.Chrome("./chromedriver_mac")
    tries = 0
    driver.get(LINK + "photos/")
    images = None
    time.sleep(1)
    while (True):
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.3)
        soup = BeautifulSoup(driver.page_source)
        images = [img['src'] for img in soup.find('div', {'class': '_2eec'}).find_all('img')]
        if (len(images) > 50 and tries < 20):
            break
        tries += 1

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
    driver.close()
    return POSTS