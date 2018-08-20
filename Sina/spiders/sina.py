# -*- coding: utf-8 -*-
import scrapy
import js2py

from Sina.items import SinaItem

import json
class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php?col=89&spec=&type=&ch=01&k=&offset_page=0&offset_num=0&num=60&asc=&page=1'.format(i) for i in range(1, 275)]


    def parse(self, response):
        resp = response.body.decode('gbk')
        # str = resp.split('list : ')[-1]
        # list1 = list(str[:str.rfind('}')])
        #
        # print(list1)
        # print(type(list1))

        ret = js2py.eval_js(resp)

        for news in ret.list:

            item = SinaItem()
            sort = news['channel']['title']
            title = news['title']
            url = news['url']
            time = news['time']

            item['sort'] = sort
            item['title'] = title
            item['time'] = time
            item['url'] = url

            yield item
            yield scrapy.Request(item['url'], meta={'detail_item':item}, callback=self.parse_page)

    def parse_page(self, response):
        item = response.meta["detail_item"]

        item['real_time'] = response.xpath('//span[@class="date"]/text()').extract_first()

        yield item








