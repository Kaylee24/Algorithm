'백트래킹 안함'

def feed_gomgom(k):
    global baebulloeyo

    if gomgom[i - 3 + k] * (3**k) <= ticket[i]:
        baebulloeyo += gomgom[i - 3 + k]
        ticket[i] -= gomgom[i - 3 + k] * (3**k)
        gomgom[i - 3 + k] = 0
    else:
        baebulloeyo += ticket[i] // (3**k)
        gomgom[i - 3 + k] -= ticket[i] // (3**k)
        ticket[i] -= ticket[i] // (3**k)

gomgom = list(map(int, input().split()))   # 곰곰이의 수 : 치킨 A, 피자 B, 햄버거 C
ticket = list(map(int, input().split()))   # 식권 장수 : 치킨 X, 피자 Y, 햄버거 Z

baebulloeyo = 0
for k in range(3):
    for i in range(3):
        feed_gomgom(k)

print(baebulloeyo)