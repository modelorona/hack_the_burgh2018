from flask import Flask
from flask import request
import subprocess
from flask import render_template
from flask import jsonify
import requests
import math
from bs4 import BeautifulSoup


app = Flask(__name__, template_folder='templates')
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
    return render_template('twitterEntry.html')

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
