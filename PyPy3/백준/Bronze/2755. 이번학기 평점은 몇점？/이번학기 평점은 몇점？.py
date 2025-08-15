N = int(input())
dict = {'A+':4.3, 'A0':4.0, 'A-':3.7, 'B+':3.3, 'B0':3.0, 'B-':2.7, 'C+':2.3, 'C0':2.0, 'C-':1.7, 'D+':1.3, 'D0':1.0, 'D-':0.7, 'F':0.0}

average = 0
total = 0

for _ in range(N):
    subject, time, score = input().split()
    time = int(time)
    average += time * dict[score]
    total += time

print(format(average/total + 0.001, ".2f"))