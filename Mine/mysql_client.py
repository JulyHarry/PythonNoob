# -*- coding: utf-8 -*-
import pymysql

mysql_host = '114.115.180.222'
mysql_port = 3306
mysql_user = 'root'
mysql_pwd = 'websqlroot'
mysql_database = 'translate'


def myslq_cursor():
    client = pymysql.connect(host=mysql_host, port=mysql_port, database=mysql_database, user=mysql_user,
                             password=mysql_pwd)
    client.autocommit(True)
    return client.cursor()
