from flask import Flask
from flask import request
import subprocess
from flask import render_template
from flask import jsonify
import requests
import math
from bs4 import BeautifulSoup


app = Flask(__name__, template_folder='templates')

import argparse
import io

from google.cloud import vision
from google.cloud.vision import types
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=os.path.join(os.path.dirname(__file__), 'hack-the-burgh-848119bd429e.json')
import requests

def annotate(path):
    """Returns web annotations given the path to an image."""
    client = vision.ImageAnnotatorClient()

    content = requests.get(path, allow_redirects=True).content
    image = types.Image(content=content)

    web_detection = client.web_detection(image=image).web_detection

    return web_detection


def report(annotations):
    """Prints detected features in the provided web annotations."""
    if annotations.pages_with_matching_images:
        print('\n{} Pages with matching images retrieved'.format(
            len(annotations.pages_with_matching_images)))

        for page in annotations.pages_with_matching_images:
            print('Url   : {}'.format(page.url))

    if annotations.full_matching_images:
        print ('\n{} Full Matches found: '.format(
               len(annotations.full_matching_images)))

        for image in annotations.full_matching_images:
            print('Url  : {}'.format(image.url))

    if annotations.partial_matching_images:
        print ('\n{} Partial Matches found: '.format(
               len(annotations.partial_matching_images)))

        for image in annotations.partial_matching_images:
            print('Url  : {}'.format(image.url))

    if annotations.web_entities:
        print ('\n{} Web entities found: '.format(
            len(annotations.web_entities)))

        for entity in annotations.web_entities:
            print('Score      : {}'.format(entity.score))
            print('Description: {}'.format(entity.description))


def urlInformation (url):
    return annotate(url)


import GettingData as G
import scraper as s
from datetime import datetime

