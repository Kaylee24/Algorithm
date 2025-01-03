document = input()
word = input()

d = 0
l = len(word)
cnt = 0
while d < len(document):
    if document[d:d+l] == word:
        cnt += 1
        d += l
    else:
        d += 1

print(cnt)
