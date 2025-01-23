import statistics

sums = 0
for _ in range(5):
    score = int(input())
    if score >= 40:
        sums += score
    else:
        sums += 40
    
print(sums//5)