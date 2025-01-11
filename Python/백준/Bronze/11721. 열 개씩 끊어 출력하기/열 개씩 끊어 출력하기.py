word = input()
N = len(word)
i = 0
while i < N:
    if i + 10 > N:
        print(word[i:])
    else:
        print(word[i:i+10])
    i += 10
