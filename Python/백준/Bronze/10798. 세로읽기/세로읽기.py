words = [list(input()) for _ in range(5)]
answer = []

L = 0
for word in words:
    if len(word) > L:
        L = len(word)

for i in range(L):
    for j in range(5):
        if i < len(words[j]):
            answer.append(words[j][i])

print(''.join(answer))