most_common_spam_words = ["4u", "accept", "credit", "cards", "act", "now!", "don’t", "hesitate!", "additional", "income", "addresses", "on", "cd", "all", "natural", "amazing", "apply", "online", "as", "seen", "on", "auto", "email", "removal", "avoid", "bankruptcy", "be", "amazed", "be", "your", "own", "boss", "being", "a", "member", "big", "bucks", "bill", "1618", "billing", "address", "billion", "dollars", "brand", "new", "pager", "bulk", "email", "buy", "direct", "buying", "judgments", "cable", "converter", "call", "free", "call", "now", "calling", "creditors", "can’t", "live", "without", "cancel", "at", "any", "time", "cannot", "be", "combined", "with", "any", "other", "offer", "cash", "bonus", "cashcashcash", "casino", "cell",", ""phone", "cancer", "scam", "cents", "on", "the", "dollar", "check", "or", "money", "order", "claims", "not", "to", "be", "selling", "anything", "claims", "to", "be", "in", "accordance", "with", "some", "spam", "law", "claims", "to", "be", "legal", "join", "millions", "of", "americans", "laser", "printer", "limited", "time", "only", "long", "distance", "phone", "offer", "lose", "weight", "spam", "lower", "interest", "rates", "lower", "monthly", "payment", "lowest", "price", "luxury", "car", "mail", "in", "order", "form", "marketing", "solutions", "mass", "email", "meet", "singles", "member", "stuff", "message", "contains", "disclaimer", "mlm", "money", "back", "money", "making", "month", "trial", "offer", "more", "internet", "traffic", "mortgage", "rates", "multi", "level", "marketing", "name", "brand", "new", "customers", "only", "new", "domain", "extensions", "nigerian", "no", "age", "restrictions", "no", "catch", "no", "claim", "forms", "no", "cost", "no", "credit", "check", "no", "disappointment", "no", "experience", "no", "fees", "no", "gimmick", "no", "inventory", "no", "investment", "no", "medical", "exams", "no", "middleman", "no", "obligation", "no", "purchase", "necessary", "unsecured", "credit/debt", "urgent", "us", "dollars", "vacation", "offers", "viagra", "and", "other", "drugs", "wants", "credit", "card", "we", "hate", "spam", "claims", "you", "are", "a", "winner", "claims", "you", "registered", "with", "some", "kind", "of", "partner", "click", "below", "click", "here", "link", "click", "to", "remove", "click", "to", "remove", "mailto", "compare", "rates", "compete", "for", "your", "business", "confidentially", "on", "all", "orders", "congratulations", "consolidate", "debt", "and", "credit", "copy", "accurately", "copy", "dvds", "credit", "bureaus", "credit", "card", "offers", "cures", "baldness", "dear", "email", "dear", "friend", "dear", "somebody", "different", "reply", "to", "dig", "up", "dirt", "on", "friends", "direct", "email", "direct", "marketing", "discusses", "search", "engine", "listings", "do", "it", "today", "don’t", "delete", "drastically", "reduced", "earn", "per", "week", "easy", "terms", "eliminate", "bad", "credit", "email", "harvest", "email", "marketing", "expect", "to", "earn", "fantastic", "deal", "fast", "viagra", "delivery", "financial", "freedom", "find", "out", "anything", "for", "free", "no", "questions", "asked", "no", "selling", "no", "strings", "attached", "not", "intended", "off", "shore", "offer", "expires", "offers", "coupon", "offers", "extra", "cash", "offers", "free", "(often", "stolen)", "passwords", "once", "in", "lifetime", "one", "hundred", "percent", "free", "one", "hundred", "percent", "guaranteed", "one", "time", "mailing", "online", "biz", "opportunity", "online", "pharmacy", "only", "$", "opportunity", "opt", "in", "order", "now", "order", "status", "orders", "shipped", "by", "priority", "mail", "outstanding", "values", "pennies", "a", "day", "people", "just", "leave", "money", "laying", "around", "please", "read", "potential", "earnings", "print", "form", "signature", "print", "out", "and", "fax", "produced", "and", "sent", "out", "profits", "promise", "you", "…!", "pure", "profit", "real", "thing", "refinance", "home", "removal", "instructions", "remove", "in", "quotes", "remove", "subject", "removes", "wrinkles", "reply", "remove", "subject", "requires", "initial", "investment", "reserves", "the", "right", "we", "honor", "all", "weekend", "getaway", "what", "are", "you", "waiting", "for?", "while", "supplies", "last", "while", "you", "sleep", "who", "really", "wins?", "why", "pay", "more?", "for", "instant", "access", "for", "just", "$", "(some", "amt)", "free", "access", "free", "cell", "phone", "free", "consultation", "free", "dvd", "free", "grant", "money", "free", "hosting", "free", "installation", "free", "investment", "free", "leads", "free", "membership", "free", "money", "free", "offer", "free", "preview", "free", "priority", "mail", "free", "quote", "free", "sample", "free", "trial", "free", "website", "full", "refund", "get", "it", "now", "get", "paid", "get", "started", "now", "gift", "certificate", "great", "offer", "guarantee", "have", "you", "been", "turned", "down?", "hidden", "assets", "home", "employment", "human", "growth", "hormone", "if", "only", "it", "were", "that", "easy", "in", "accordance", "with", "laws", "increase", "sales", "increase", "traffic", "insurance", "investment", "decision", "it's", "effective", "reverses", "aging", "risk", "free", "round", "the", "world", "s", "1618", "safeguard", "notice", "satisfaction", "guaranteed", "save", "$", "save", "big", "money", "save", "up", "to", "score", "with", "babes", "section", "301", "see", "for", "yourself", "sent", "in", "compliance", "serious", "cash", "serious", "only", "shopping", "spree", "sign", "up", "free", "today", "social", "security", "number", "special", "promotion", "stainless", "steel", "stock", "alert", "stock", "disclaimer", "statement", "stock", "pick", "stop", "snoring", "strong", "buy", "stuff", "on", "sale", "subject", "to", "credit", "supplies", "are", "limited", "take", "action", "now", "talks", "about", "hidden", "charges", "talks", "about", "prizes", "tells", "you", "it’s", "an", "ad", "terms", "and", "conditions", "the", "best", "rates", "the", "following", "form", "they", "keep", "your", "money", "—", "no", "refund!", "they’re", "just", "giving", "it", "away", "this", "isn’t", "junk", "this", "isn’t", "spam", "university", "diplomas", "unlimited", "will", "not", "believe", "your", "eyes", "winner", "winning", "work", "at", "home", "you", "have", "been", "selected", "your", "trump" "income",]


