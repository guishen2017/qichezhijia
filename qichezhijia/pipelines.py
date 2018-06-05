# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
from qichezhijia.settings import IMAGES_STORE
import os

class QichezhijiaPipeline(object):
    def process_item(self, item, spider):
        return item

class QichezhijiaImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        request_objs = super(QichezhijiaImagePipeline,self).get_media_requests(item,info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    def file_path(self, request, response=None, info=None):
        path = super(QichezhijiaImagePipeline, self).file_path(request,response,info)
        category_one = request.item.get('category_one')
        category_two = request.item.get('category_two')
        category_three = request.item.get('category_three')
        category_four = request.item.get('category_four')
        dir_path = os.path.join(IMAGES_STORE, category_one, category_two,category_three,category_four)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        path = path.replace("full/","")
        image_path = os.path.join(dir_path,path)
        return image_path
