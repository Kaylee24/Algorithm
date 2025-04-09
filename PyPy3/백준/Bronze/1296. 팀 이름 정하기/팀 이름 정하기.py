YD = list(input())
L = YD.count("L")
O = YD.count("O")
V = YD.count("V")
E = YD.count("E")

winner = ''
winP = -1
for _ in range(int(input())):
    t = input()
    team = list(t)
    tL = L + team.count("L")
    tO = O + team.count("O")
    tV = V + team.count("V")
    tE = E + team.count("E")
    p = ((tL+tO) * (tL+tV) * (tL+tE) * (tO+tV) * (tO+tE) * (tV+tE)) % 100
    if winP < p:
        winP = p
        winner = t
    elif winP == p:
        temp = [winner, t]
        temp.sort()
        winner = temp[0]

print(winner)