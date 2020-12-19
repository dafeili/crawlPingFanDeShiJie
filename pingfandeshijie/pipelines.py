# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter


#class PingfandeshijiePipeline:
    #def process_item(self, item, spider):
        #return item



import json
import codecs
# 以txt的形式存储，其实也就是一个存储方式
class PingfandeshijiePipeline(object):
    def process_item(self, item, spider):
        # 根据书名来创建文件
        #item.get('title')  # 就可以获取到书名
        #self.file = codecs.open(item.get('title') + '.txt', 'w', encoding='utf-8')
        self.file = codecs.open('平凡的世界_路遥' + '.txt', 'a+', encoding='utf-8')
        #self.file.write("<br><br>")
        self.file.write("\n" + "********" + item.get("title") + "********" + "\n\n")
        self.file.write(item.get("paragraph") + "\n")
        return item

    def spider_closed(self, spider):
        self.file.close()