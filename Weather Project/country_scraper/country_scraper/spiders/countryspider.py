import scrapy
from country_scraper.items import StateItem


class CountryspiderSpider(scrapy.Spider):
    name = "countryspider"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Municipalities_of_the_Netherlands"]

    custom_settings = {
        'FEEDS' : {
            'booksdata.json': {'format': 'json', 'overwrite': True}
        }
    }

    def parse(self, response):

        table_rows = response.css("table.wikitable tbody tr")

        for state in range(len(table_rows)):

            state_item = StateItem()

            state_item['flag'] = response.xpath(f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[3]/tbody/tr[{state+1}]/th/table/tbody/tr/td[1]/span/span/span/img/@src').get()
            state_item['name'] = response.xpath(f'//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr[{state+1}]/th/table/tbody/tr/td[2]/a/@title').get()
            state_item['province'] = response.xpath(f'//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr[{state+1}]/td[2]/a/@title').get()
            state_item['population'] = response.xpath(f'//*[@id="mw-content-text"]/div[1]/table[3]/tbody/tr[{state+1}]/td[3]/span/text()').get()

            if state_item['flag'] and state_item['name'] and state_item['province'] and state_item['population']:
                yield state_item

        