def returnScoreLabels(LINK):
    scoreLabels = 0
    numer_of_iterations = 0
    try:
        for link in s.returnImageUrls(LINK)[::2]:
            dataOfImage = G.dataOnImage(str(link), 0.5, 1)
            for label in dataOfImage["labels"]:
                for word in label[0].split(' '):
                    if word.lower() in most_common_spam_words:
                        scoreLabels += label[1]
                    numer_of_iterations += 1
    except AttributeError:
        return scoreLabels

    return scoreLabels#/numer_of_iterations*100


def returnScoreText(LINK):
    number_of_iterations = 0
    dateList = []
    dateobject = datetime.strptime("11 March 2018", '%d %B %Y')
    try:
        for dicts in s.returnUrlData(LINK):
            if dicts["time_stamp"][-4:-2] == "20":
                dateList += [(dateobject - datetime.strptime(dicts["time_stamp"], '%d %B %Y')).days]
                dateobject = datetime.strptime(dicts["time_stamp"], '%d %B %Y')
            number_of_iterations += 1
    except AttributeError:
        return sum(dateList) / (number_of_iterations+1)

    return sum(dateList)/number_of_iterations



    #May want to implement checking the url address of the sites that include this image agains the database of fake news sites.

def isFake (LINK):
    returnDates = returnScoreText(LINK)
    returnLabels = returnScoreLabels(LINK)
    if returnDates > 9 or returnLabels < 5:
        return False
    else:
        return True


from selenium import webdriver
from bs4 import BeautifulSoup
import time



def returnImageUrls(LINK):
    driver = webdriver.Chrome("./chromedriver_mac")
    tries = 0
    driver.get(LINK+"photos/")
    images = None
    time.sleep(2.5)
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
    time.sleep(2.5)
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

def dataOnImage(url, min_label_score = 0.0, limit_of_urls = -1):
    """
    dict file structure:
        "labels": [(labe_name, score)]
        "urls_to_similar_sides": ["url"]
    """

    information = GoogleApi.annotate(url)
    dict = {"labels": [],
            "urls_to_similar_sides": []}

    for entity in information.web_entities:
        if entity.score >= min_label_score:
            dict["labels"] += [(entity.description, entity.score)]

    if (limit_of_urls == -1):
        for page in information.pages_with_matching_images:
            dict["urls_to_similar_sides"] += [page.url]
    else:
        for page in information.pages_with_matching_images[:min(limit_of_urls, len(information.pages_with_matching_images))]:
            dict["urls_to_similar_sides"] += [page.url]

    return dict


