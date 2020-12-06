# -*- coding: utf-8 -*-
import sqlite3


class Sqlite3Aw(object):
    def __init__(self, db_name, table_name):
        self.table_name = table_name
        self.con = None
        self.cur = None
        self.connect(db_name)
        self.init_sqlite3()

    def init_sqlite3(self):
        """
        @summary: 初始化数据库
        """
        sql = "CREATE TABLE IF NOT EXISTS %s(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)" % self.table_name
        return self.cur.execute(sql)

    def connect(self, db_name):
        """
        @summary: 连接数据库
        """
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        return self.con

    def disconnect(self):
        """
        @summary: 断开连接
        """
        # 关闭游标
        self.cur.close()
        # 断开数据库连接
        return self.con.close()

    def add_data(self, data):
        """
        @summary: 添加数据
        """
        if type(data) == str:
            self.cur.execute('INSERT INTO %s VALUES (%s)' % (self.table_name, data))
        elif type(data) == tuple:
            self.cur.execute("INSERT INTO %s values(?,?,?)", (self.table_name, data))
        elif type(data) == list:
            self.cur.execute("INSERT INTO %s values(?,?,?)", (self.table_name, data))
        return self.con.commit()

    def modify_data(self, item, value):
        """
        @summary: 修改数据
        """
        self.cur.execute("UPDATE %s SET %s WHERE %s" % (self.table_name, item, value))
        return self.con.commit()

    def delete_data(self, value):
        self.cur.execute("DELETE FROM %s WHERE %s" % (self.table_name, value))
        return self.con.commit()

    def query_data(self):
        self.cur.execute("select * from %s" % self.table_name)
        return self.cur.fetchall()


if __name__ == '__main__':
    sql = Sqlite3Aw("DEMO.db", 'test')
    sql.add_data("1,'Desire',5")
    sql.disconnect()
