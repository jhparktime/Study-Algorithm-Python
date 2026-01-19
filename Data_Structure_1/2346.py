import sys
from collections import deque

N = int(input())
arr = list(map(int, sys.stdin.readline().split()))

dq = deque([(i+1, arr[i]) for i in range(N)])
out = []

while len(dq) > 0:
    balloon_num, move = dq.popleft()  
    out.append(balloon_num)
    
    if len(dq) > 0:
        if move > 0:  
            dq.rotate(-(move - 1))
        else: 
            dq.rotate(-move)

print(*out)