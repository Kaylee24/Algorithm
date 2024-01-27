year = int(input())

if year % 4 == 0 and year % 100 != 0:
    print(1)
elif year % 400 == 0:
    print(1)
else:
    print(0)



# 오답
    
year = int(input())

if (year % 4 == 0 & year % 100 != 0) or year % 400 == 0:
    print(1)
else:
    print(0)