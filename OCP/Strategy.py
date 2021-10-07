import csv
from abc import ABC, abstractmethod
# Class in charge of showing the search results.
class Strategy(ABC):

    @abstractmethod
    def execute_algorithm(self, newsList):
        pass

    pass

class PrintConsole(Strategy):

    def execute_algorithm(self, newsList):
        for news in newsList:
            print(news[0], news[1], news[2])

    pass

class PrintCSV(Strategy):

    def execute_algorithm(self, newsList):
        header = ['source', 'title', 'link']
        with open(newsList[0][0]+'News.csv', 'w', encoding='UTF-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            for news in newsList:
                writer.writerow([news[0], news[1], news[2]])

    pass