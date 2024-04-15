S = list(map(str, input().split('>')))
organized = []
result = ''

for i in range(len(S)):
    if '<' in S[i]:
        S[i] += '>'

for i in range(len(S)):
    if S[i] != '':
        if S[i][-1] == '>':
            temp = list(map(str, S[i].split('<')))
            for j in range(len(temp)):
                if temp[j] != '':
                    if temp[j][-1] == '>':
                        organized.append('<' + temp[j])
                    else:
                        organized.append(temp[j])
        else:
            organized.append(S[i])

for word in organized:
    if word[0] == '<':
        result += word
    else:
        temp = list(map(str, word.split()))
        L = len(temp)
        for i in range(L):
            temp_word = list(temp[i])
            result += ''.join(temp_word[::-1])
            if i != L-1:
                result += ' '

print(result)
