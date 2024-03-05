# 도감에 수록되어 있는 포켓몬의 개수 N, 맞춰야 하는 문제의 개수 M
N, M = map(int, input().split())
pocketmons = ['0'] + [input() for _ in range(N)]   # 포켓몬 번호가 1부터 시작 -> 허수 추가로 인덱스 조정
problems = [input() for _ in range(M)]

for problem in problems:
    if problem.isalpha() == 1:   # 문제가 알파벳이면 -> 포켓몬 번호 출력
        print(f'{pocketmons.index(problem)}')
    elif problem.isnumeric() == 1:   # 문제가 숫자면 -> 포켓몬 이름 출력
        problem = int(problem)
        print(f'{pocketmons[problem]}')