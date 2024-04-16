import sys
input = sys.stdin.readline

N, K = map(int, input().split())                              # 물품의 수 N, 버틸 수 있는 무게 K
items = [list(map(int, input().split())) for _ in range(N)]   # 무게 W, 가치 V
dp = [0] * (K+1)

for weight, value in items:                          # 물건들을 차례대로 순회하면서
    for w in range(K, weight-1, -1):                 # 물건의 무게 이상, 최대 용량까지의 저장된 가치들과
        dp[w] = max(dp[w], dp[w - weight] + value)   # 이 물건을 담아서 해당 무게가 된 가치와 비교하여 값을 업데이트한다.

print(dp[K])