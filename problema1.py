import requests
import csv

class StockItem(object):
    def __init__(self, date, open, high, close, volume):
        self.date = date
        self.open = open
        self.high = high
        self.close = close
        self.volume = volume

    def get_date(self):
        return self.date

    def get_open(self):
        return self.open

    def get_high(self):
        return self.high

    def get_close(self):
        return self.close

    def get_volume(self):
        return self.volume

    def __repr__(self):
        return "StockItem(%s, %s, %s, %s, %s)" % (self.date, self.open, self.high, self.close, self.volume)

    def __eq__(self, other):
        if isinstance(other, StockItem):
            return ((self.date == other.date) and (self.open == other.open) and (self.high == other.high) and (self.close == other.close) and (self.volume == other.volume))
        else:
            return False

    def __ne__(self, other):
        return (not self.__eq__(other))

    def __hash__(self):
        return hash(self.__repr__())

class GetStockFinance(object):

    def __init__(self, url, stockindex):
        self.url = url
        self.stockindex = stockindex

    def get_stock_finance(self):
        download = requests.get(self.url+self.stockindex+'.csv')
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        return list(cr)

    # def get_stock_finance_return_set(self):
    #     #.............
    #     return set_obiecte_StockItem

class WriteToCsv(object):

    def __init__(self, filename):
        self.filename = filename

    def write_to_csv(self, continut):
        with open(self.filename, 'w') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(continut)

with open('test.csv', newline='') as csvfile:
    deschide = csv.reader(csvfile)

print(deschide)

# x = OpenFile()
# print(x)

# a = GetStockFinance('https://www.quandl.com/api/v3/datasets/WIKI/','AAPL')
# csv_de_scris = a.get_stock_finance()
# b = WriteToCsv(r'test.csv')
# b.write_to_csv(csv_de_scris)
