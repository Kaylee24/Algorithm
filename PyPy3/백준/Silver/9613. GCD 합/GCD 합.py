import math

for _ in range(int(input())):
    nums = list(map(int, input().split()))
    N = nums.pop(0)

    result = 0
    for i in range(N-1):
        for j in range(i+1, N):
            result += math.gcd(nums[i], nums[j])

    print(result)