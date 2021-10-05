from bs4 import BeautifulSoup
from urllib.request import urlopen

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
    def Scrap(editor, url, html_tag, html_class):
        output = []

        html = urlopen(url)
        bs = BeautifulSoup(html, 'lxml')
        news = bs.find_all(html_tag, class_=html_class)
        for i in news:
            output.append((
                    editor,
                    Scraper.getNewsText(i),
                    Scraper.getNewsLink(i)
                ))

        return output
    
    pass