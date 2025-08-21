N = int(input())
arr = list(map(int, input().split()))

total = 0
for a in arr:
    if a < N:
        total += a
    else:
        total += N
    
print(total)