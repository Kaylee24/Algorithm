N, K = map(int, input().split())          # 동전 N 종류, 동전의 가치의 합 K
coin = [int(input()) for _ in range(N)]   # 동전 정보
coin.sort(reverse=True)                   # 동전 내림차순으로 정렬
cnt = 0                                   # 사용한 동전의 수를 담을 변수 설정

for i in range(N):   # 동전 정보를 순회하면서
    if K == 0:       # 채워야 하는 남은 가치가 0이 되면
        print(cnt)   # 이때까지 사용한 동전의 수를 출력하고
        exit()       # 코드 중단
    elif K > 0:
        while K >= coin[i]:
            K -= coin[i]
            cnt += 1
        if K == 0:
            print(cnt)
            exit()