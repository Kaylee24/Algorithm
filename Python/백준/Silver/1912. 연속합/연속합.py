N = int(input())
arr = list(map(int, input().split()))

for i in range(N-2, -1, -1):   # 순회하며 연속된 수의 최대합 구하기
    arr[i] = max(arr[i], arr[i]+arr[i+1])

print(max(arr))
