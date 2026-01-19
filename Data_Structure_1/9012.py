import sys

N = int(sys.stdin.readline())


for _ in range(N) : # case 수
    str = sys.stdin.readline().rstrip()

    stack = []

    for i in range(len(str)) :
        if str[i] == '(' :
            stack.append('(')
        elif str[i] == ')' :
            if len(stack) == 0 :
                stack.append(1)
                break
            stack.pop()

    if len(stack) == 0 :
        print('YES')
    else :
        print('NO')





                