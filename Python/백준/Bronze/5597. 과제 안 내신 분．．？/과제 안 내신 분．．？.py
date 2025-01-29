students = set(range(1, 31))
done = set([int(input()) for _ in range(28)])

print(*sorted(list(students - done)), sep='\n')