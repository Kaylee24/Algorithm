N, Q = map(int, input().split())
note = []
for i in range(N):
    for k in range(int(input())):
        note.append(i+1)

for i in range(Q):
    print(note[int(input())])