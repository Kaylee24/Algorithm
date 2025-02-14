N = int(input())
cards = list(map(int, input().split()))
M = int(input())
quests = list(map(int, input().split()))

deck = {}
for quest in quests:
    deck[quest] = 0

for card in cards:
    if card in deck:
        deck[card] = 1

for d in deck:
    print(deck[d], end=' ')
