N, M = map(int, input().split())   # 논문의 마지막 페이지 번호 N, 바닥에 흩어진 논문의 장수 M
pages = list(map(int, input().split()))

pages = list(set(pages))
pages.sort()

if list(range(1, N+1)) == pages:
    print(0)
else:
    htp = [x for x in list(range(1, N+1)) if x not in pages]
    L = len(htp)
    dp = [0] * (N+1)
    dp[htp[0]] = 7

    for i in range(1, L):
        dp[htp[i]] = min(dp[htp[i-1]] + 7, dp[htp[i-1]] + 2 * (htp[i] - htp[i-1]))

    print(dp[htp[-1]])