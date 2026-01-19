import sys
from collections import deque

C = int(sys.stdin.readline().strip())

for _ in range(C) : 
    N, M = map(int, sys.stdin.readline().strip().split())  
    prior = list(map(int, sys.stdin.readline().strip().split())) 
    
    queue = deque([(i, prior[i]) for i in range(N)])
    count = 0

    while True : 
        idx, pri = queue.popleft()

        if any(p > pri for _, p in queue):
            queue.append((idx, pri))  
        else:
            count += 1  
            if idx == M: 
                print(count)
                break
    