N, K = map(int, input().split())

data = {1:["1"], 2:["1+1", "2"], 3:["1+2", "1+1+1", "2+1", "3"]}
for i in range(4, 11):
    data[i] = []
    for j in data[i-1]:
        data[i].append(j+"+1")
    for j in data[i-2]:
        data[i].append(j+"+2")
    for j in data[i-3]:
        data[i].append(j+"+3")

print(sorted(data[N])[K-1] if len(data[N]) >= K else -1)