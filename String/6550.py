import sys
from collections import deque

while True :
    line = sys.stdin.readline().rstrip()
    if not line:   # EOF
        break

    s, t = line.split()

    s = deque(list(map(str, s)))

    for i in t : 
        if i == s[0] :
            s.popleft()

        if len(s) == 0 :
            print("Yes")
            break
    
    if len(s) != 0 :
        print("No")
    
        