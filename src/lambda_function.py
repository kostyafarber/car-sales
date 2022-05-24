import requests
from statistics import median, mean
from scraper.car_sales_scraper import CarSalesScraper

def lambda_handler(event, context):

    print("Scraping data...")
    print()

    header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"}
    base_url = 'https://www.carsales.com.au/cars/?q=(And.Service.carsales._.(C.Make.Mazda._.Model.3.)_.BodyStyle.Sedan._.GenericGearType.Automatic._.Year.range(2013..2014).)&offset=0'

    scraper = CarSalesScraper(base_url, header)

    page_urls = scraper.make_page_url(base_url, 12)
    print('Number of total web pages for your search results: {}'.format(scraper._num_of_pages()))
    print()

    all_requests = [requests.get(page, headers=header).text for page in page_urls]

    # create a list of beautiful soup objects from the urls
    pages_bs = scraper.make_bs(all_requests)

    # obtain all the tags that contain all the prices
    tags = scraper.extract_tags(pages_bs)

    # scrape prices and format into integers
    print("Extracting prices...")
    prices = scraper.get_prices(tags)
    median_price, mean_price, today = median(prices), mean(prices), scraper.date
    data = {"date": today, "mean": "{:.2f}".format(mean_price), "median": "{:.2f}".format(median_price)}

    scraper.upload_prices(data, 'mazda-prices-dev')
    print("Successfully uploaded {} to your dynamodb table.".format(data))












