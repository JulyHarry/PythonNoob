import binascii

from pyDes import des, CBC, PAD_PKCS5


def des_encrypt(secret, s):
    iv = secret
    k = des(secret, CBC, iv, pad=None, padmode=PAD_PKCS5)
    en = k.encrypt(s, padmode=PAD_PKCS5)
    return binascii.b2a_hex(en)


def des_decrypt(secret, s):
    iv = secret
    k = des(secret, CBC, iv, pad=None, padmode=PAD_PKCS5)
    de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
    return de


key = "12345678"
a = des_encrypt(key, "foobar")
b = des_decrypt(key, a)
print(a)
print(b)
