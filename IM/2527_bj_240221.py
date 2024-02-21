for t in range(4):
    rec = list(map(int, input().split()))

    fir = rec[:4]
    sec = rec[4:]

    if (fir[2] < sec[0] or sec[2] < fir[0]) and (fir[3] < sec[1] or sec[3] < fir[1]):
        print('d')
    elif fir[2] == sec[0] or fir[0] == sec[2]:
        if fir[3] == sec[1] or fir[1] == sec[3]
            print('c')
        elif fir[3] < sec[1] or sec[3] < fir[1]:
            print('d')
        else:
            print('b')
    elif
