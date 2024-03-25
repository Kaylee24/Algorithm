import sys
input = sys.stdin.readline

K = int(input())

N = 0
while 2 ** N < K:
    N += 1
chocolate = 2**N

i = N
while K % (2**i) != 0:
    i -= 1

print(chocolate, N-i)


'''
'17% 시간초과'

T, cnt = 0, 0
while T != K:
    chocolate //= 2
    cnt += 1
    if (T + chocolate) <= K:
        T += chocolate
        
print(2**N, cnt)
'''