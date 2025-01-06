import sys
input = sys.stdin.readline

nums = []
for _ in range(int(input())):
    nums.append(int(input()))

L = max(nums)

prime_check = [0] * 2 + [1] * (L-1)

for i in range(2, int(L**0.5)+1):
    if prime_check[i]:
        for j in range(2*i, L+1, i):
            prime_check[j] = 0

for num in nums:
    for i in range(num//2, 1, -1):
        if prime_check[i] and prime_check[num-i]:
            print(i, num-i)
            break