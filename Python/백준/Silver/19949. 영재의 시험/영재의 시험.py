def test(x, cnt):
    global right

    if x == 10:      # 문제를 10개 다 풀었다면
        right += 1   # 5점 이상인 경우의 수에 카운팅
        return

    # 풀어야 할 문제가 아직 남았다면
    for i in range(1, 6):   # 5지 선다로 찍기
        if x >= 2 and yj_answer[-2] == yj_answer[-1] == i:
            continue

        yj_answer.append(i)   # 문제를 찍는다

        if answer[x] == i:   # 정답을 맞췄다면
            test(x+1, cnt+1)       # 다음 번호를 찍으러 간다
        else:                  # 정답을 틀렸다면
            if (10 - (x+1)) + cnt < 5:    # 남은 문제를 다 맞춰도 5점 이상이 될 수 없는 경우
                yj_answer.pop()           # 마지막 푼 문제 되돌리고
                continue                  # 넘어가기

            test(x+1, cnt)         # 다음 번호를 찍으러 간다
            
        yj_answer.pop()        # 마지막 문제 되돌리기, for 문 돌아가도록


answer = list(map(int, input().split()))   # 시험의 정답 10개
yj_answer = []   # 영재가 작성하는 답변
right = 0        # 5점 이상인 경우의 수
test(0, 0)       # 시험 한문제씩 찍는 함수

print(right)
