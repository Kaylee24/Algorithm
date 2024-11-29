A, B = map(int, input().split())
C = int(input())

H, M = A + C//60, B + C%60
if M > 59:
    M -= 60
    H += 1
if H > 23:
    H -= 24

print(H, M)