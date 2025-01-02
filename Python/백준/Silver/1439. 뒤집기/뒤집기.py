x = input()

cnt = 0
for i in range(len(x)-1):
    if x[i] != x[i+1]:
        cnt += 1

print((cnt + 1) // 2)