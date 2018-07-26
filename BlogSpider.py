
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://juejin.im/']
    print(963)
    def parse(self, response):
        yield response

        # for title in response.css('.info-row .title-row'):
        #     yield {'title':title.css('a ::text').extract_first()}

        # for next_page in response.css('div.prev-post > a'):
        #     yield response.follow(next_page,self.parse)

