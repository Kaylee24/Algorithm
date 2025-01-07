import sys
sys.setrecursionlimit(1000000)

N = int(input())
result = 0


def make_three(x, sums):
    global result

    for i in range(3):
        if x == 0 and i == 0:
            continue
        if x == N:
            if sums % 3 == 0:
                result += 1
                return result
        else:
            make_three(x+1, sums+i)


make_three(0, 0)
print(result)