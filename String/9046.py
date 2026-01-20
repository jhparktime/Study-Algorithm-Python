import sys


N = int(sys.stdin.readline().rstrip())

for _ in range(N) :
    string = sys.stdin.readline().rstrip()
    check = {}

    for i in range(len(string)) :
        if string[i] == ' ':
            pass
        else : 
            if string[i] not in check.keys() :
                check[string[i]] = 1
            else : 
                check[string[i]] += 1

    idx, cnt, num = '', -1, 0

    for v, k  in check.items() : 
        if k > cnt : 
            idx = v
            cnt = k
            num = 1
        elif k == cnt :
            num += 1
    
    if num == 1 :
        print(idx)
    else :
        print('?')