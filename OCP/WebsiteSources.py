# Holds the websites in which data must be retrieved.
# To extract the data of a website, simply add it's url, html tag and class type.
class WebsiteSources:

    # Websites which we will be extracting the news.
    # They follow the structure: (editor, url, html tag, class type)
    sources = [("G1", "https://g1.globo.com/", "a", "feed-post-link"),
               ("UOL", "https://noticias.uol.com.br/", "h3", "thumb-title"),
               ("EL PAÍS", "https://brasil.elpais.com/", "a", ""),
               ("S.A.", "https://www.scientificamerican.com/", "h2", "t_small-listing-title")]

    @staticmethod
    def getWebsites():
        return WebsiteSources.sources

    pass