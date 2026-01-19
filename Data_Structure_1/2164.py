import sys
from collections import deque

N = sys.stdin.readline()
N = int(N)

dq = deque(range(1, N+1))

while(len(dq) > 1) :
    dq.popleft()
    dq.append(dq.popleft())

print(dq.pop())