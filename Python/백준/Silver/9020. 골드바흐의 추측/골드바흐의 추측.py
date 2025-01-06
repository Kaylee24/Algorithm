def is_prime(N):
    if N == 1:
        return False
    for j in range(2, int(N**0.5)+1):
        if N % j == 0:
            return False
    return True

for _ in range(int(input())):
    num = int(input())

    small_gb = num//2
    while 1:
        if is_prime(small_gb) and is_prime(num-small_gb):
            print(small_gb, num-small_gb)
            break
        else:
            small_gb -= 1