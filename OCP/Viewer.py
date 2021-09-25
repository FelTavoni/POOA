# Class in charge of showing the search results.
class Viewer:

    @staticmethod
    def printConsole(newsList):
        for news in newsList:
            print(news[0], news[1], news[2])
        pass