#report(annotate(args.image_url))
# saves the url to the database
bad_sites = ["24sevendailynews.com",
             "akoy-pilipino.blogspot.com",
             "aljazeera-tv.com",
             "allthingspinoy.com",
             "asianpolicy.press",
             "www.balitangpinas.net",
             "bbc101.co.uk",
             "bbctimes.com",
             "latestdutertenews.altervista.org",
             "classifiedtrends.net",
             "cnnalive.com",
             "da1lymail.com",
             "dai1lymail.co.uk",
             "dailyfilipino.altervista.org",
             "dailyfilipinews.blogspot.com",
             "definitelyfilipino.com",
             "balita.definitelyfilipino.com",
             "buzz.definitelyfilipino.com",
             "buzz.definitelyfilipino.net",
             "dugongmaharlika.com",
             "dutertenews.com",
             "du30news.com",
             "du30news.net",
             "www.dutertenewswatch.com",
             "du30newsblog.blogspot.com",
             "du30newsinfo.com",
             "dutertetrendingnews.blogspot.com",
             "www.dyaryo.net",
             "dutertedefender.com",
             "extremereaders.com",
             "filipinewsph.net",
             "grpshorts.blogspot.com",
             "theguard1an.com",
             "hotnewsphil.blogspot.com",
             "www.iampilipino.com",
             "www.leaknewsph.com",
             "www.maharlikanews.com",
             "mindanation.com",
             "okd2.com",
             "ilikeyouquotes.blogspot.com",
             "philnewscourier.blogspot.com",
             "www.philnewsportal.com",
             "pilipinastrendingnews.blogspot.com",
             "pinasnewsportal.blogspot.com",
             "pinoyfreedomwall.com",
             "pinoynewsblogger.blogspot.com",
             "pinoynewstv.com",
             "pinoypasikat.tk",
             "pinoyspeak.info",
             "pinoyviralissues.net",
             "pinoyworld.net",
             "phppoliticsnews.blogspot.com",
             "pinoytrending.altervista.org",
             "pinoytrendingnews.net",
             "pinoytrendingnewsph.blogspot.com",
             "pinoytrending.altervista.org",
             "pinoyviralissues.net",
             "pinoyworld.net",
             "publictrending.net",
             "publictrending.news",
             "qwazk.blogspot.com",
             "radiogtv.com",
             "sowhatsnews.wordpress.com",
             "www.socialnewsph.com",
             "tahonews.com",
             "thenewsfeeder.net",
             "thephilippinepolitics.com",
             "thet1mes.com",
             "thevolatilian.com",
             "thinkingpinoy.net",
             "thinkingpinoynews.info",
             "todayinmanila.ga",
             "trendingnewsportal.com",
             "trendingnewsportal.net",
             "trendingnewsportal.net.ph",
             "trendingnewsportal.blogspot.com",
             "blogspot.com",
             "tnp.today",
             "trendingnewsvideo.com",
             "trendingtopics.altervista.org",
             "trendingviral.tk",
             "radio.com",
             "verifiedph.blogspot.com",
             "viralportal.ml",
             "http://ww6.365usnews.com"]

def getQs(text, char):
    counter = 0
    for i in range(0, len(text)):
        if (text[i] == char):
            counter = counter + 1

    return counter

