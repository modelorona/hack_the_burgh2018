#import requests
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

print(spelling_check("hollo wrld"))
