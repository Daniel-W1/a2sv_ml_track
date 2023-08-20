from bs4 import BeautifulSoup
import csv

csv_file = open('scrape.csv', 'w', encoding="utf-8")
csv_writer = csv.writer(csv_file)

with open('data.txt', 'r', encoding="utf-8") as file:
    soup = BeautifulSoup(file, 'lxml')

    # get the div containing all the latest new li elements
    latest_news = soup.find_all('div', class_='W8yrY')

    for news in latest_news:
        title = news.find('h4', class_='gPFEn').text
        timeStamp = news.find('time', class_ = 'hvbAAd').text
        articles = news.find_all('article')

        # extract the url from the articles
        urls = []
        for article in articles:
            url = article.find('a')['href']
            urls.append('https://news.google.com' + url[1:])

        # print(title)
        # print(timeStamp)
        # print(urls)

        csv_writer.writerow([title, timeStamp, urls])

csv_file.close()