def analyser():
    req = requests.request('GET', 'https://api.fakenewsdetector.org/links/all')
    urls = ["24sevendailynews.com",
            "akoy-pilipino.blogspot.com",
            "aljazeera-tv.com",
            "allthingspinoy.com",
            "asianpolicy.press",
            "www.balitangpinas.net",
            "bbc101.co.uk",
            "bbctimes.com",
            "latestdutertenews.altervista.org",
            "classifiedtrends.net",
            "cnnalive.com",
            "da1lymail.com",
            "dai1lymail.co.uk",
            "dailyfilipino.altervista.org",
            "dailyfilipinews.blogspot.com",
            "definitelyfilipino.com",
            "balita.definitelyfilipino.com",
            "buzz.definitelyfilipino.com",
            "buzz.definitelyfilipino.net",
            "dugongmaharlika.com",
            "dutertenews.com",
            "du30news.com",
            "du30news.net",
            "www.dutertenewswatch.com",
            "du30newsblog.blogspot.com",
            "du30newsinfo.com",
            "dutertetrendingnews.blogspot.com",
            "www.dyaryo.net",
            "dutertedefender.com",
            "extremereaders.com",
            "filipinewsph.net",
            "grpshorts.blogspot.com",
            "theguard1an.com",
            "hotnewsphil.blogspot.com",
            "www.iampilipino.com",
            "www.leaknewsph.com",
            "www.maharlikanews.com",
            "mindanation.com",
         	"okd2.com",
            "ilikeyouquotes.blogspot.com",
            "philnewscourier.blogspot.com",
            "www.philnewsportal.com",
            "pilipinastrendingnews.blogspot.com",
            "pinasnewsportal.blogspot.com",
            "pinoyfreedomwall.com",
            "pinoynewsblogger.blogspot.com",
            "pinoynewstv.com",
            "pinoypasikat.tk",
            "pinoyspeak.info",
            "pinoyviralissues.net",
            "pinoyworld.net",
            "phppoliticsnews.blogspot.com",
            "pinoytrending.altervista.org",
            "pinoytrendingnews.net",
            "pinoytrendingnewsph.blogspot.com",
            "pinoytrending.altervista.org",
            "pinoyviralissues.net",
            "pinoyworld.net",
            "publictrending.net",
            "publictrending.news",
            "qwazk.blogspot.com",
            "radiogtv.com",
            "sowhatsnews.wordpress.com",
            "www.socialnewsph.com",
            "tahonews.com",
            "thenewsfeeder.net",
            "thephilippinepolitics.com",
            "thet1mes.com",
            "thevolatilian.com",
            "thinkingpinoy.net",
            "thinkingpinoynews.info",
            "todayinmanila.ga",
            "trendingnewsportal.com",
            "trendingnewsportal.net",
            "trendingnewsportal.net.ph",
            "trendingnewsportal.blogspot.com",
            "blogspot.com",
            "tnp.today",
            "trendingnewsvideo.com",
            "trendingtopics.altervista.org",
            "trendingviral.tk",
            "radio.com",
            "verifiedph.blogspot.com",
            "viralportal.ml"]
    for x in (req.json()):
        if (x["category_id"] == 2):
            url = (x["url"])
            if ("http" in url):
                urls.append(url)
    return urls

def compare(url):
    for i in analyser():
        if (url == i):
            return True
    return False

