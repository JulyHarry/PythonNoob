m = int(input())
s = [set() for _ in range(m)]
for i in range(m):
    for j in input().split(','):
        s[i].add(int(j))
todo = []
for i in range(m):
    for j in range(i + 1, m):
        if len(s[i].intersection(s[j])) >= 2:
            todo.append((i, j))
for i, j in todo:
    s[i] = s[i].union(s[j])
    s[j] = set()
ans = []
for x in s:
    if len(x) > 0:
        ans.append(list(x))
print(ans)
