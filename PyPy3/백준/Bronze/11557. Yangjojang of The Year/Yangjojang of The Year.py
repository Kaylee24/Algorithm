for _ in range(int(input())):
    dict = {}
    for _ in range(int(input())):
        S, L = map(str, input().split())
        dict[int(L)] = S
    temp = list(dict.keys())
    print(dict[max(temp)])