import sys
input = sys.stdin.readline

N = int(input())
num = {}
for i in range(N):
    number = int(input())
    num[number] = num.get(number, 0) + 1
    # if number in num:
    #     num[number] += 1
    # else:
    #     num[number] = 1

for i in sorted(num.keys()):
    for _ in range(num[i]):
        print(i)