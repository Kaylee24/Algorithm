import sys
sys.stdin.readline
from collections import deque

for _ in range(int(input())):                             # 테스트 케이스
    N, M = map(int, input().split())                      # 문서의 개수 N, 궁금한 문서의 번호 M
    importance = deque(list(map(int, input().split())))   # N개 문서의 중요도
    document = deque(list(range(0, N)))

    # M번째 문서를 tracking
    # M번째 이전의 문서들이 작업 될 때마다
        # 출력되거나, 뒤로 빠지거나
        # => M번째의 위치는 하나씩 앞으로 빠짐
    # 본인이 작업 대상인 경우
        # 출력되었다면, 이때까지 출력된 문서들 + 1 을 print
        # 뒤로 빠진다면, 현재 남은 문서들의 개수를 확인해서 문서 위치 변수에 값 재할당
    # 본인이 출력될때까지 반복

    cnt = 0
    while importance:
        current = importance.popleft()

        if importance:
            if current < max(importance):
                importance.append(current)
                document.append(document.popleft())
            else:
                cnt += 1
                if document.popleft() == M:
                    print(cnt)
                    break
        else:
            cnt += 1
            if document.popleft() == M:
                print(cnt)
                break