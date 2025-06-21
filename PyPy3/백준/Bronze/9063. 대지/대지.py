x1, x2, y1, y2 = 10000, -10000, 10000, -10000

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x < x1:
        x1 = x
    if x > x2:
        x2 = x
    if y < y1:
        y1 = y
    if y > y2:
        y2 = y

print((x2-x1)*(y2-y1))