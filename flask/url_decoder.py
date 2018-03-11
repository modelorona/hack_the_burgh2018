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

print(url_check("This is my tweet check it out http://tinyurl.com/blah and http://blabla.com"))