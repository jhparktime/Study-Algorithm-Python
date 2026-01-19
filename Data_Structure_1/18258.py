from collections import deque
import sys

def push(item) : 
    queue.append(item)

def pop() :
    if size() == 0 :
        return -1
    else : 
        out = queue.popleft()
        return out

def size() :
    return len(queue)

def empty() :
    if len(queue) == 0 :
        return 1
    else :
        return 0

def front() :
    if len(queue) == 0 :
        return -1
    else : 
        return queue[0]

def back() :
    if len(queue) == 0 :
        return -1
    else : 
        return queue[-1]

queue = deque()

num = int(sys.stdin.readline())

for i in range(num) : 
    X = 0

    inst = sys.stdin.readline().rstrip()
    
    if 'push' in inst : 
        inst, X = inst.split()

    if inst == 'pop' :
        print(pop())
    elif inst == 'push' :
        push(X) 
    elif inst == 'size' :
        print(size())    
    elif inst == 'empty' :
        print(empty())   
    elif inst == 'front' :
        print(front())     
    elif inst == 'back' :
        print(back())
    else : 
        print('Err')