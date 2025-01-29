N, M = map(int, input().split())   # 바구니 N개, 공 넣는 횟수 M번
baskets = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    baskets[i-1:j] = [k] * (j-i+1)

print(*baskets)
