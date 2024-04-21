N, M = map(int, input().split())   # 체스판의 세로 길이 N, 가로 길이 M

# 오른쪽 끝에 도착하면 끝
if N == 1 or M == 1:
    print(1)
elif N == 2:
    if M < 3:
        print(1)
    elif M < 5:
        print(2)
    elif M < 7:
        print(3)
    else:
        print(4)
elif N >= 3:
    if M == 2:
        print(2)
    elif M == 3:
        print(3)
    elif M < 7:
        print(4)
    else:
        print(M-2)