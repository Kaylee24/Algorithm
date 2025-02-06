V = int(input())
votes = input()

A = 0
for vote in votes:
    if vote == 'A':
        A += 1
B = V - A

if A > B:
    print('A')
elif A < B:
    print('B')
else:
    print('Tie')