import requests

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

compare("hi")