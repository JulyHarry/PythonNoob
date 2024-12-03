import sys

for line in sys.stdin:
    st = line.strip()
    a = list(st)


    def getMin(x):
        s, k = x[0], 0
        for i, t in enumerate(x):
            if t <= s:
                s = t
                k = i
        return s, k


    def getMin2(x, y):
        s, k = x[0], 0
        for i, t in enumerate(x):
            if y <= t <= s:
                s = t
                k = i
        return s, k


    def getStart(x, s):
        i = 0
        while x[i] <= s:
            i += 1
        return i


    s, k = getMin(st)
    i = getStart(st, s)
    if i <= k:
        a[i], a[k] = a[k], a[i]
    print(''.join(a))
