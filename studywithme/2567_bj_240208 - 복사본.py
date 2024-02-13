N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]

sums = N * 4 * 10
papers_save = papers[:]
for n in range(N):
    papers = papers_save[:]
    x = papers[n][0]
    y = papers[n][1]
    papers.pop(n)
    left = []
    bottom = []
    for dx in range(10):
        left.append(y + dx)
        bottom.append(x + dx)
    for paper in papers:
        for i in range(10):
            if paper[0] <= x <= paper[0] + 9 or paper[0] <= x + 9 <= paper[0] + 9:
                if paper[1] <= left[i] <= paper[1] + 9:
                    sums -= 1
            if paper[1] <= y <= paper[1] + 9 or paper[1] <= y + 9 <= paper[1] + 9:
                if paper[0] <= bottom[i] <= paper[0] + 9:
                    sums -= 1

print(sums)