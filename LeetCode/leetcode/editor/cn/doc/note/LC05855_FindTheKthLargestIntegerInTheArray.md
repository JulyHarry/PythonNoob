# python自带排序实现
* `sorted`    `reverse=True`为降序  可使用切片直接返回
```python
sorted(nums, key=int, reverse=True)
sorted(nums, key=int, reverse=True)[k]
```
* `.sort()` `reverse=True`为降序  不可使用切片
```python
nums.sort(key=int, reverse=True)
nums[k]
```
* 自定义key
```python
class MyCompare(str):
    def __lt__(self, other):
        if len(self) != len(other):
            return len(self) < len(other)
        else:
            for i in range(len(self)):
                if self[i] != other[i]:
                    return self[i] < other[i]

nums.sort(key=MyCompare, reverse=True)
sorted(nums, key=MyCompare, reverse=True)
```