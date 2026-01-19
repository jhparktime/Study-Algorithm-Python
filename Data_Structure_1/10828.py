import sys

N = sys.stdin.readline()

stack = []

for i in range(int(N)) :
    inst = sys.stdin.readline().rstrip()

    if 'push' in inst :
        inst, X = inst.split()
        stack.append(int(X))
    elif inst == 'pop' :
        if len(stack) == 0 :
            print(-1)
        else : 
            print(stack.pop())
    elif inst == 'size' :
        print(len(stack))
    elif inst == 'empty' :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    elif inst == 'top' :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])
    else :
        print('err')

