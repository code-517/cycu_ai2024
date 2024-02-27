print("Hello, World!")

#https://news.pts.org.tw/xml/newsfeed.xml
import requests
import feedparser
import csv
def print_titles(rss_url):
    response = requests.get(rss_url)
    feed = feedparser.parse(response.content)
    for post in feed.entries:
        print(post.title)
        print('-' * 50)

# 使用你提供的RSS feed URL
print_titles('https://news.pts.org.tw/xml/newsfeed.xml')
#印出summary
def print_summary(rss_url):
    response = requests.get(rss_url)
    feed = feedparser.parse(response.content)
    for post in feed.entries:
        print(post.summary)
        print('-' * 50)
print_summary('https://news.pts.org.tw/xml/newsfeed.xml')
#讀取title裡面有提到youbike的新聞
#在幫我用csv存起來存到路徑是C:\Users\User\Desktop\11022345\cycu_ai2024\20240227
#檔案名稱叫11022345.csv
#寫進去他內容是亂碼，請幫我轉成big5

def print_youbike(rss_url):
    response = requests.get(rss_url)
    feed = feedparser.parse(response.content)
    with open('C:\\Users\\User\\Desktop\\11022345\\cycu_ai2024\\20240227\\11022345.csv', 'w', newline='', encoding='big5') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['title', 'summary'])
        for post in feed.entries:
            if 'YouBike' in post.title:
                writer.writerow([post.title, post.summary])

print_youbike('https://news.pts.org.tw/xml/newsfeed.xml')
