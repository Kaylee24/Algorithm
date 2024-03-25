N = list(input())
len_N = len(N)
int_N = int(''.join(N))
M = int(input())

# 1. +, - 버튼으로만 이동하는 경우
candidate = [abs(int_N - 100)]

# 2-1. 고장난 버튼이 없어 숫자 버튼으로만 이동하는 경우
if M == 0:
    candidate.append(len_N)

# 2-2. 고장난 버튼이 있는 경우
else:
    broken = list(map(int, input().split()))
    N_broken = [0] * len_N

    for i in range(len_N):
        N[i] = int(N[i])
        if N[i] in broken:
            N_broken[i] = 1

    if N_broken.count(1) == 0:
        # 2-2-1. 고장난 버튼은 있지만, 눌러야 하는 버튼은 모두 정상이여서 숫자 버튼으로만 이동하는 경우
        candidate.append(len_N)

    # 2-2-2. 눌러야 하는 버튼 중 고장난 버튼이 있는 경우 : 숫자 버튼으로 가까운 채널로 이동 후, +, - 버튼으로 이동
    else:
        for k in [-1, 1]:    # 채널 N을 기준으로 숫자 버튼으로 누를 수 있는 가까운 채널 탐색
            near_N = int_N   # 아래, 위로 확인
            cnt = 0
            while 0 <= near_N + k and cnt <= min(candidate):
                near_N += k
                cnt += 1
                for j in range(len(str(near_N))):
                    if int(str(near_N)[j]) in broken:
                        break
                else:        # 모든 자리의 수를 누를 수 있는 번호 발견
                    candidate.append(len(str(near_N)) + abs(near_N - int_N))
                    break

print(min(candidate))


'''
N = list(input())
len_N = len(N)
int_N = int(''.join(N))
M = int(input())

candidate = [abs(int_N - 100)]

if M > 0:
    broken = list(map(int, input().split()))
    N_broken = [0] * len_N

    for i in range(len_N):
        N[i] = int(N[i])
        if N[i] in broken:
            N_broken[i] = 1

    if len(N_broken) == 0:
        candidate.append(len_N)
    else:
        for k in [-1, 1]:   # 더하거나 빼는 두가지 경우를 확인
            near_N = int_N
            while 0 <= near_N + k < 10**(len_N+1):
                near_N += k
                for j in range(len(str(near_N))):
                    if int(str(near_N)[j]) in broken:
                        break
                else:       # 모든 자리의 수를 누를 수 있는 번호 발견
                    candidate.append(len(str(near_N)) + abs(near_N - int_N))
                    break

else:
    candidate.append(len_N)

print(min(candidate))
'''

'''
                x = 0
                keep_going = True
                while keep_going == True:
                    x += 1                                             # 한칸씩 원래 번호와 멀어져가며
                    for k in [-1, 1]:                                  # 위아래로 번갈아가며 확인한다.
                        if N[i] + k*x not in broken:                   # 고장나지 않은 번호라면,
                            temp += (N[i] + k*x) * 10**(len_N -1 -i)   # 임시 번호에 저장한다.
                            keep_going = False
                            break
        candidate.append(len_N + abs(temp - int_N))
'''