x = input()
a = x[-1]
L = list(x.split(a))

cnt = 0
for i in L:
    if i != '':
        cnt += 1

print(cnt)