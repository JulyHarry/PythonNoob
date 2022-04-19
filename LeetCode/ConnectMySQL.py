# -*- coding: utf-8 -*- 
"""
Description:
Creator: HarryUp
Create time: 2021-11-16 20:31
"""

import pymysql

conn = pymysql.connect(host="localhost", user="hang", password="asdfasdf", database="employee", charset='utf8')
cursor = conn.cursor()
cursor.execute("select count(*) from employees")
data = cursor.fetchall()
for d in data:
    print(d)
dropTable = "drop table if exists park"
cursor.execute(dropTable)
createTable = "create table if not exists park (" \
              "id int not null auto_increment primary key comment 'index', " \
              "name varchar(20) not null comment 'name', " \
              "location varchar(60) comment 'address' " \
              ") ENGINE=InnoDB DEFAULT charset=utf8"
cursor.execute(createTable)
conn.close()
