#https://www.cwa.gov.tw/V8/C/S/eservice/rss.html
import requests
from bs4 import BeautifulSoup
import feedparser
import urllib.parse
import geopandas as gpd
# Read shp data of Taiwan county 
# 縣市界
County_data = gpd.read_file("C:/Users/User/Desktop/mapdata202301070205/COUNTY_MOI_1090820")
print(County_data)
base_url = 'https://www.cwa.gov.tw/V8/C/S/eservice/rss.html'
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

rss_links = [urllib.parse.urljoin(base_url, a['href']) for a in soup.find_all('a', href=True) if 'rss' in a['href']]

# 遍歷所有的RSS鏈接
for link in rss_links:
    feed = feedparser.parse(link)

    for entry in feed.entries:
        print(f"標題: {entry.title}")
        print("---")
