from data_collecting import Scraper

url = "https://www.macrotrends.net/stocks/charts/MSFT/microsoft/stock-price-history"
data_set = Scraper(url).get_data()

