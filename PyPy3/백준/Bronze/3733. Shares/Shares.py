try:
    while 1:
        N, S = map(int, input().split())
        print(int(S/(N+1)))
except:
    exit()