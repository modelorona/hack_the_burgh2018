from google import google


def clean_url(url):
    # remove https/http
    url = url.replace('http://', '').replace('https://', '')
    # now get everything before the first slash as that is the domain name
    return url.split('/')[0]


# does a google search, then
def search(url):
    url = url.strip().replace('\n', "")
    title = 'poisoned russian spy linked to dossier author christopher steele'
    search_results = google.search(title)
    cleaned_urls = [clean_url(r.link) for r in search_results]
    file = open('gsr.txt', 'w+')
    for r in cleaned_urls:
        file.write(str(r) + '\n')
    file.write('EOL\n\n')  # to signify the end of this one search
    file.close()


if __name__ == '__main__':
    f = open('params.txt', 'r')
    p = f.readline()
    f.close()
    search(p)

