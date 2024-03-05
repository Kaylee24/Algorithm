a, b = input().split()
# 100 <= a, b < 1000

sangsu_a = int(a[::-1])
sangsu_b = int(b[::-1])

if sangsu_a > sangsu_b:
    print(sangsu_a)
elif sangsu_a < sangsu_b:
    print(sangsu_b)