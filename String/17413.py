import sys
from collections import deque

string = sys.stdin.readline().rstrip()
result = string.replace('<', '!').replace('>', '!')

tmp = []
cnt = 0


for ch in result :
    if ch == '!' :
        # < 또는 > 를 만남
        if cnt == 0 : # < 만남
            print(''.join(reversed(tmp)), end = '')
            tmp = []
            print('<', end = '')
            cnt += 1

        elif cnt == 1 : # > 만남
            print('>', end = '')
            cnt = 0

    elif ch == ' ' :
        if cnt == 0 :
            print(''.join(reversed(tmp)), end = ' ')
            tmp = []
        else : 
            print(' ', end= '')


    else : 
        if cnt == 0 : # < > 내부가 아닌 경우
            tmp.append(ch)
        elif cnt == 1 : # < > 내부인 경우
            print(ch, end = '')

if len(tmp) != 0 :
    print(''.join(reversed(tmp)), end = '')



# <ab cd>ef gh<ij kl>