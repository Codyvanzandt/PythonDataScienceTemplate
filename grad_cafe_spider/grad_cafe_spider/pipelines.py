# -*- coding: utf-8 -*-

import logging
from scrapy.exporters import CsvItemExporter

class LoggerPipeline(object):

    def __init__(self, settings):
        self.settings = settings

    def process_item(self, item, spider):
        logging.info( "Scraped {}".format( item ) )
        return item

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(settings)

class CsvPipeline(object):
    def __init__(self, settings):
        self.file = open("grad_cafe.csv", 'wb')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(settings)