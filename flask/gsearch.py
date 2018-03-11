from google import google
# from bs4 import BeautifulSoup
# import requests


def clean_url(url):
    # remove https/http
    url = url.replace('http://', '').replace('https://', '')
    # now get everything before the first slash as that is the domain name
    return url.split('/')[0]


# # getting a webpage, parse it and get the title element as well as some social meta tags and try to build a title out of it
# def get_title(page):
#     page = requests.get('http://' + page)  # should not be a problem with http/s. www must be added if it contains it
#     soup = BeautifulSoup(page.content, 'lxml')
#     title = soup.title.string
#     print(title)
#     return 0


# does a google search, then
def search(article_name):
    # title = get_title(url)
    search_results = google.search(article_name, 3)
    cleaned_urls = [clean_url(r.link) for r in search_results]
    file = open('gsr.txt', 'w+')
    for r in cleaned_urls:
        file.write(str(r) + '\n')
    # file.write('EOL\n\n')  # to signify the end of this one search
    file.close()


if __name__ == '__main__':
    f = open('params.txt', 'r')
    p = f.readline().strip().replace('\n', '').replace('_', ' ')  # name will be with underscores to be one parameter
    f.close()
    search(p)

