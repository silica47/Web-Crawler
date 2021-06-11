import requests
from requests.api import get
import re
import urllib.parse
import argparse
import pyfiglet

banner = pyfiglet.figlet_format("Crawler", font = "slant")
print(banner)

def getArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", dest="target", help="Enter the target URL")
    options = parser.parse_args()
    return options

options = getArguments()
target_url = options.target
target_links = []

def extract_links_from(url):
    response = requests.get(target_url)
    return re.findall('(?:href=")(.*?)"', response.content.decode('utf-8'))

def crawl(url):
    href_links = extract_links_from(url)
    for link in href_links:
        link = urllib.parse.urljoin(url, link)

        if "#" in link:
            link = link.split("#")[0]

        if target_url in link and link not in target_links:
            target_links.append(link)
            print(link)
            crawl(link)
    
crawl(target_url)