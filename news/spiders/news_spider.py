import scrapy
from ..items import NewsItem
from selenium import webdriver


class NewsUrlSpider(scrapy.Spider):
    name = 'newsUrl'

    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.implicitly_wait(3)
    driver.get('')

    # def start_requests(self):
    #     yield scrapy.Request("https://www.boannews.com/media/o_list.asp", self.parse_url)
    #
    # def parse_url(self, response):
    #     for news in response.xpath('//div[@id="news_area"]/div[@class="news_list"]'):
    #         temp_url = ''.join(['https://www.boannews.com'] + news.xpath('a[2]/@href').extract())
    #         request = scrapy.Request(temp_url, callback=self.parse_news)
    #
    #         yield request
    #
    # def parse_news(self, response):
    #     item = NewsItem()
    #
    #     item['title'] = response.xpath('//*[@id="news_title02"]/text()').extract()
    #     item['content'] = response.xpath('//*[@id="news_content"]/text()').extract()
    #     item['date'] = response.xpath('//*[@id="news_util01"]/text()').extract()
    #     item['url'] = response.xpath('/html/head/link[2]/@href').extract()
    #
    #     print(item['url'])
    #
    #     yield item
