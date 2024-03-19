problem = ['0'] + list(input())
re_problem = []

for i in range(len(problem)):
    try:
        problem[i] = int(problem[i])
    except:
        pass

temp = 0
for i in range(len(problem)):
    if type(problem[i]) == int:
        temp = temp * 10 + problem[i]
    else:
        re_problem.append(temp)
        temp = 0
        re_problem.append(problem[i])
re_problem.append(temp)

part = 0
temp = []
for k in range(len(re_problem)-1, -1, -1):
    if type(re_problem[k]) == int:
        part += re_problem[k]
    elif re_problem[k] == '-' and part > 0:
        temp.append(-part)
        part = 0
temp.append(part)

print(sum(temp))
