N = int(input())
original = N

cycle = 0
while 1:
    if cycle and N == original:
        exit(print(cycle))
    
    N = (N%10)*10 + (N//10 + N%10)%10
    cycle += 1
