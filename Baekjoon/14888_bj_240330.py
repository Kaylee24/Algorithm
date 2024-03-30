import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
n, *num = map(int, input().split())
cal = list(map(int, input().split()))   # +, -, *, % 의 개수
cal = ['+'] * cal[0] + ['-'] * cal[1] + ['*'] * cal[2] + ['%'] * cal[3]

# 순열, 경우의 수
cals = list(permutations(cal, N-1))

maximum = -1 * float('inf')
minimum = float('inf')
for c in cals:
    result = n
    for i in range(N-1):
        if c[i] == '+':
            result += num[i]
        elif c[i] == '-':
            result -= num[i]
        elif c[i] == '*':
            result *= num[i]
        elif c[i] == '%':
            if result >= 0:
                result //= num[i]
            elif result < 0:
                result *= -1
                result //= num[i]
                result *= -1
    if result > maximum:
        maximum = result
    if result < minimum:
        minimum = result

print(maximum)
print(minimum)