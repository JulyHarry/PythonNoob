import binascii
import configparser

import pymysql
from pyDes import des, CBC, PAD_PKCS5
from pymysql import connect


def des_decrypt(s, secret):
    iv = secret
    k = des(secret, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5).decode('gbk')
    return de


def decrypt_mysql_info(secretfile: str, filename: str, section: str):
    with open(secretfile, 'r') as f:
        secret_key = f.read()
    cf = configparser.ConfigParser()
    cf.read(filename)
    dict = {'user': des_decrypt(cf.get(section, 'user'), secret_key),
            'password': des_decrypt(cf.get(section, 'password'), secret_key),
            'host': des_decrypt(cf.get(section, 'host'), secret_key),
            'port': des_decrypt(cf.get(section, 'port'), secret_key),
            'database': des_decrypt(cf.get(section, 'database'), secret_key)}
    return dict


# 创建一个函数用来获取数据库链接
def get_db_connection():
    item = decrypt_mysql_info(secretfile="config/secret_key", filename='config/encrypt_config.ini',
                              section='MYSQL-INFO')
    con = connect(user=item['user'], password=item['password'], host=item['host'], port=int(item['port']),
                  database=item['database'], cursorclass=pymysql.cursors.DictCursor)
    cursor = con.cursor()
    return con, cursor


# 根据post_id从数据库中获取post
def get_post(post_id):
    con, cursor = get_db_connection()
    cursor.execute('SELECT * FROM web.content WHERE contentid = %(id)s', {'id': post_id})
    post = cursor.fetchone()
    con.close()
    return post
