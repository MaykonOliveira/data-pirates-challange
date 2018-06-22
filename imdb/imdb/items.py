# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.loader.processors import MapCompose, TakeFirst

def customize_string_field(field):
    return re.sub("[\n\r]", '', field).strip()

def customize_position_field(field):
    return field.replace('.', '')

def customize_genre_field(field):
    return re.sub("[\n\r]", '', field).replace(',', '').strip()

class ImdbItem(scrapy.Item):
    position = scrapy.Field(input_processor=MapCompose(customize_position_field), output_processor=TakeFirst())
    name = scrapy.Field(input_processor=MapCompose(customize_string_field), output_processor=TakeFirst())
    genre = scrapy.Field(input_processor=MapCompose(customize_genre_field), output_processor=TakeFirst())
    rating = scrapy.Field(output_processor=TakeFirst())
