N = int(input())

result = 0

for i in range(1, N):
    result += N*i + i
    
print(result)