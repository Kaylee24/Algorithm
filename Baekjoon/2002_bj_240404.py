import sys
input = sys.stdin.readline

N = int(input())
IN = [input() for _ in range(N)]
OUT = [input() for _ in range(N)]

OUT_idx = [IN.index(OUT[i]) for i in range(N)]

cnt = 0
for i in range(N):
    for j in range(OUT_idx[i]):
        if j in OUT_idx[i+1:]:
            cnt += 1
            break

print(cnt)