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
        resultList = []
        houseinfo = soup.findAll('div', class_='info')

        for house in houseinfo:
            bk_item = BkItem()
            list1 = house.find('a').contents[0].split()
            reslist = []
            bk_item['community_name'] = list1[0]
            reslist.append(list1[0])
            
            if len(list1[1]) > 3:
                reslist.append(list1[1][0])
                reslist.append(list1[1][2])
            else:
                continue
            reslist.append(list1[2][:-2])
            
            list2 = house.find('div', class_='houseInfo').contents[2].strip().split('|')
            reslist.append(list2[0].strip())
            reslist.append(list2[1].strip())
            
            list3 = house.find('div', class_='dealDate').contents[0].strip()
            reslist.append(list3)
            
            list41 = house.findAll('span', class_='number')[0].contents[0]
            reslist.append(list41)
            list42 = house.findAll('span', class_='number')[1].contents[0]
            reslist.append(list42)
            
            list5 = house.find('div', class_='positionInfo').contents[2].strip().split()
            reslist.append(list5[0])
            
            resultList.append(reslist)
        
        print(resultList)
