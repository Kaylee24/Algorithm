# 재활 코딩 중 | while 로 시도하다가 지난 풀이 확인 후 복습

def f(k, result):   # 재귀 함수 정의 / k는 조합 몇개째 원소 넣었는지 체크하는 변수, result 는 현재 조합의 리스트
    if k == M:           # 조합에 M개의 원소를 넣었다면
        print(*result)       # 조합 원소 출력
    else:                # 조합에 아직 M개의 원소를 넣지 않았다면
        for i in range(N):   # N개의 수에 대해 index를 순회하면서
            if visited[i] == 0:   # 현재 idx의 수가 아직 조합에 없다면
                visited[i] = 1           # 조합에 넣었다고 표시
                result.append(nums[i])   # 조합에 해당 숫자 넣어주기
                f(k+1, result)           # 조합 원소 수 하나 더 늘었음을 반영하고, 현재 조합 리스트를 들고 재귀 호출
                visited[i] = 0           # 조합에 넣었다는 표시 리셋
                result.pop()             # 조합에 넣었던 숫자 다시 빼기


N, M = map(int, input().split())
nums = list(range(1, N+1))

visited = [0] * N   # 방문 기록
result = []         # 조합 저장할 리스트
f(0, result)        # 재귀 함수 호출