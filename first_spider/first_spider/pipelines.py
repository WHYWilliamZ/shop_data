# # -*- coding: utf-8 -*-
#
# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import json
# from scrapy.exporters import JsonItemExporter
#
#
#
from scrapy.exporters import JsonItemExporter

class FirstSpiderPipeline(object):
    """
        功能：保存item数据
    """
    def open_spider(self,item,):
        # 打开文件
        self.filename = open("shop_data.json", "wb")
        self.writer=JsonItemExporter(self.filename,indent=2,ensure_ascii=False)
        self.writer.start_exporting()

    def process_item(self, item,spider):
        # 将获取到的每条item转换为json格式
        # text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        # self.filename.write(text)
        self.writer.export_item(item)
        return item

    def close_spider(self, item):
        # 关闭文件
        self.writer.finish_exporting()
        self.filename.close()

