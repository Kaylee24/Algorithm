for _ in range(int(input())):
    arr = list(map(str, input().split()))
    N = float(arr.pop(0))
    for x in arr:
        if x == '@':
            N *= 3
        elif x == '%':
            N += 5
        elif x == '#':
            N -= 7
    print(format(N, ".2f"))
