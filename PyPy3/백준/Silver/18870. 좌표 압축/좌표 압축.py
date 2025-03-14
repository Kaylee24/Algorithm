import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
sorted_set = sorted(set(nums))
dictionary = {sorted_set[i]:i for i in range(len(sorted_set))}

for num in nums:
    print(dictionary[num], end=" ")