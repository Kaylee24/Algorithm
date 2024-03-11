A, B = map(int, input().split())

if A == B:
    print(A, A)
    exit()
elif A > B:
    A, B = B, A

# 최대 공약수 greatest commom divisor
for i in range(A, 0, -1):
    if A % i == 0 and B % i == 0:
        gcd = i
        break

# 최소 공배수 least commom multiple
# lcd = A * B / gcd

print(i)
print(int(A*B/gcd))