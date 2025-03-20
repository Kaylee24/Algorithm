for i in range(3):
    time = list(map(int, input().split()))
    work = []
    
    if time[5] < time[2]:
        time[4] -= 1
        time[5] += 60
        
    if time[4] < time[1]:
        time[3] -= 1
        time[4] += 60
        
    print(time[3]-time[0], time[4]-time[1], time[5]-time[2])