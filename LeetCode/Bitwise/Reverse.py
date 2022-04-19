def reverseBits(n: int) -> int:
    n = '{:032b}'.format(n)
    # print(n)
    return int(n[::-1], 2)


def reverseBits2(n: int) -> int:
    a = bin(n)[2:]
    # a = format(n, 'b')
    a = a.zfill(32)[::-1]
    return int(a, 2)

if __name__ == '__main__':
    # c = reverseBits2(7)
    # print(c)
    a = int("", 8)
    print(a)
