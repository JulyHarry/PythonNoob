def minElements(nums, limit: int, goal: int) -> int:
    sum = 0
    for num in nums:
        sum = sum + num
    ab = abs(goal - sum)
    return ab / limit + (0 if ab % limit == 0 else 1)


def minElements2(nums, limit: int, goal: int) -> int:
    t = abs(goal - sum(nums))  # ***sum***
    if t == 0:
        return 0
    return (t - 1) // limit + 1 # 向下取整

if __name__ == '__main__':
    nums = [1,2,3];
    print(minElements(nums, 1,7))

    s = "abc1233"
    l = list(s)
    print(l)
    print(type(l))

    ss = set(list(s))
    print(ss)
