import hashlib

i = 0
s = "bigdata is a very good project"
while i < 20:
    a = hashlib.md5(s.encode('utf-8')).hexdigest()
    b = hashlib.md5(s.encode('utf-8')).digest()
    print(len(a), b)
    i += 1
