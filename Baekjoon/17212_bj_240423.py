N = int(input())

coin = [0, 1, 1, 2, 2, 1, 2, 1]
if N < 8:
    print(coin[N])
else:
    coin += [0] * (N-7)
    for i in range(8, N+1):
        coin[i] = min(coin[i-1]+coin[1], coin[i-2]+coin[2], coin[i-5]+coin[5], coin[i-7]+coin[7])
    print(coin[N])



'''
[오답 코드]
N = int(input())

cnt = 0
for coin in [7, 5, 2, 1]:
    cnt += N//coin
    N -= N//coin * coin
print(cnt)
'''



'''
[동현 코드]
coins = [1,2,5,7]

N = int(input())
DP = list(range(N+1+7))

for i in range(N+1):
    for coin in coins :
        DP[i+coin] = min(DP[i+coin], DP[i]+1)
        print(DP)
print(DP[N])
'''