N = int(input())
scores = list(map(int, input().split()))

# 최고 점수 구하기
best = 0
for score in scores:
    if score >= best:
        best = score
    else:
        pass

# 새로운 평균 계산 및 출력하기
new_mean = sum(scores) / (best * len(scores)) * 100
print(new_mean)