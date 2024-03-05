N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 실패, 중복된 B의 원소값에 대한 오류 발생

# B2 = B[:]
# B.sort()
#
# A.sort(reverse=True)   # 내림차순 정렬
# A2 = [0] * N           # S가 최소가 될 수 있는 정렬한 A
# for n in range(N):
#     cnt = B.count(B[n])
#     first_index = B2.index(B[n])
#     for i in range(cnt):
#         A2[B2.index(B[n], first_index + i)] = A[n]
#
# S = 0
# for n in range(N):
#     S += A2[n] * B2[n]
#
# print(f'A = {A}')
# print(f'B = {B}')
# print(f'A2 = {A2}')
# print(f'B2 = {B2}')
#
# print(S)

'''
정답, 출제자의 의도는 X

A.sort()
B.sort(reverse=True)
S = 0
for n in range(N):
    S += A[n] * B[n]
print(S)
'''