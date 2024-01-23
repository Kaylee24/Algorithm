# N, M : 10,000 이하의 자연수
N, M = map(int, input().split())

for i in range(2, N + 1):
    if N % i == 0:
        if M % i == 0:
            common = i
    i += 1
print(common)
commonm = int(N * M / common)
print(commonm)


# for i in range(2, N + 1):
#     if N % i == 0:
#         if M % i == 0:
#             commond = i
#     i += 1
# print(commond)
# commonm = int(N * M / commond)
# print(commonm)



# for문
# for i in range(N + 1):
#     i = 2
#     while N >= i:
#         if N % i == 0:
#             divisor = i
#             i += 1
#             if M % divisor == 0:
#                 commond = int(divisor)
#             else:
#                 pass
#         else:
#             i += 1
# print(commond)
# commonm = int(N * M / commond)
# print(commonm)




# # greatest common divisor
# def get_common(num1, num2):
#     i = 2
#     while num1 >= i:
#         if num1 % i == 0:
#             divisor = i
#             i += 1
#             if num2 % divisor == 0:
#                 commond = int(divisor)
#             else:
#                 pass
#         else:
#             i += 1
#     print(commond)
#     commonm = int(num1 * num2 / commond)
#     print(commonm)

# get_common(N, M)



# # greatest common divisor
# def get_gcd(N, M):
#     i = 2
#     while N >= i:
#         if N % i == 0:
#             divisor = i
#             i += 1
#             if M % divisor == 0:
#                 common = divisor
#             else:
#                 pass
#         else:
#             i += 1
#     return int(common)

# gcd = get_gcd(N, M)
# print(gcd)

# # least common mutiple
# def get_lcm(N, M):
#     return int(N * M / gcd)

# print(get_lcm(N, M))




# 다음에 이렇게도 풀어볼까

# def get_divisor(num):
#     while num > 1:
#         if num % i == 0:
#             divisor.append(i)
#         else:
#             i += 1
#     return divisor

# common = []
# def get_gcd(N, M):
#     for div_n in get_divisor(N):
#         if div_n in get_divisor(M):
#             common.append(div_n)
    