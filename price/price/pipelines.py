# -*- coding: utf-8 -*-

from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors

class MqlPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool("MySQLdb",
            db="xin_db",
            user="root",
            passwd="",
            cursorclass=MySQLdb.cursors.DictCursor,
            charset='utf8',
            use_unicode=True
            )

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item

    def _conditional_insert(self, tx, item):
        sql = "insert into xin_xincar values(%s,%s,%s,%s,%s,%s)"
        tx.execute(sql, ('', item["name"], item["city"], item["price"], item["licensed_time"], item["mile"]))
