for i in range(int(input())):
    if i == 0:
        order = list(input())
        L = len(order)
    else:
        file = list(input())
        for j in range(L):
            if order[j] != file[j]:
                order[j] = '?'

print(''.join(order))