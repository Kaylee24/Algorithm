arr = list(input())

H = 10
for i in range(1, len(arr)):
    if arr[i-1] == arr[i]:
        H += 5
    else:
        H += 10

print(H)