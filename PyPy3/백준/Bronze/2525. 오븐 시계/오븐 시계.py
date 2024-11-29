A, B = map(int, input().split())
C = int(input())

X, Y = C//60, C%60
H, M = A + X, B + Y
if M > 59:
    M -= 60
    H += 1
if H > 23:
    H -= 24

print(H, M)