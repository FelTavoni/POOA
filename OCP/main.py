"""
    Open Closed Principle
    Felipe Tavoni, 758707

    The following code implements the SRP and OCP from the S.O.L.I.D. principles in a online news scraper.
"""

from Viewer import Viewer
from WebsiteSources import NewsFromG1, NewsFromUOL, NewsFromElPais, NewsFromSA

# Main. Run the application.
if __name__ == "__main__":
    globo = NewsFromG1()
    globo.getNews()
    Viewer.printConsole(globo.news)

    uol = NewsFromUOL()
    uol.getNews()
    Viewer.printCSV(uol.news)

    elpais = NewsFromElPais()
    elpais.getNews()
    Viewer.printConsole(elpais.news)

    scienAmer = NewsFromSA()
    scienAmer.getNews()
    Viewer.printConsole(scienAmer.news)
    