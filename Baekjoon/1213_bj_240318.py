name = list(input())
name.sort()
name_kind = list(set(name))
name_kind.sort()
name_kind_num = [0] * len(name_kind)
center = -1

# 원소별 개수 체크
# 만약 전체 원소수가 홀수라면,
# 최대 1종류의 원소가 홀수개 있을 수 있다.
# 전체 원소수가 짝수라면,
# 모든 원소의 동일한 수도 짝수여야 한다.
M = len(name_kind)
for i in range(M):
    name_kind_num[i] = name.count(name_kind[i])
    if name_kind_num[i] % 2 == 1 and center == -1:
        center = i
    elif name_kind_num[i] % 2 == 1 and center != -1:
        print("I'm Sorry Hansoo")
        exit()

result = ''
if center != -1:
    result = name_kind[center]
    name_kind_num[center] -= 1

for i in range(M-1, -1, -1):
    result = name_kind[i] * int(name_kind_num[i] / 2) + result + name_kind[i] * int(name_kind_num[i] / 2)

print(result)
