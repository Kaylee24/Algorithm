S = list(input())
K = input()

N = []
for x in S:
    try:
        x = int(x)
    except:
        N.append(x)

note = ''.join(N)

if K in note:
    print(1)
else:
    print(0)