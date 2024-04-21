import sys
input = sys.stdin.readline

N = int(input())                          # 카드의 개수 N
cards = list(map(int, input().split()))   # 카드의 레벨

cards.sort()
gold = sum(cards) + cards[-1] * (N-2)

print(gold)