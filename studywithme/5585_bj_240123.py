# 타로가 지불할 금액, 1 <= N < 1000
N = int(input())

# 잔돈 종류
changes = [500, 100, 50, 10, 5, 1]

# 잔돈 개수, 잔액
cha_num = 0
balance = 1000 - N

for chn in changes:
    while balance >= chn:
        cha_num += 1
        balance -= chn
print(cha_num)



# Question. 12줄에서 if문 쓰면 안되는 이유