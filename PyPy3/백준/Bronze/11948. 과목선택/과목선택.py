arr_A = [int(input()), int(input()), int(input()), int(input())]
arr_B = [int(input()), int(input())]

arr_A.sort()
arr_B.sort()

print(sum(arr_A[1:4]) + arr_B[1])