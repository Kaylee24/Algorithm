fibo = [0] * 41
fibo[1] = 1
for i in range(2, 41):
    fibo[i] = fibo[i-1] + fibo[i-2]   # 1이 호출되는 수는 피보나치 수열과 같고, 0은 2가 호출되는 것과 같다.

for _ in range(int(input())):
    N = int(input())
    if N == 0:
        print(1, 0)
    else:
        print(fibo[N-1], fibo[N])