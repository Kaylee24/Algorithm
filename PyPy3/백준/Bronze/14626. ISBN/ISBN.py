ISBN = input()

check = int(ISBN[-1])

part_sum, unknown_weight = 0, 0

for N, W in zip(ISBN[:-1], [1, 3]*6):
    if N == "*":
        unknown_weight = W
        continue
    part_sum += int(N) * W

for X in range(10):
    rest = (part_sum + (X * unknown_weight) + check) % 10

    if rest == 0:
        exit(print(X))