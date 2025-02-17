X = int(input())

i = 1
while X > i:
    X -= i
    i += 1

S = i+1
if S%2:
    S -= X
    print("{}/{}".format(X, S))
else:
    S -= X
    print("{}/{}".format(S, X))