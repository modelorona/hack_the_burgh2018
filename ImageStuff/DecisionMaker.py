import GettingData as G
from flask import scraper as s

most_common_spam_words = ["4U", "Accept", "credit", "cards", "Act", "now!", "Don’t", "hesitate!", "Additional", "income", "Addresses", "on", "CD", "All", "natural", "Amazing", "Apply", "Online", "As", "seen", "on", "Auto", "email", "removal", "Avoid", "bankruptcy", "Be", "amazed", "Be", "your", "own", "boss", "Being", "a", "member", "Big", "bucks", "Bill", "1618", "Billing", "address", "Billion", "dollars", "Brand", "new", "pager", "Bulk", "email", "Buy", "direct", "Buying", "judgments", "Cable", "converter", "Call", "free", "Call", "now", "Calling", "creditors", "Can’t", "live", "without", "Cancel", "at", "any", "time", "Cannot", "be", "combined", "with", "any", "other", "offer", "Cash", "bonus", "Cashcashcash", "Casino", "Cell",", ""phone", "cancer", "scam", "Cents", "on", "the", "dollar", "Check", "or", "money", "order", "Claims", "not", "to", "be", "selling", "anything", "Claims", "to", "be", "in", "accordance", "with", "some", "spam", "law", "Claims", "to", "be", "legal", "Join", "millions", "of", "Americans", "Laser", "printer", "Limited", "time", "only", "Long", "distance", "phone", "offer", "Lose", "weight", "spam", "Lower", "interest", "rates", "Lower", "monthly", "payment", "Lowest", "price", "Luxury", "car", "Mail", "in", "order", "form", "Marketing", "solutions", "Mass", "email", "Meet", "singles", "Member", "stuff", "Message", "contains", "disclaimer", "MLM", "Money", "back", "Money", "making", "Month", "trial", "offer", "More", "Internet", "traffic", "Mortgage", "rates", "Multi", "level", "marketing", "Name", "brand", "New", "customers", "only", "New", "domain", "extensions", "Nigerian", "No", "age", "restrictions", "No", "catch", "No", "claim", "forms", "No", "cost", "No", "credit", "check", "No", "disappointment", "No", "experience", "No", "fees", "No", "gimmick", "No", "inventory", "No", "investment", "No", "medical", "exams", "No", "middleman", "No", "obligation", "No", "purchase", "necessary", "Unsecured", "credit/debt", "Urgent", "US", "dollars", "Vacation", "offers", "Viagra", "and", "other", "drugs", "Wants", "credit", "card", "We", "hate", "spam", "Claims", "you", "are", "a", "winner", "Claims", "you", "registered", "with", "Some", "Kind", "of", "Partner", "Click", "below", "Click", "here", "link", "Click", "to", "remove", "Click", "to", "remove", "mailto", "Compare", "rates", "Compete", "for", "your", "business", "Confidentially", "on", "all", "orders", "Congratulations", "Consolidate", "debt", "and", "credit", "Copy", "accurately", "Copy", "DVDs", "Credit", "bureaus", "Credit", "card", "offers", "Cures", "baldness", "Dear", "email", "Dear", "friend", "Dear", "somebody", "Different", "reply", "to", "Dig", "up", "dirt", "on", "friends", "Direct", "email", "Direct", "marketing", "Discusses", "search", "engine", "listings", "Do", "it", "today", "Don’t", "delete", "Drastically", "reduced", "Earn", "per", "week", "Easy", "terms", "Eliminate", "bad", "credit", "Email", "harvest", "Email", "marketing", "Expect", "to", "earn", "Fantastic", "deal", "Fast", "Viagra", "delivery", "Financial", "freedom", "Find", "out", "anything", "For", "free", "No", "questions", "asked", "No", "selling", "No", "strings", "attached", "Not", "intended", "Off", "shore", "Offer", "expires", "Offers", "coupon", "Offers", "extra", "cash", "Offers", "free", "(often", "stolen)", "passwords", "Once", "in", "lifetime", "One", "hundred", "percent", "free", "One", "hundred", "percent", "guaranteed", "One", "time", "mailing", "Online", "biz", "opportunity", "Online", "pharmacy", "Only", "$", "Opportunity", "Opt", "in", "Order", "now", "Order", "status", "Orders", "shipped", "by", "priority", "mail", "Outstanding", "values", "Pennies", "a", "day", "People", "just", "leave", "money", "laying", "around", "Please", "read", "Potential", "earnings", "Print", "form", "signature", "Print", "out", "and", "fax", "Produced", "and", "sent", "out", "Profits", "Promise", "you", "…!", "Pure", "profit", "Real", "thing", "Refinance", "home", "Removal", "instructions", "Remove", "in", "quotes", "Remove", "subject", "Removes", "wrinkles", "Reply", "remove", "subject", "Requires", "initial", "investment", "Reserves", "the", "right", "We", "honor", "all", "Weekend", "getaway", "What", "are", "you", "waiting", "for?", "While", "supplies", "last", "While", "you", "sleep", "Who", "really", "wins?", "Why", "pay", "more?", "For", "instant", "access", "For", "just", "$", "(some", "amt)", "Free", "access", "Free", "cell", "phone", "Free", "consultation", "Free", "DVD", "Free", "grant", "money", "Free", "hosting", "Free", "installation", "Free", "investment", "Free", "leads", "Free", "membership", "Free", "money", "Free", "offer", "Free", "preview", "Free", "priority", "mail", "Free", "quote", "Free", "sample", "Free", "trial", "Free", "website", "Full", "refund", "Get", "It", "Now", "Get", "paid", "Get", "started", "now", "Gift", "certificate", "Great", "offer", "Guarantee", "Have", "you", "been", "turned", "down?", "Hidden", "assets", "Home", "employment", "Human", "growth", "hormone", "If", "only", "it", "were", "that", "easy", "In", "accordance", "with", "laws", "Increase", "sales", "Increase", "traffic", "Insurance", "Investment", "decision", "It's", "effective", "Reverses", "aging", "Risk", "free", "Round", "the", "world", "S", "1618", "Safeguard", "notice", "Satisfaction", "guaranteed", "Save", "$", "Save", "big", "money", "Save", "up", "to", "Score", "with", "babes", "Section", "301", "See", "for", "yourself", "Sent", "in", "compliance", "Serious", "cash", "Serious", "only", "Shopping", "spree", "Sign", "up", "free", "today", "Social", "security", "number", "Special", "promotion", "Stainless", "steel", "Stock", "alert", "Stock", "disclaimer", "statement", "Stock", "pick", "Stop", "snoring", "Strong", "buy", "Stuff", "on", "sale", "Subject", "to", "credit", "Supplies", "are", "limited", "Take", "action", "now", "Talks", "about", "hidden", "charges", "Talks", "about", "prizes", "Tells", "you", "it’s", "an", "ad", "Terms", "and", "conditions", "The", "best", "rates", "The", "following", "form", "They", "keep", "your", "money", "—", "no", "refund!", "They’re", "just", "giving", "it", "away", "This", "isn’t", "junk", "This", "isn’t", "spam", "University", "diplomas", "Unlimited", "Will", "not", "believe", "your", "eyes", "Winner", "Winning", "Work", "at", "home", "You", "have", "been", "selected", "Your", "income",]

def returnTheScore(LINK):
    score = 0
    numer_of_iterations = 0
    for link in s.returnImageUrls(LINK)[::2]:
        dataOfImage = G.dataOnImage(str(link))
        for label in dataOfImage["labels"]:
            for word in label[0].split(' '):
                if word in most_common_spam_words:
                    score += label[1]
                numer_of_iterations += 1


    #May want to implement checking the url address of the sites that include this image agains the database of fake news sites.


    return score/numer_of_iterations


#returnTheScore("https://www.facebook.com/motiwafashiondesinger/")
print (returnTheScore("https://www.facebook.com/FitnessMotivation123/"))