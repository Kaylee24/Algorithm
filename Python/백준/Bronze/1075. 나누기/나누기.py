N = input()
F = int(input())

num = int(N[:-2] + '00')
if num % F:
    num += F - (num % F)
num = str(num)

if len(num) < 2:
    num = '0' + num

print(num[-2:])
