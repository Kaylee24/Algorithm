import sys
input = sys.stdin.readline

N = int(input())                           # 에너지 드링크의 수 N
drinks = list(map(int, input().split()))   # 각 에너지 드링크의 양

drinks.sort()
total = sum(drinks)
total -= drinks[-1]
total /= 2
total += drinks[-1]

print(total)



'''
2, 3, 6, 9, 10
=> 9/2 + 10
=> 6/2 + 14.5
=> 3/2 + 17.5
=> 2/1 + 19
=> 20
'''