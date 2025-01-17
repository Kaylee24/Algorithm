L, C = map(int, input().split())   # L개의 알파벳 소문자, C가지 암호로 사용했을 법한 문자의 종류
arr = list(map(str, input().split()))
arr.sort()

visited = [0] * C
result = []
password = []


def f(last, cnt):
    if cnt == L:
        vowels = 0
        for char in password:
            if char in ['a', 'e', 'i', 'o', 'u']:
                vowels += 1
        cons = L - vowels
        if vowels >= 1 and cons >= 2:
            result.append(''.join(password))

    for i in range(last, C):
        if visited[i] == 0:
            visited[i] = 1
            password.append(arr[i])
            f(i, cnt+1)
            password.pop()
            visited[i] = 0


f(0, 0)
print(*result, sep='\n')
