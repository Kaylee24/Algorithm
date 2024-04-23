P = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9] + [0] * 90
for i in range(11, 101):
    P[i] = P[i-2] + P[i-3]

for _ in range(int(input())):
    N = int(input())
    print(P[N])