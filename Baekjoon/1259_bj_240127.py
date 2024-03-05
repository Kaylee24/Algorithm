# 팰린드롬수 판별 함수 정의
def pal():
    N = input()
    if N == N[::-1] and N != '0':
        print('yes')
        pal()
    elif N != N[::-1]:
        print('no')
        pal()
    else:
        pass

# 함수 호출
pal()


# 왜 안될까요? 왜 0 input하면 'yes' 출력될까요...?

# def pal():
#     N = input()
#     while N != '0':
#         if N == N[::-1]:
#             print('yes')
#         else:
#             print('no')
#         pal()

# pal()