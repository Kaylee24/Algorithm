S = int(input())
switch = [0] + list(map(int, input().split()))
N = int(input())
students = [list(map(int, input().split())) for _ in range(N)]

for n in range(N):   # 학생 정보를 순회하며
    if students[n][0] == 1:   # 남학생인 경우
        for i in range(1, S + 1):         # 스위치 번호를 순회하며
            if i % students[n][1] == 0:   # 남학생이 받은 번호의 배수인 경우
                if switch[i] == 0:        # 스위치 꺼고 켜기
                    switch[i] = 1
                else:
                    switch[i] = 0

    else:                     # 여학생인 경우
        g = students[n][1]
        r = min(g - 1, S - g)     # 여학생이 받은 번호에서 대칭으로 갈 수 있는 최대 범위 구하기
        for i in range(r + 1):
            if switch[g - i] == switch[g + i]:   # 대칭이라면
                if switch[g - i] == 0:               # 스위치 꺼고 켜기
                    switch[g - i] = 1
                    switch[g + i] = 1
                else:
                    switch[g - i] = 0
                    switch[g + i] = 0
            else:                                # 대칭이 아니라면
                break                            # 반복문 종료

switch.pop(0)   # 인덱스 보정을 위해 넣어뒀던 가짜 원소 빼기

while switch:
    print(*switch[:20])
    switch = switch[20:]