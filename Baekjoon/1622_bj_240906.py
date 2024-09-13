while 1:   # EOF 처리 (while, try-except)
    try:
        A = list(input())   # 다중교집합을 구해야 함
        B = list(input())   # set, intersect 가 아닌 list

        inter = []

        for i in B:
            if i in A:
                A.remove(i)   # 다중교집합을 위해서 한번 교집합의 원소로 확인된 원소는 제거
                inter.append(i)

        inter.sort()
        print(''.join(inter))
    except:
        break