def calcDist(text):
    text1 = "Viral news circulated last week that accused a White House intern of being part of a white supremacist group because of a hand sign he was holding up in a picture of White House staffers. The hand sign I’m referring to might be one you have seen before.According to scholarly research, the historic 'OK' hand sign has been adopted by the alt-right as a sign meaning white power. Everybody has seen this before and it has absolutely nothing to do with white power groups, just another conspiracy theory. But since Democrats are convinced that flashing this 'ok' sign is proof of a secret cult that you are in, how come so many democrats are also flashing this offensive hand sign? Bill Clinton is a nazi??? who knew?? Look at him clearly brandishing his White Power hand sign for all to see, is it true that Bill Clinton has been secretly working with white power groups during his time in politics and has been attending secret white power meetings in the basement of the White House? Of course not, because this sign just means 'ok', or if you are on a basketball court, it means a 3 point shot. He’s a younger Bill Clinton flashing the sign, how long has he been apart of this secret white power society for?? Even Hillary was recruited over to the dark side? We have no hope left. No…. God, no… not Obama himself. We are all doomed.The point is that this is the silliest thing to invest controversy over because literally every politician ever who has spoke at a podium has made that sign with their hands at one point, it’s almost an unconscious thing to do. As for the White House staffer, by guess is that they asked everybody to do a thumbs up and he got confused and made the ‘ok’ sign, or he was just trying to be funny, because it kinda is."
    text2 = "Chealsea Clinton owes the American public some sort of explanation as she publicly wished a well known Satanic organization a 'Happy New Year' Tuesday night.This is going to sound like the start of a weird joke, but the parties in involved in the exchange with ended with Chealsea Clinton wishing the Church of Satan a 'Happy New Year,' were the Church of Satan, Chrissy Teigen and Hooters, try to guess the punch line.Chelsea Clinton tweeted, 'In 2017, @ChurchofSatan and I were put in a few threads together, in 2018 it’s @Hooters. What a time to be alive Chrissy! To which the Church of Satan’s official twitter responded with .The never ending excitement over here is never ending.To which Chelsea Clinton responded It’s been so long! Happy New Year! Because of the weird exchange between Chelsea and the Church of Satan, many twitter users were questioning her religious beliefs. Of course Chelsea is denying the claims that she intentionally tweeted at the Church of Satan, but it definitely raises some eyebrows.Twitter is a pretty easy app to use, Chelsea Clinton needs to stop tweeting at random, less than reputable, accounts."
    text3 = "Citizens of the great state of Oregon are up in arms on social media over a new law being passed that would allow people to pump their own gas.The law was passed through the state legislature in May and signed in June, and it will allow people in counties with less than 40,000 residents to pump their own gas, and for some reason, people are really mad about it.The law started taking effect on January 1st of this new year and in rural parts of Oregon people are very upset about the change. Full service gas stations have been around in Oregon since 1951 and people are not ready for things to change.A local CBS affiliate in Medford, Ore., asked its viewers on Facebook about the new law – the responses have ranged from anger to confusion.I don’t even know HOW to pump gas and I am 62, native Oregonian…..I say NO THANKS! I don’t want to smell like gasoline! one woman wrote in a comment on a survey the new station posted Dec. 29.It is safer for people, if a station attendant does the service. The only advantage of pumping the gas yourself, would be paying a few cents less a gallon. Getting older, and being disabled, I’d rather have the help! another person wrote, noting there are times when attendants are welcomed.Then there were those on the side of reality who understood how ridiculous it was that people were complaining about having to pump their own gas.It’s official. Oregon is full of mentally defective, full grown children, incapable of the most mundane of adult task, wrote one person whose reaction was a common one on the thread.The people of Oregon are such babies for complaining about this, for one it doesn’t even apply to some counties, and for two most people do this on a semi-daily basis in other states, it’s not a big deal."

    textR1 = "Traces of the nerve agent used against former Russian spy Sergei Skripal and his daughter, Yulia, have been found at the restaurant where they ate on Sunday afternoon, the BBC understands.The substance was found in one part of Zizzi in Salisbury during a continuing forensic examination.The pair were found two hours after finishing their meal collapsed on a park bench. Both are critically ill.No-one who was in the restaurant at the same time is thought to be in danger.There is also no suggestion that anyone dining at the time had anything to do with the nerve agent.The restaurant is currently surrounded by a large screen while an investigation continues inside.Zizzi is one of five sites in the small Wiltshire city of Salisbury at the heart of the operation. Earlier, Home Secretary Amber Rudd praised the professionalism of the police, who she said were proceeding at speed She said the government was using enormous resources to try to identify those responsible for the attempted murder.This investigation is focused on making sure that we keep people safe and also that we collect all the evidence so that when it comes to attribution [of the attack] we will be absolutely clear where it should be. The police have said that if anybody thinks they have any additional information they would welcome them coming forward. As part of the investigation, about 180 military personnel have been deployed to Salisbury to remove vehicles and objects which may have been contaminated.They include members of the Army and RAF, Royal Marines and others who are specially trained in chemical warfare and decontamination.On Saturday, police were active at the cemetery where Ms Skripal's brother, Alexander Skripal, and mother, Liudmila Skripal are buried."
    textR2 = "The Financial Times and Pearson, the world’s leading learning company, today unveiled a new FT Education API that offers students and educators the opportunity to access free, award-winning content from the Financial Times.The API, created on Pearson’s developer platform, enables free access to FT articles, 30 days after original publication. Access to this rich library of content can help students bring learning to life with real world case studies and context and develop a deeper understanding of global business, economic, political and social issues.The University of St Gallen in Switzerland is an early adopter of the new royalty free licence. It uses articles to create case studies for students to use in preparation for mock job interviews, equipping them for competitive job markets.Professor Simon Evenett, Academic Director at St Gallen (MBA) commented on the potential of the licence: The feedback on the use of FT articles in our Learning Assessment Week has been excellent. It really helped to clarify what the students need to do in the classroom, and they’ve started reading the FT more regularly because of it. The professors on the panel thought the range of articles was great, and the corporate partners really liked the way that students were focusing on the themes in the news and seeing the big picture.Diana Stepner, Head of Future Technologies at Pearson, added: Online learning is changing the way we teach and how students interact in and out of the classroom. There are so many new exciting possibilities and injecting world class FT journalism into this new learning environment is a powerful way to engage with students and help them make a real impact while studying and in the job market.Caspar de Bono, Managing Director B2B, Financial Times, said: Employers want to hire students who are able to apply theory in practice and are well informed of commercial issues and international markets. This licence and API are designed to help educators use articles from the FT in the creation of new engaging learning resources."
    textR3 = "Scotland Yard is investigating a possible hate crime after reports a letter encouraging people to punish a Muslim was posted in London. The threatening letter, which has also been circulated online, urged its recipients to join a national day of violence against Muslims in April.It asked people to carry out violent acts including verbal abuse, removing a woman’s hijab or head-scarf, physical assault and using acid as a weapon. These were ranked using a points-based system, with the letter stating: There will be rewards based on action taken.The Met Police confirmed on Saturday that it is investigating the letter and added that no one has been arrested.A spokesman said: Police are investigating a report of malicious communications in a letter having been sent to the occupants of a residential address in east London.A further report has been received from a member of the public in the SW4 area who received a copy of a letter through Whatsapp.The MPS does not tolerate any form of hate crime. If anyone believes they have been a victim of such an offence we would encourage them to report it to police so it can be fully investigated.”"

    meanFQs = getQs(text1, "?") + getQs(text2, "?") + getQs(text3, "?")
    meanFExs = getQs(text1, "!") + getQs(text2, "!") + getQs(text3, "!")

    meanRQs = getQs(textR1, "?") + getQs(textR2, "?") + getQs(textR3, "?")
    meanRExs = getQs(textR1, "!") + getQs(textR2, "!") + getQs(textR3, "!")

    myCoOrd1F = [getQs(text1, "?"), getQs(text1, "!")]
    myCoOrd2F = [getQs(text2, "?"), getQs(text2, "!")]
    myCoOrd3F = [getQs(text3, "?"), getQs(text3, "!")]
    Fcoords = [myCoOrd1F, myCoOrd2F, myCoOrd3F]

    myCoOrd1R = [getQs(textR1, "?"), getQs(textR1, "!")]
    myCoOrd2R = [getQs(textR2, "?"), getQs(textR2, "!")]
    myCoOrd3R = [getQs(textR3, "?"), getQs(textR3, "!")]
    Rcoords = [myCoOrd1R, myCoOrd2R, myCoOrd3R]
    dist = []
    myCoOrdsText = [getQs(text,"?"), getQs(text,"!")]
    for i in range(0, len(Fcoords)):
        dist.append(math.sqrt((myCoOrdsText[0] - Fcoords[i][0])**2 + (myCoOrdsText[1] - Fcoords[i][1])**2))
    for j in range(0, len(Rcoords)):
        dist.append(math.sqrt((myCoOrdsText[0] - Rcoords[j][0])**2 + (myCoOrdsText[1] - Rcoords[j][1])**2))

    x = dist.index(min(dist))
    dist[x] = -100
    y = dist.index(min(dist))

    if (x < 3 and y < 3):
        return "F"
    else:
        return "R"



