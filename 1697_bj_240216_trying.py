'''
수빈이는 동생과 숨바꼭질을 하고 있다.
수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다.
만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

수빈이와 동생의 위치가 주어졌을 때,
수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.
'''


# 수빈이 X-1, X+1, X*2 이동 가능
# 한번 이동할때마다 cnt

# 수빈이가 이동하는 함수

def bfs(start, finish):   # 시작정점 start, 도착정점 finish
    q = []                # 큐
    cnt = [[start, 0]]    # 지점별 시간 정보 담을 리스트
    q.append(start)       # 시작점 방문 표시

    while q:              # 큐가 비워질 때까지 (남은 정점이 있으면)
        t = q.pop(0)      # t에서 갈 수 있는 정점 i
        # t 에서 할일
        # t 범위 설정
        for i in [t-1, t+1, 2*t]:  # 갈 수 있는 3가지 지점을 순회
            for c in range(len(cnt)):   # 방문한 지점 정보 순회
                if t in cnt[c]:
                    index = c
                if i in cnt[c]:    # 방문한 정점이면
                    break          # cnt 에서 방문한 지점인지 더 확인할 필요 X
            else:             # 방문하지 않은 정점이면
                q.append(i)   # 인큐
                cnt.append([i, 1 + cnt[index][1]])

            if i == finish:
                return cnt[i][1]

# 수빈이가 있는 위치 N, 동생이 있는 위치 K
N, K = map(int, input().split())

print(bfs(N, K))