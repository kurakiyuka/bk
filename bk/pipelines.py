# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from bk.settings import mysql_host, mysql_port, mysql_db_name, mysql_table_name


class BkPipeline(object):
    """ def __init__(self):
        host = mysql_host
        port = mysql_port
        dbname = mysql_db_name
        tbname = mysql_table_name """

    def process_item(self, item, spider):
        conn = pymysql.connect(host = mysql_host, port = mysql_port,
                               user = 'root', passwd = '151393myz', db = mysql_db_name)
        cur = conn.cursor()
        cur.execute('insert into bigtable (name, shi, ting) values (%s, %s, %s)', [item['community_name'], item['shi_num'], item['ting_num']])
        cur.close()
        conn.close()
        
        return item
