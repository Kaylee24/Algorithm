from heapq import heappop, heappush, heapify

N, centi, T = map(int, input().split())          # 인구수 N, 키 H, 마법의 뿅망치 제한 횟수 T
giants = []
for _ in range(N):
    giant = int(input())
    if giant >= centi:
        giants.append(-giant)

T_org = T
heapify(giants)

while T:   # 마법의 뿅망치 사용 횟수를 다 소진할 때까지
    if not giants:               # 센티보다 키가 크거나 같은 거인이 없다면 못된짓 종료
        break
    temp = heappop(giants) / 2   # 가장 키 큰 거인을 반쪽 내버린다.
    T -= 1                       # 뿅망치 사용 횟수도 1 감소한다.
    if abs(temp) >= centi:       # 만약 반쪽 난 거인이 여전히 센티보다 키가 크거나 같다면, 다시 거인들의 모임에 넣어준다.
        heappush(giants, -int(abs(temp)))
    if temp >= -1:               # 만약 반쪽 난 키가 1 이하이면, 종료한다.
        break

if not giants:
    if centi == 1:
        print('NO')
        exit(print(1))
    print('YES')
    print(T_org - T)
else:
    print('NO')
    print(int(abs(min(giants))))