# see if the given link is in the bad sites list
def find_in_db(u):
    return str(u.strip().replace('\n', '')) in bad_sites


def get_content(url):
    url = 'http://'+str(url) if not str(url).startswith('http://') else url
    url = requests.get(url)
    soup = BeautifulSoup(url.content, "lxml")
    l = []
    for p in soup.find_all('p'):
        string = p.text.replace("\"", "\\\"").replace("\'", "\\'")
        l.append(string)
    return " ".join(l)

import http.client, urllib.parse, json

def spelling_check(text):
    #req = requests.request('GET', 'https://api.fakenewsdetector.org/links/all')
    params = {'mkt': 'en-US', 'mode': 'proof', 'text': text}
    key = "d65534e9381546e6997bdcd1e10dbd81"
    host = 'api.cognitive.microsoft.com'
    path = '/bing/v7.0/spellcheck'
    headers = {'Ocp-Apim-Subscription-Key': key,
               'Content-Type': 'application/x-www-form-urlencoded'}
    conn = http.client.HTTPSConnection(host)
    params = urllib.parse.urlencode(params)
    conn.request("POST", path, params, headers)
    response = conn.getresponse()
    x = response.read().decode('utf-8')
    y = json.loads(x)
    return(len(y["flaggedTokens"]))

import re

