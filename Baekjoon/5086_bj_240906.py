while 1:
    N, M = map(int, input().split())

    if N == 0 and M == 0:
        break
    elif M % N == 0:
        print('factor')
    elif N % M == 0:
        print('multiple')
    else:
        print('neither')