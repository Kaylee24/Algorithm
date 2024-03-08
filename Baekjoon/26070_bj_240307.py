gomgom = list(map(int, input().split()))   # 곰곰이의 수 : 치킨 A, 피자 B, 햄버거 C
ticket = list(map(int, input().split()))   # 식권 장수 : 치킨 X, 피자 Y, 햄버거 Z

baebulloeyo = 0
# 각각 A <= X, ...인지 확인하고 맞다면 A 만큼 카운팅 하고 X -= A
for i in range(3):
    if gomgom[i] <= ticket[i]:
        baebulloeyo += gomgom[i]
        ticket[i] -= gomgom[i]
        gomgom[i] = 0
    else:
        baebulloeyo += ticket[i]
        gomgom[i] -= ticket[i]
        ticket[i] = 0

# 이제 티켓을 순회하며 남은 티켓이 있다면, 한단계 교환해서 먹일 수 있는 곰곰이가 남아 있는지 확인하고 교환해서 먹인다.
for i in range(3):
    if ticket[i] >= 3 and gomgom[i - 2] > 0:
        if gomgom[i - 2] * 3 <= ticket[i]:
            baebulloeyo += gomgom[i - 2]
            ticket[i] -= gomgom[i - 2] * 3
            gomgom[i - 2] = 0
        else:
            baebulloeyo += ticket[i] // 3
            gomgom[i - 2] -= ticket[i] // 3
            ticket[i] -= ticket[i] // 3

for i in range(3):
    if ticket[i] >= 9 and gomgom[i - 1] > 0:
        if gomgom[i - 1] * 9 <= ticket[i]:
            baebulloeyo += gomgom[i - 1]
            ticket[i] -= gomgom[i - 1] * 9
            gomgom[i - 1] = 0
        else:
            baebulloeyo += ticket[i] // 9
            gomgom[i - 1] -= ticket[i] // 9
            ticket[i] -= ticket[i] // 9

print(baebulloeyo)