# 고유번호 리스트로 받기
nums = list(map(int, input().split()))

# for문 활용해서 검증수 계산 및 출력하기
sum = 0
for num in nums:
    sum += num ** 2
print(sum % 10)