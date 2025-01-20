N = int(input())
arr = [int(input()) for _ in range(N)]
if arr.count(1) > N//2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")