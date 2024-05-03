'17:22 - 17:52'

'''
그리고 한수는 집에 돌아가는 방법이 다양하다.
단, 한수는 똑똑하여 한번 지나친 곳을 다시 방문하지는 않는다.

위 예제는 한수가 집에 돌아갈 수 있는 모든 경우를 나타낸 것이다.
T로 표시된 부분은 가지 못하는 부분이다.
문제는 R x C 맵에 못가는 부분이 주어지고 거리 K가 주어지면 한수가 집까지 도착하는 경우 중 거리가 K인 가짓수를 구하는 것이다.

첫 줄에 거리가 K인 가짓수를 출력한다.
'''

from collections import deque

R, C, K = map(int, input().split())
data = [list(input()) for _ in range(R)]

di = [[1, 0], [-1, 0], [0, 1], [0, -1]]

queue = deque([R-1, 0])
while queue:
    i, j = queue.popleft()
    for k in range(4):
        p, q = i + di[k][0], j + di[k][1]
        if 0 <= p <= R-1 and 0 <= q <= C-1:


