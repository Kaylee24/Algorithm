import re

result = 'acceptable'

'''
문자열이 아니라 리스트로 받아서 재진행해보기
'''

next = True
while next == True:
    password_str = input()
    password = list(password_str)
    if password == ['e', 'n', 'd']:
        next = False
    else:
        # 1. 모음(a, e, i, o, u) 하나를 반드시 포함하여야 한다.
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_check = 0
        for vowel in vowels:
            if vowel not in password:
                result = 'not acceptable'
            else:
                # 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안된다.
                mo_cnt = 0
                ja_cnt = 0
                for j in range(1, len(password) - 1):
                    if password[j] in vowels:
                        mo_cnt += 1
                        ja_cnt = 0
                    else:
                        mo_cnt = 0
                        ja_cnt += 1

                if mo_cnt >= 3 or ja_cnt >= 3:
                    result = 'not acceptable'
                else:
                    # 3. 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo 는 허용한다.
                    if len(password) >= 2:
                        for i in range(len(password) - 1):
                            if password[i] == password[i + 1] and password != 'e' and password != 'o':
                                result = 'not acceptable'

            print(f'<{password_str}> is {result}.')


    # 결과 출력
    print(f'<{password_str}> is {result}.')