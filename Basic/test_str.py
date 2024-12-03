a = 'python&'
b = 'python&'
print(a is b)

a = 'py thon adf_ 123'
c = 'py thon'
d = ' adf_ 123'
print(a is (c + d))
print(a == (c + d))

a = '11'
b = '11'
print(a is b)

a = ''
b = ''
print(a is b)

a = ' '
b = ' '
print(a is b)

m = '1'
n = m * 1
print(m is n)

m = 'python'
n = m * 3
print(m is n)

m = 'aa'
n = m * 10
print(m is n)

m = 'aa'
n = m * 15
print(m is n)
