N = int(input())
cars = list(map(int, input().split()))

cnt = 0
for car in cars:
    if car%10 == N:
        cnt += 1
        
print(cnt)