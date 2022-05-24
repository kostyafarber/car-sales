from bs4 import BeautifulSoup
from datetime import date
import boto3
import json
import requests
from decimal import Decimal

class CarSalesScraper():
    def __init__(self, base_url, header) -> None:
        
        self.base_url = base_url
        self.header = header
        self.date = date.today().strftime('%Y-%m-%d')

    def _num_of_pages(self) -> int:
        """
        Generates the number of web pages from the base url that is used for carsales. 
        There are 12 results per page so the total number of pages will be:
             total results / 12

        Returns:
            int: Returns the number of web pages for your search results
        """
        request = requests.get(self.base_url, headers=self.header).text
        page_bs = BeautifulSoup(request, "html.parser")

        # title contains the number of web pages (e.g 96 Mazda 3s)
        title = page_bs.find('h1', {"class":"title"}).text.strip()
        # offset for car sales is 12
        num_of_pages = int((title[0:2]))//12

        return num_of_pages


    def make_page_url(self, base_url: str, offset: int) -> list[str]:
        """Generates a list of webpages to scrape

        Args:
            base_url (str): Base url used to generate all the subsequent webpages
            num_pages (int): Number of pages to scrape
            offset (int): offset used to increment web pages

        Returns:
            str: A list of web page urls
        """
        pages = []
        num_pages = self._num_of_pages()

        for i in range(num_pages):
            page = "".join((base_url, str(i*offset)))
            pages.append(page)

        return pages

    def make_bs(self, requests: list) -> list:
        """Generates all the Beautiful Soup objects for each webpage

        Args:
            requests (list): A list of requests

        Returns:
            list: Returns a list of bs objects.
        """
        pages_bs = []

        for request in requests:
            page_bs = BeautifulSoup(request, "html.parser")
            pages_bs.append(page_bs)

        return pages_bs

    def extract_tags(self, bs_list: list) -> list:
        """Extracts all relevant tags where prices are stored.

        Args:
            bs_list (list): A list of bs objects.

        Returns:
            list: Returns a list of tags.
        """
        tags = []

        for bs in bs_list:
            tag = bs.find_all("div", {"class": "price"})
            tags.append(tag)

        return tags

    def get_prices(self, tags: list) -> list:
        """Extracts all the prices from the tags and formats them into integers.

        Args:
            tags (list): A list of tags.

        Returns:
            list: Returns a list of car prices.
        """
        prices = []

        for page in tags:
            for tag in page:
                price = tag.text.strip().replace("*", "").strip("$").replace(",", "")
                prices.append(int(price))

        return prices

    def upload_prices(self, data: dict, table_name: str):
        """Uploads the car prices into a dynamodb table.

        Args:
            data dict: A dictionary of data points in the form: {date: '2022-02-02', mean: 20123.45, median: 23234.3}
            table_name str: The name of the dynamodb table.
        """
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(table_name)
        # to avoid type errors when writing floats
        data = json.loads(json.dumps(data), parse_float=Decimal)
        table.put_item(Item=data)

