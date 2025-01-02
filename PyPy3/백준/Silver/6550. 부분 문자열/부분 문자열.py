while 1:
    try:
        s, t = map(str, input().split())

        i, j = 0, 0
        while 1:
            if t[j] == s[i]:
                i += 1
                if i == len(s):
                    print('Yes')
                    break
            j += 1
            if j == len(t):
                print('No')
                break

    except:
        break