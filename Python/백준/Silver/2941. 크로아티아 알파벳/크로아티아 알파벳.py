word = input()
cr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for c in cr:
    word = word.replace(c, '*')

print(len(word))