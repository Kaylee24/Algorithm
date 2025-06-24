import sys
input = sys.stdin.readline

st = []

for _ in range(int(input())):
    x = list(map(int, input().split()))
    if x[0] == 1:
        st.append(x[1])
    elif x[0] == 2:
        if st:
            print(st.pop(-1))
        else:
            print(-1)
    elif x[0] == 3:
        print(len(st))
    elif x[0] == 4:
        if st:
            print(0)
        else:
            print(1)
    else:
        if st:
            print(st[-1])
        else:
            print(-1)