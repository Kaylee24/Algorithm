# 소수인지 아닌지 확인하는 함수
def is_prime(N):
    for i in range(2, int(N**0.5)+1):
        if not N%i:
            return 0
    return 1

# 골드바흐 검증 함수
def goldbach():
    import sys
    input = sys.stdin.read
    nums = input().splitlines()
    nums = [int(num) for num in nums if num.strip().isdigit()]
    nums.pop()

    L = max(nums)
    primes = [0] * 2 + [1] * (L-1)
    for i in range(2, int(L**0.5)+1):
        if primes[i]:
            for j in range(i*2, L+1, i):
                primes[j] = False

    for num in nums:
        for gb in range(3, num//2+1, 2):
            if primes[gb] and primes[num-gb]:
                print(f'{num} = {gb} + {num-gb}')
                break
        else:
            print("Goldbach's conjecture is wrong.")

goldbach()