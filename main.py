from data_collecting import Scraper
from ForcastAlgorithm import forcast_algorithm

def test_forcast_algorithm(data_set: list):
    expected_result = data_set.pop()
    print("Found Result:", forcast_algorithm(data_set))
    print("Required Result:", expected_result)

url = "https://www.macrotrends.net/stocks/charts/MSFT/microsoft/stock-price-history"

data_set = Scraper(url).get_simple_data()

print(forcast_algorithm(data_set))
test_forcast_algorithm(data_set)




