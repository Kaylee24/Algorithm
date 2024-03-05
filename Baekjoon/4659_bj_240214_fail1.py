import re

inputs = True
result = 'acceptable'

'''
문자열이 아니라 리스트로 받아서 재진행해보기
'''

while inputs == True:
    password = input()
    if password == 'end':
        inputs = False
        break
    print(f'<{password}> is {result}.')

    # 1. 모음(a, e, i, o, u) 하나를 반드시 포함하여야 한다.
    for vowel in ['a', 'e', 'i', 'o', 'u']:
        if vowel not in password:
            result = 'not acceptable'
    print(f'<{password}> is {result}.')

    # 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안된다.
    jaeums = re.split('a|e|i|o|u', password)

    moeum_cnt = 0
    for j in range(1, len(jaeums) - 1):
        if (jaeums[j] == '' and jaeums[j + 1] == '') or (jaeums[j] == '' and jaeums[j - 1] == ''):
            moeum_cnt += 1
        else:
            moeum_cnt = 0
            if len(jaeums[j]) >= 3:
                result = 'not acceptable'

    if moeum_cnt >= 3:
        result = 'not acceptable'
    print(f'<{password}> is {result}.')

    # 3. 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo 는 허용한다.
    for i in range(len(password) - 1):
        if password[i] == password[i + 1] and password != 'e' and password != 'o':
            result = 'not acceptable'

    # 결과 출력
    print(f'<{password}> is {result}.')