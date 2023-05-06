from typing import Any
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re


class Scraper:

    data: list[Any]
    url: str

    def __init__(self, url):
        self._url = url
        self._create_data_set()

    def _get_html(self) -> Any:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return urlopen(self._url, context=ctx).read()

    def _get_tags(self):
        html = self._get_html()
        soup = BeautifulSoup(html, "html.parser")
        return soup('tr')

    def _create_data_set(self):
        data = []
        tags = self._get_tags()

        for tag in tags:
            found_data = re.findall("([0-9]+.[0-9]*|-[0-9]+.[0-9])", tag.text)
            if len(found_data) == 7:
                for i in range(len(found_data)):
                    found_data[i] = float(found_data[i])
                data.append(found_data)

        data_set = []
        for i in data:
            data_set.append([{"year": int(i[0])},
                             {"avg_stock_price": i[1]},
                             {"year_open": i[2]},
                             {"year_high": i[3]},
                             {"year_low": i[4]},
                             {"year_close": i[5]},
                             {"annual_precent_change": i[6]}])
        self.data = data_set

    def get_data(self) -> list[Any]:
        return self.data

    def get_simple_data(self) -> list[[int, float]]:
        simple_data = []

        for i in self.data:
            temp_data = [i[0]['year'], i[1]['avg_stock_price']]
            simple_data.insert(0, temp_data)

        return simple_data
