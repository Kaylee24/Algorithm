B, C = 3000, 3000
for _ in range(3):
    temp = int(input())
    if B > temp:
        B = temp
for _ in range(2):
    temp = int(input())
    if C > temp:
        C = temp

print(B + C - 50)