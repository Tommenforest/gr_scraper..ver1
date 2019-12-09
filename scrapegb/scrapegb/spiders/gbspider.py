import scrapy
#from ..items import ScrapegbItem

class QuotesSpider(scrapy.Spider):
    name = "scraip2"
    page_number = 2
    start_urls = [
        'https://www.globalresearch.ca/theme/us-nato-war-agenda',

    ]

    def parse(self, response):


        all_div_quotes = response.css('div.article')

        for quote in all_div_quotes:
            yield {
                "otsikko": quote.css('.title a::text') .extract()
                    }

        next_page = "https://www.globalresearch.ca/theme/us-nato-war-agenda/page/" + str(QuotesSpider.page_number) + "/"

        if next_page is not None:
            QuotesSpider.page_number += 1

            yield response.follow(next_page, callback=self.parse)