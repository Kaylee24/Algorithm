A, B, V = map(int, input().split())

# 달팽이가 나무 막대를 모두 올라가는데 걸리는 시간 구하기

# 현재 높이, 오르는데 걸린 날짜
day = 0

# 오른 높이 < V 이면 밤새 미끄러지고, 다시 오르고, 하루가 지난다.
# 이튿날부터 오르는 높이 = A - B
# A + (A - B) * (day - 1) > V
if A == V:
    print(1)
elif 0 < (V - A) / (A - B) < 1:
    day = (V - A) // (A - B) + 2
    print(f'{day}')
elif (V - A) / (A - B) >= 1:
    if (V - A) % (A - B) == 0:
        day = (V - A) // (A - B) + 1
        print(f'{day}')
    elif (V - A) % (A - B) != 0:
        day = (V - A) // (A - B) + 2
        print(f'{day}')



# A == V 인 경우 누락

# A, B, V = map(int, input().split())

# # 달팽이가 나무 막대를 모두 올라가는데 걸리는 시간 구하기

# # 헌재 높이, 오르는데 걸린 날짜
# height = A

# # 오른 높이 < V 이면 밤새 미끄러지고, 다시 오르고, 하루가 지난다.
# # 이튿날부터 오르는 높이 = A - B
# # A + (A - B) * (day - 1) > V
# if (V - A) // (A - B) == 0:
#     day = (V - A) // (A - B) + 2
# # elif (V - A) // (A - B) == 1:
# #     day = (V - A) // (A - B) + 1
# else:
#     day = (V - A) // (A - B) + 1

# print(day)



# 시간 초과

# A, B, V = map(int, input().split())

# # 달팽이가 나무 막대를 모두 올라가는데 걸리는 시간 구하기

# # 헌재 높이, 오르는데 걸린 날짜
# height = A
# day = 1

# # 오른 높이 < V 이면 밤새 미끄러지고, 다시 오르고, 하루가 지난다.
# while height < V:
#     height += (A - B)
#     day += 1

# # 출력
# print(day)