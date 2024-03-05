N = int(input())

for n in range(1, N + 1):
    print(' ' * (N - n) + '*' * n)

# stars = [' '] * N
# for n in range(1, N + 1):
#     stars = stars[:N - n] + ['*'] * n
#     print(*stars)