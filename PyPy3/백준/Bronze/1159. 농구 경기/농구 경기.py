N = int(input())
members = []

for _ in range(N):
    members.append(input())
    
members.sort()

check = ""
cnt = 0
result = ""
for member in members:
    if check != member[0]:
        check = member[0]
        cnt = 1
    else:
        cnt += 1
        if cnt == 5:
            result += check
            
if result == "":
    print("PREDAJA")
else:
    print(result)