import sys
input = sys.stdin.readline

N = int(input())                          # 집의 수 N
house = list(map(int, input().split()))   # N채의 집의 위치

house.sort()

if N % 2 == 0:
    print(house[N//2 - 1])
else:
    print(house[(N-1) // 2])