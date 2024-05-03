'20:59 - 21:24, 18:07 - 18:37'

import sys
input = sys.stdin.readline

N = int(input())                             # 토핑의 종류의 수 N
A, B = map(int, input().split())             # 도우의 가격 A, 토핑의 가격 B
C = int(input())                             # 도우의 열량 C
topping = [int(input()) for _ in range(N)]   # 각 토핑의 열량







'''
[메모리 초과 - 1]

from itertools import combinations

N = int(input())                             # 토핑의 종류의 수 N
A, B = map(int, input().split())             # 도우의 가격 A, 토핑의 가격 B
C = int(input())                             # 도우의 열량 C
topping = [int(input()) for _ in range(N)]   # 각 토핑의 열량

pizza = 0
for i in range(1, N+1):
    toppings = list(combinations(topping, i))
    for top in toppings:
        test = (C + sum(top)) // (A + B * i)
        if pizza < test:
            pizza = test

print(pizza)
'''