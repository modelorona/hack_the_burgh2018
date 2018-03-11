import GettingData as G
<<<<<<< HEAD
import scraper as s
from datetime import datetime
=======
from flask import scraper as s
>>>>>>> 9656bf0bba022dc51ce5106ef02357116b00a9a3

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
    scoreData = 0
    number_of_iterations = 0
    dateList = []
    dateobject = datetime.strptime("11 March 2018", '%d %B %Y')
    for dicts in s.returnUrlData(LINK):
        if dicts["time_stamp"][-4:-3] == "2":
            dateList += [(dateobject - datetime.strptime(dicts["time_stamp"], '%d %B %Y')).days]
            dateobject = datetime.strptime(dicts["time_stamp"], '%d %B %Y')
    print (dateList)
    return 0



    #May want to implement checking the url address of the sites that include this image agains the database of fake news sites.

def isFake (LINK):
    returnScoreLabels(LINK)
    returnScoreText(LINK)



print(returnScoreText("https://www.facebook.com/PenelopeCruzOfficial/"))
print(returnScoreText("https://www.facebook.com/motiwafashiondesinger/"))
rint(returnScoreText("https://www.facebook.com/FitnessMotivation123/"))
print(returnScoreText("https://www.facebook.com/pavers.shoes/"))
print(returnScoreText("https://www.facebook.com/BruceLee"))


print(returnScoreLabels("https://www.facebook.com/PenelopeCruzOfficial/"))
print(returnScoreLabels("https://www.facebook.com/motiwafashiondesinger/"))
print(returnScoreLabels("https://www.facebook.com/FitnessMotivation123/"))
print(returnScoreLabels("https://www.facebook.com/pavers.shoes/"))
print(returnScoreLabels("https://www.facebook.com/BruceLee"))