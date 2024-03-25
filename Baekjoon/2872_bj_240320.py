import sys
input = sys.stdin.readline

N = int(input())
book = [int(input()) for _ in range(N)]

std, check = 0, 0
for i in range(N-1, -1, -1):
    if book[i] > std:
        std = book[i]
        check = std - 1
    else:
        if book[i] == check:
            check -= 1

print(N - (std - check))
