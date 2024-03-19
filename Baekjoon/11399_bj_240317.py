import sys

N = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split()))

time.sort()
time_sum = 0
for i in range(N):
    time_sum += time[i] * (N-i)

print(time_sum)