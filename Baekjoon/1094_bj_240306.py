X = int(input())
stick = [64]

while sum(stick) > X:
    stick[0] /= 2
    if sum(stick) < X:
        stick.insert(0, stick[0])

if sum(stick) == X:
    print(len(stick))