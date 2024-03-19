A, B = map(int, input().split())
cnt = 1

while B > A:
    cnt += 1
    if B % 10 == 1:
        B //= 10
    elif B % 2 == 0:
        B /= 2
    else:
        break

if B == A:
    print(cnt)
else:
    print(-1)