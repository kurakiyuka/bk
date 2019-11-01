# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from bk.items import BkItem


class BkspiderSpider(scrapy.Spider):
    name = 'bkSpider'
    allowed_domains = ['ke.com']
    start_urls = ['https://sh.ke.com/chengjiao/beicai/']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        houseinfo = soup.findAll('div', class_='info')

        for house in houseinfo:
            bk_item = BkItem()
            list1 = house.find('a').contents[0].split()
            bk_item['community_name'] = list1[0]
            
            # 这段文本有可能是车位，那就忽略掉此节点
            if len(list1[1]) > 3:
                bk_item['shi_num'] = list1[1][0]
                bk_item['ting_num'] = list1[1][2]
            else:
                continue

            bk_item['area'] = list1[2][:-2]
            
            list2 = house.find('div', class_='houseInfo').contents[2].strip().split('|')
            bk_item['direction'] = list2[0].strip()
            bk_item['decoration'] = list2[1].strip()
            
            bk_item['deal_date'] = house.find('div', class_='dealDate').contents[0].strip()          
            bk_item['total_price'] = house.findAll('span', class_='number')[0].contents[0]
            bk_item['unit_price'] = house.findAll('span', class_='number')[1].contents[0]
            
            list3 = house.find('div', class_='positionInfo').contents[2].strip().split()
            bk_item['layer'] = list3[0]

            yield bk_item

        """ next_link_node = soup.find('div', class_ = 'page-box house-lst-page-box')
        page_data = next_link_node.attrs['page-data'].split(',')[0].split(':')[1]
        print(page_data)
        page_url = next_link_node.attrs['page-url'].split('{')[0]
        print(page_url) """
        
        """ for i in range(2, 5):
            yield scrapy.Request("https://sh.ke.com/chengjiao/beicai/pg" + str(i), callback = self.parse) """
