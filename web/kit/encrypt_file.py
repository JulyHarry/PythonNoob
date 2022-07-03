import binascii
import configparser

from pyDes import CBC, des, PAD_PKCS5

"""
对配置文件加密
"""


def des_encrypt(secret_key: str, content: str) -> str:
    key = des(secret_key, CBC, secret_key, pad=None, padmode=PAD_PKCS5)
    en = key.encrypt(content, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en).decode('utf8')


def des_decrypt(secret_key: str, content: str) -> str:
    key = des(secret_key, CBC, secret_key, pad=None, padmode=PAD_PKCS5)
    de = key.decrypt(binascii.a2b_hex(content), padmode=PAD_PKCS5).decode('utf8')
    return de


def encrypt_file(filename: str, secret_key: str) -> None:
    path = '/'.join(filename.split('/')[:-1])
    name = filename.split('/')[-1]
    src_config = configparser.ConfigParser()
    dst_config = configparser.ConfigParser()
    src_config.read(filename, encoding='utf-8')
    for section in src_config.sections():
        if not dst_config.has_section(section):
            dst_config.add_section(section)
        for option in src_config.options(section):
            dst_config.set(section, option, des_encrypt(secret_key, src_config.get(section, option)))
    with open('{}/encrypt_{}'.format(path, name), 'w') as fp:
        dst_config.write(fp)


if __name__ == '__main__':
    with open('../config/secret_key', 'r') as f:
        secret_key = f.read()
    filename = "../config/config.ini"
    encrypt_file(filename, secret_key)
