from urllib import response
import scrapy


class BestsellersSpider(scrapy.Spider):
    name = 'bestsellers'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        products = response.xpath("//div[@id='product-lists']/div")
        for product in products:
            yield {
                'name': product.xpath("normalize-space(.//div[@class='p-title']/a/text())").get(),
                'url': product.xpath(".//div[@class='product-img-outer']/a/@href").get(),
                'img_url': product.xpath(".//img[@class='lazy d-block w-100 product-img-default']/@data-src").get(),
                'price': product.xpath(".//div[@class='p-price']//span/text()").get()
            }

        next_page = response.xpath(
            "//ul[@class='pagination']/li[position() = last()]/a/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
            