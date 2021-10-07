"""
    Open Closed Principle
    Felipe Tavoni, 758707

    The following code implements the SRP and OCP from the S.O.L.I.D. principles in a online news scraper.
"""

from Strategy import Strategy, PrintConsole, PrintCSV
from WebsiteSources import NewsFromG1, NewsFromUOL, NewsFromElPais, NewsFromSA

# Main. Run the application.
if __name__ == "__main__":
    globo = NewsFromG1(None)
    globo.getNews()
    globo.setStrategy(PrintCSV())
    globo.strategy.execute_algorithm(globo.news)
    globo.setStrategy(PrintConsole())
    globo.strategy.execute_algorithm(globo.news)

    uol = NewsFromUOL(PrintConsole())
    uol.getNews()
    uol.strategy.execute_algorithm(uol.news)

    elpais = NewsFromElPais(PrintConsole())
    elpais.getNews()
    elpais.strategy.execute_algorithm(uol.news)

    scienAmer = NewsFromSA(PrintConsole())
    scienAmer.getNews()
    scienAmer.strategy.execute_algorithm(scienAmer.news)