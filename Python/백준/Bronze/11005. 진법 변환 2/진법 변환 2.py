N, B = map(int, input().split())
S = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while N:
    S += str(arr[N%B])
    N //= B
    
print(S[::-1])