import scrapy


class LampsdivanSpider(scrapy.Spider):
    name = "lampsdivan"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svetilniki"]

    def parse(self, response):
        lamps = response.css("div.LlPhw")
        for lamp in lamps:
            yield {
                "name": lamp.css("div.wYUX2 span::text").get(),
                "price": lamp.css("div.pY3d2 span::text").get(),
                "url": 'divan.ru' + lamp.css('a').attrib['href']
            }
