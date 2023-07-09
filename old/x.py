import csv
import urllib
from urllib.parse import urlparse
def fix_url(url):
    url  = url.replace('https://', '')
    url = url.replace('http://', '')
    if '/' in url:
        url = url.split('/')[0]
    return url
with open('/old/export.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    rows_count = 0
    urls = list()
    for row in reader:
        id, url = row
        url = fix_url(url)
        urls.append(url)



print(len(urls))
unique = set(urls)
print(len(unique))
with open('clean_domains.txt', 'w') as file:
    for url in unique:
        file.write(url + '\n')


