# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json


class ImdbPipeline(object):

    def __init__(self):
        self.file_name_base = 'data'
        self.dictionary = {}

    def process_item(self, item, spider):
        if item['genre'] in self.dictionary:
            self.dictionary[item['genre']].append(item)
        else:
            self.dictionary[item['genre']] = [item]
        return item

    def close_spider(self, spider):
        for key in self.dictionary:
            file = codecs.open('{}_{}.json'.format(self.file_name_base, key.replace(' ', '_')), 'w', encoding='utf-8')
            for item in self.dictionary[key]:
                line = json.dumps(dict(item), ensure_ascii=False) + "\n"
                file.write(line)
            file.close()




