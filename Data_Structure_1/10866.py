import sys
from collections import deque


N = int(sys.stdin.readline())

dq = deque([])

for _ in range(N) :
    inst = sys.stdin.readline().rstrip()

    if 'push' in inst :
        inst, X = inst.split()
        X = int(X)
        
        if inst == 'push_front' :
            dq.appendleft(X)
        elif inst == 'push_back' :
            dq.append(X)
        else :
            print('err')
    elif 'pop_front' == inst :
        if len(dq) == 0 :
            print(-1)
        else :
            print(dq.popleft())

    elif 'pop_back' == inst :
        if len(dq) == 0 :
            print(-1)
        else :
            print(dq.pop())

    elif 'size' == inst :
        print(len(dq))

    elif 'empty' == inst :
        if len(dq) == 0 :
            print(1)
        else :
            print(0)

    elif 'front' == inst :
        if len(dq) == 0 :
            print(-1)
        else :
            print(dq[0])

    elif 'back' == inst :
        if len(dq) == 0 :
            print(-1)
        else :
            print(dq[-1])

    else :
        print('err')
        


