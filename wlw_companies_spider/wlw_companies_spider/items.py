# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags
from scrapy_djangoitem import DjangoItem
from companies_data_str.models import CompanyItemModel


class WlwCompaniesSpiderItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    django_model = CompanyItemModel()
    company_name_raw = scrapy.Field(
        input_processor= MapCompose(remove_tags, str.strip),
        output_processor = TakeFirst(),
    )
    company_name_clean = scrapy.Field(
        input_processor= MapCompose(remove_tags, str.strip),
        output_processor = TakeFirst(),
    )
    company_loc_raw = scrapy.Field(
        input_processor= MapCompose(remove_tags, str.strip),
        output_processor = TakeFirst(),
    )
    company_biz_clean = scrapy.Field(
        input_processor= MapCompose(remove_tags, str.strip),
        output_processor = TakeFirst(),
    )
    company_biz_phone = scrapy.Field(
        input_processor= MapCompose(remove_tags, str.strip),
        output_processor = TakeFirst(),
    )
    company_biz_email = scrapy.Field(
        input_processor= MapCompose(remove_tags, str.strip),
        output_processor = TakeFirst(),
    )
    company_street_name = scrapy.Field(
        input_processor= MapCompose(remove_tags, str.strip),
        output_processor = TakeFirst(),
    )
    company_postal_code = scrapy.Field(
        input_processor= MapCompose(remove_tags, str.strip),
        output_processor = TakeFirst(),
    )


    
