L, P = map(int, input().split())
news = list(map(int, input().split()))
X = L*P

for N in news:
    print(N - X, end=" ")