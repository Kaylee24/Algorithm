def bfs(T, cnt):
    if cnt > C:
        if T == S:
            return print(1)
        else:
            return print(0)
    else:
        if T[-1] == 'A':
            T.pop()
            bfs(T, cnt + 1)
        else:
            T.pop()
            T.reverse()
            bfs(T, cnt + 1)

S = list(input())
T = list(input())
C = len(T) - len(S)

# T -> S
# 문자열의 뒤에 - 'A'
# 문자열의 뒤에 - 'B' 그리고 뒤집기

bfs(T, 1)

'''
처음에 풀고자 했던 방향 : 완전탐색

len(T) - len(S) 만큼 실행
bfs -> 완전탐색
결과물이 S와 같다면 1 출력 후 코드 종료
완전탐색이 끝났는데도 S와 같은 결과물이 없으면 0 출력 후 종료

def bfs(T, cnt):
    if cnt > C:
        if T == S:
            return print(1)
        else:
            return print(0)
    else:
        if T[-1] == 'A':
            T.pop()
            bfs(T, cnt + 1)
            T.append('A')
        else:
            T.pop()
            T.reverse()
            bfs(T, cnt + 1)
            T.reverse()
            T.append('B')
'''