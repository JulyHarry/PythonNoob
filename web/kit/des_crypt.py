import binascii

from pyDes import des, CBC, PAD_PKCS5


def des_encrypt(secret, s):
    iv = secret
    k = des(secret, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en).decode('utf-8')


def des_decrypt(secret, s):
    iv = secret
    k = des(secret, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de.decode('utf-8')
