nums = []
while 1:
    N = int(input())
    if not N:
        break
    else:
        nums.append(N)

L = max(nums)

primes = [0] * 2 + [1] * (L-1)
for i in range(2, int(L**0.5)+1):
    if primes[i]:
        for j in range(i*2, L+1, i):
            primes[j] = 0

for num in nums:
    gb = 3
    while gb <= num//2:
        if primes[gb] & primes[num-gb]:
            print(f'{num} = {gb} + {num-gb}')
            break
        else:
            gb += 1
    else:
        print('Goldbach\'s conjecture is wrong.')