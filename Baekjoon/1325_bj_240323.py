import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
computer = [list(map(int, input().split())) for _ in range(M)]   # A가 B를 신뢰한다.

trusted = [[] for _ in range(N+1)]
for i in range(M):
    trusted[computer[i][1]].append(computer[i][0])

can_hack = [0] * (N+1)
can_hack[0] = -1
for i in range(1, N+1):
    if trusted[i] != []:   # i번 컴퓨터를 신뢰하는 컴퓨터가 있다면,
        queue = deque([i])
        hacked = [0] * (N+1)
        hacked[i] = 1
        weak = 1
        while queue:
            t = queue.popleft()
            for target in trusted[t]:
                if hacked[target] == 0:
                    hacked[target] = 1
                    weak += 1
                    queue.append(target)
        can_hack[i] = weak

chm = max(can_hack)
while chm in can_hack:
    chi = can_hack.index(chm)
    print(chi, end=' ')
    can_hack[chi] = -1