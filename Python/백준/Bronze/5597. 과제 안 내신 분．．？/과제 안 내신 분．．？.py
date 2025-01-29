students = set(range(1, 31))
done = [int(input()) for _ in range(28)]
done = set(done)
bad = sorted(list(students - done))

print(bad[0])
print(bad[1])
