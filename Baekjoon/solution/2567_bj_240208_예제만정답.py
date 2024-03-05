N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]

sums = N * 4 * 11
papers_save = papers[:]
for n in range(N):
    papers = papers_save[:]
    x = papers[n][0]
    y = papers[n][1]
    papers.pop(n)
    left = []
    bottom = []
    for dx in range(11):
        left.append(y + dx)
        bottom.append(x + dx)
    for paper in papers:
        for i in range(11):
            if paper[0] <= x <= paper[0] + 10 or paper[0] <= x + 10 <= paper[0] + 10:
                if paper[1] <= left[i] <= paper[1] + 10:
                    sums -= 1
            if paper[1] <= y <= paper[1] + 10 or paper[1] <= y + 10 <= paper[1] + 10:
                if paper[0] <= bottom[i] <= paper[0] + 10:
                    sums -= 1

print(sums)