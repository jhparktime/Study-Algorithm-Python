import sys

N = int(sys.stdin.readline().rstrip())
events = []

for i in range(N):
    x, r = map(int, sys.stdin.readline().split())
    events.append((x - r, i, 0))  # open
    events.append((x + r, i, 1))  # close

events.sort(key=lambda e: (e[0], e[2]))

# 같은 좌표 체크 + 스택 처리
stack = []
for i in range(len(events)):
    x, idx, t = events[i]
    
    # 같은 좌표 체크
    if i > 0 and events[i-1][0] == x:
        print("NO")
        exit()
    
    if t == 0:  # open
        stack.append(idx)
    else:  # close
        if not stack or stack[-1] != idx:
            print("NO")
            exit()
        stack.pop()

print("YES" if not stack else "NO")