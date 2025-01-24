p, q = {}, {}

for i in range(3):
    x, y = map(int, input().split())
    if x in p:
        p[x] += 1
    else:
        p[x] = 1
    if y in q:
        q[y] += 1
    else:
        q[y] = 1

a, b = 0, 0
for num in p:
    if p[num] == 1:
        a = num
for num in q:
    if q[num] == 1:
        b = num

print(a, b)
    

