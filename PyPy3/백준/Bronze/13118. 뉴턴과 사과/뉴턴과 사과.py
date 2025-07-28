people = list(map(int, input().split()))
apple = list(map(int, input().split()))

none = False

for i in range(4):
    if people[i] == apple[0]:
        print(i+1)
        none = True

if not none:
    print(0)