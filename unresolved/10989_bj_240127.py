N = int(input())

# 입력받은 N개의 수를 리스트에 담기
my_list = []
for n in range(N):
    i = int(input())
    my_list.append(i)

# my_list 정렬하기
my_list.sort()

# my_list 한 줄에 하나씩 출력하기
for n in range(N):
    print(my_list[n])



# 메모리 초과

# N = int(input())

# # 입력받은 N개의 수를 리스트에 담기
# my_list = []
# for n in range(N):
#     i = int(input())
#     my_list.append(i)

# # my_list 정렬하기
# my_list.sort()

# # my_list 한 줄에 하나씩 출력하기
# for n in range(N):
#     print(my_list[n])



# 왜 안돼?

# my_list 한 줄에 하나씩 출력하기
# for n in range(N, 0, -1):
    # print(my_list.pop())