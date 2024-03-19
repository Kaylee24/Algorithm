N = int(input())   # 단어의 개수 N
word = list(input() for _ in range(N))   # N 개의 단어들

word = list(set(word))
word.sort(key=lambda x: (len(x), x))

for i in range(len(word)):
    print(word[i])