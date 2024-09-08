def lotto(k, j):
    if k == 6:
        print(*case)
    else:
        for i in range(j, N):
            case.append(nums[i])
            lotto(k+1, i+1)
            case.pop()


while 1:
    N, *nums = map(int, input().split())
    if not N:
        break

    case = []
    lotto(0, 0)
    print('')