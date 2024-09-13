N = int(input())
M = int(input())
K = int(input())

if M % (2**K):
    print('NO')
else:
    print('YES')