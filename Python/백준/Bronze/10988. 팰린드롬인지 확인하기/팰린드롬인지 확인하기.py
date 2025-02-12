word = input()
L = len(word)

for i in range(L//2):
    if word[i] != word[L-i-1]:
        exit(print(0))
print(1)