# 나무의 개수 N, 나무를 자를 때 드는 비용 C, 나무 한 단위의 가격 W,
# 이다솜이 가지고 있는 나무의 길이 정보 입력
N, C, W = map(int, input().split())
woods = [int(input()) for _ in range(N)]

# 모든 경우의 수에 대한 수익을 담을 빈 리스트 준비
moneys = []

# 나무의 길이 중 가장 큰 값보다 1 작은 수까지 순회하며 몫으로 삼는다.
for divisor in range(max(woods)):
    # 몫이 0인 경우
    if divisor == 0:
        # 나무의 길이별로 같은 길이를 가진 나무의 개수를 세어 리스트에 저장한다.
        wood_counts = []
        for wood in woods:
            wood_counts.append(woods.count(wood))
        # 가능한 수익의 경우를 모두 계산하여 moneys 리스트에 저장한다.
        for n in range(N):
            money = W * wood_counts[n] * woods[n]
            moneys.append(money)

    # 몫이 0이 아닌 경우
    else:
        # 나무를 커팅하고 난 나머지와 커팅 횟수 변수를 준비
        waste = 0
        count = 0
        # 나무들마다 순회하며 나머지와 커팅 횟수를 구한다.
        for wood in woods:
            waste += wood % divisor
            if wood % divisor == 0:
                count += wood // divisor - 1
            else:
                count += wood // divisor
        # 가능한 수익의 경우를 모두 계산하여 moneys 리스트에 저장한다.
        money = W * (sum(woods) - waste) - C * count
        moneys.append(money)

# 수익의 최댓값을 출력한다.
print(f'{max(moneys)}')