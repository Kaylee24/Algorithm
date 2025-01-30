phone = input()
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = [len(phone)]

for p in phone:
    i = alphabet.index(p)
    if i < 15:
        number.append(i//3 + 2)
    elif 15 <= i < 19:
        number.append(7)
    elif 19 <= i < 22:
        number.append(8)
    elif 22 <= i < 26:
        number.append(9)

print(sum(number))