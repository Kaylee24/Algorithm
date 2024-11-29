A, B = map(int, input().split())
C = int(input())

time = A * 60 + B + C

print((time//60)%24, time%60)