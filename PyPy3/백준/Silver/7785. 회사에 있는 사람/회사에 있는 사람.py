people = {}

for _ in range(int(input())):
    name, x = input().split()
    if x == 'enter':
        people[name] = 1
    else:
        people.pop(name)
        
remain = list(people.keys())
remain.sort(reverse=True)

for person in remain:
    print(person)
