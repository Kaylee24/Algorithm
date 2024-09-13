N = int(input())
nums = list(map(int, input().split()))

print('YES')
if nums[-1] == 0:
    print(0)
elif nums[-1] == 1:
    print(111)
else:
    print(nums[-1]*10 + nums[-1])