import math

N, S = map(int, input().split())        # 동생 N명, 수빈이의 현재 위치 S
arr = list(map(int, input().split()))   # 동생의 위치

arr2 = [abs(S - x) for x in arr]

G = arr2[0]
for y in arr2[1:]:
    G = math.gcd(y, G)

print(G)
