from bs4 import BeautifulSoup
from urllib.request import urlopen
from WebsiteSources import WebsiteSources

# The Scrapper class. It scraps the news from the websites previously defined into `WebsiteSources`.
# Returns the news in the following structure (`news-source`, `news`)
class Scraper:

    @classmethod
    def getNewsText(cls, news):
        return news.getText()

    @classmethod
    def getNewsLink(cls, news):
        while (news != None) and (news.name != 'a'):
            news = news.parent
        return news['href']

    @staticmethod
    def Scrap():
        sources = WebsiteSources().getWebsites()
        output = []

        for editor, url, tag, foo in sources:
            html = urlopen(url)
            bs = BeautifulSoup(html, 'lxml')
            news = bs.find_all(tag, class_=foo)
            for i in news:
                output.append((
                        editor,
                        Scraper.getNewsText(i),
                        Scraper.getNewsLink(i)
                    ))

        return output
    
    pass