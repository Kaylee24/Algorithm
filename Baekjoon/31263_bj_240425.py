N = int(input())
S = input()

i, cnt = 0, 0
while i < N:
    if S[i] == '0':
        i -= 1
        continue
    if int(S[i:i+3]) <= 641:
        i += 3
    else:
        i += 2
    cnt += 1

print(cnt)