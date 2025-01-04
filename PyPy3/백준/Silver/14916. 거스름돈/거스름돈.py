money = int(input())

five = money // 5
for i in range(five, -1, -1):
    if (money - i * 5) % 2 == 0:
        print(i + (money - i * 5) // 2)
        break
else:
    print(-1)