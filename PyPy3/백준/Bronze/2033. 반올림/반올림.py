N = int(input())

p = 10
while N >= p:
    if N%p >= 5*(p//10):
        N = (N//p)*p + p
    else:
        N = (N//p)*p
    
    p *= 10

print(N)