import sys
import math
input = sys.stdin.readline

def round_half_up(n):
    return int(n + 0.5)

N = int(input().strip())

if N == 0:
    exit(print(0))
    
arr = [int(input().strip()) for _ in range(N)]  
arr.sort()

M = round_half_up(N * (0.15))

if N - 2*M <= 0:
    exit(print(0))
    
S = sum(arr[M:N-M])

print(round_half_up(S/(N-2*M)))