"""
    Open Closed Principle
    Felipe Tavoni, 758707

    The following code implements the SRP and OCP from the S.O.L.I.D. principles in a online news scraper.
"""

from Scraper import Scraper
from Viewer import Viewer

# Main. Run the application.
if __name__ == "__main__":
    news = Scraper.Scrap()
    Viewer.printConsole(news)