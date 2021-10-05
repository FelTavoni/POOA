# Holds the websites in which data must be retrieved.
# To extract the data of a website, simply create a class and set it's url, html tag and class type.

from Scraper import Scraper

class NewsFromSource:
    
    def __init__(self, source, url, htlm_tag, html_class):
        self.source = source 
        self.url = url
        self.html_tag = htlm_tag
        self.html_class = html_class
        self.news = []

    def getNews(self):
        self.news = Scraper.Scrap(self.source, self.url, self.html_tag, self.html_class)
        

class NewsFromG1(NewsFromSource):

    def __init__(self):
        NewsFromSource.__init__(self, "G1", "https://g1.globo.com/", "a", "feed-post-link")

    pass

class NewsFromUOL(NewsFromSource):

    def __init__(self):
        NewsFromSource.__init__(self, "UOL", "https://noticias.uol.com.br/", "h3", "thumb-title")

    pass

class NewsFromElPais(NewsFromSource):

    def __init__(self):
        NewsFromSource.__init__(self, "EL PAÍS", "https://brasil.elpais.com/", "a", "")

    pass

class NewsFromSA(NewsFromSource):

    def __init__(self):
        NewsFromSource.__init__(self, "S.A.", "https://www.scientificamerican.com/", "h2", "t_small-listing-title")

    pass