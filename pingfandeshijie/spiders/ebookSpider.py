import scrapy
from pingfandeshijie.items import PingfandeshijieItem
import time
import random

count = 1

class EbookspiderSpider(scrapy.Spider):
    name = 'ebookSpider'
    allowed_domains = ['mingzhuxiaoshuo.com']
    # 1
    start_urls = ['http://www.mingzhuxiaoshuo.com/jinxiandai/99/3481.Html']
    # 13
    #start_urls = ['http://www.mingzhuxiaoshuo.com/jinxiandai/99/4314.Html']



    def parse(self, response):

        P_text = PingfandeshijieItem()

        global count
        #P_text['title'] = response.xpath("//H1/text()").get()




        P_text['title'] = response.xpath("//body/h1/text()").get()

        # chapter1-12
        #iterParagraph = response.xpath("//body/div[@class='width']/p/text()").getall()

        #chapter13
        #iterParagraph = response.xpath("//body/div[@class='width']/div/text()").getall()

        if count < 13:
            iterParagraph = response.xpath("//body/div[@class='width']/p/text()").getall()
        else:
            iterParagraph = response.xpath("//body/div[@class='width']/div/text()").getall()

        content = ' '
        for i in iterParagraph:
            content =content + i + '\n'

        P_text['paragraph'] = content

        yield P_text

        next = response.xpath("//div[@id='thumb']/a[4]/@href").get()

        if next:

            count = count + 1

            next_p = 'http://www.mingzhuxiaoshuo.com' + next

            yield scrapy.Request(next_p, callback=self.parse)

        time.sleep(random.randint(3,8))


