"""
满减券：满100减10，满200减20，满300减30，满400减40，以此类推不限制使用；

打折券：固定折扣92折，且打折之后向下取整，每次购物只能用1次；

无门槛券：一张券减5元，没有使用限制。


"""
import math


def coupon1(p, n):
    k = n
    while p >= 100 and n > 0:
        m = p // 100
        p -= m * 10
        n -= 1
    return p, k - n


def coupon2(p, n):
    if n >= 1:
        return int(p * 0.92), 1
    return p, 0


def coupon3(p, n):
    return max(p - n * 5, 0), n if p >= n * 5 else (p + n - 1) // n


c1, c2, c3 = map(int, input().split())
n = int(input())
for i in range(n):
    p = int(input())
    minp, minc = math.inf, math.inf
    price1, cnt1 = coupon1(p, c1)
    price2, cnt2 = coupon2(price1, c2)
    minp = min(minp, price2)
    minc = min(minc, cnt1 + cnt2)

    price1, cnt1 = coupon1(p, c1)
    price2, cnt2 = coupon3(price1, c3)
    if price2 < minp:
        minp = price2
        minc = cnt1 + cnt2
    elif price2 == minp:
        minc = min(minc, cnt1 + cnt2)

    price1, cnt1 = coupon2(p, c2)
    price2, cnt2 = coupon3(price1, c3)
    if price2 < minp:
        minp = price2
        minc = cnt1 + cnt2
    elif price2 == minp:
        minc = min(minc, cnt1 + cnt2)

    print(minp, minc)