def url_check(myString):
    myString_list = [item for item in myString.split(" ")]
    urls = []
    for item in myString_list:
        try:
            urls.append (re.search("(?P<url>https?://[^\s]+)", item).group("url"))
        except:
            pass
    return (urls)


goodsites = ["https://www.economist.com/",
             "https://uk.reuters.com/"]

import botometer

# set up the botometer
mashape_key = 'C0eUvCzWdDmshsbXAnK53fQRJUTtp1Km5x1jsnTQ2tMwIUruEp'
twitter_app_auth = {
    'consumer_key': 'rpmEbImgFwEHzOUFifA1peRcw',
    'consumer_secret': 'agIECASC9skRiOVmanRVJO4XlDbTRk4vGU8a8lPBLl3OybkD6n',
    'access_token': '972495546719010817-mjkyaHgxXExdrUFLfzOtt5F3K1cm0wJ',
    'access_token_secret': '2ylFoxJ5W09JFTfACVtTzmzVOlUX48B1Uao4ktZccmOPQ'
}


# call this with the user url to check its scores
def check_user(id=None, screen_name=None):
    bom = botometer.Botometer(wait_on_ratelimit=True, mashape_key=mashape_key,**twitter_app_auth)
    result = None
    if id is not None:
        # check by user id
        result = bom.check_account(id)
    elif screen_name is not None:
        # check by screen name
        result = bom.check_account(screen_name)
    else:  # some nonsense with the params
        return None

    # content * 2 / 7
    print("original:")
    print(result)
    print()
    print("new average:")
    avg = 0
    for key, value in result['categories'].items():
        if key == 'content':
            avg += 2*value
        avg += value
    return ((avg/7))


@app.route('/')
def index():
    return render_template('selection.html')

@app.route('/tbot', methods=['POST', 'GET'])
def tbot():
    id = request.values.get('name', None)
    x = check_user(id)
    if (x < 0.65):
        return jsonify(result='Legit')
    return jsonify(result='Bot')

@app.route('/fbot', methods=['POST', 'GET'])
def fbot():
    id = request.values.get('name', None)
    x = check_user(id)
    if (x < 0.65):
        return jsonify(result='Legit')
    return jsonify(result='Bot')


@app.route('/fnews', methods=['POST', 'GET'])
def fnews():
    # print(request.values)
    url = request.values.get('url', None)
    overallScore = 0
    print(url)
    content = get_content(url)
    if url in analyser():
        return jsonify(result='Fake')
    if (calcDist(content) == "F"):
        overallScore = overallScore + 1
    for i in url_check(content):
        if i in analyser():
            return jsonify(result='Fake')

    overallScore = overallScore + spelling_check(content)

    file = open('params.txt', 'w')  # will contain the parameter to run
    file.write(content)
    file.close()
    command = 'python gsearch.py'
    run = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = run.communicate()
    flag = False
    if (error == 0):
        results = open("gsr.txt", 'r')
        searches = results.readlines()
        for i in searches:
            if i in goodsites:
                flag = True
    if(flag == False): overallScore = overallScore + 3;

    if(overallScore > 10):
        return jsonify(result='Fake')
    return jsonify(result='Legit')


if __name__ == '__main__':
    app.run()
