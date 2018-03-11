import GettingData as G
import scraper as s

def returnTheScore(LINK):
    G.dataOnImage()
    score = 0
    for link in s.returnImageUrls(LINK)[::2]:
        


    return score



print(returnImageUrls("https://www.facebook.com/motiwafashiondesinger/"))
returnTheScore("https://www.facebook.com/motiwafashiondesinger/")