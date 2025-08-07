word = input()

result = 0
arr = ['a', 'e', 'i', 'o', 'u']
for a in arr:
    result += word.count(a)
    
print(result)