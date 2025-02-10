arr = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
first = input()
second = input()
third = input()

a = arr.index(first)
b = arr.index(second)
c = arr.index(third)

result = str(a) + str(b)
result = int(result) * (10 ** c)

print(result)