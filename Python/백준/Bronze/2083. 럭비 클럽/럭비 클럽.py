while 1:
    name, age, weight = map(str, input().split())
    
    if name == '#':
        break
    
    if int(age) > 17 or int(weight) >= 80:
        print(name, 'Senior')
    else:
        print(name, 'Junior')