S = int(input())
switch = [0] + list(map(int, input().split()))
N = int(input())
student = [list(map(int, input().split())) for _ in range(N)]

def change_switch(idx):
    if switch[idx] == 0:
        switch[idx] = 1
    else:
        switch[idx] = 0

for s in student:
    if s[0] == 1:
        for i in range(1, S + 1):
            if i % s[1] == 0:
                change_switch(i)
    else:
        k = min(s[1] - 1, S - s[1])
        change_switch(s[1])
        for j in range(1, k + 1):
            if switch[s[1] - j] == switch[s[1] + j]:
                change_switch(s[1] - j)
                change_switch(s[1] + j)
            else:
                break

switch.pop(0)

while switch:
    print(*switch[:20])
    switch = switch[20:]