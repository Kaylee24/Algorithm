nums = []

for _ in range(int(input())):
    nums.append(int(input()))

L = max(nums)

prime_check = [0] * (L + 1)
for i in range(2, int(L ** 0.5) + 1):
    if not prime_check[i]:
        x = 2
        while i * x <= L:
            prime_check[i * x] = 1
            x += 1

# print('prime_check :', prime_check)

prime_idx = []
for i in range(2, L + 1):
    if not prime_check[i]:
        prime_idx.append(i)

# print('prime_idx :', prime_idx)

# 주어진 숫자들을 순회하면서
for num in nums:
    # 골드바흐 파티션 구하기
    small_gb = num // 2
    # print('small_gb :', small_gb)
    while 1:
        if (small_gb in prime_idx) & (num - small_gb in prime_idx):
            print(small_gb, num - small_gb)
            break
        else:
            small_gb -= 1