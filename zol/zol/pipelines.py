# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline


class ZolPipeline:
    def process_item(self, item, spider):
        return item


class MyPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item["big_img"])

    def file_path(self, request, response=None, info=None, *, item=None):
        path = "img/"
        file_name = item["big_img"].split("/")[-1]
        return path + file_name
