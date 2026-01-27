import sys

N, target = map(int, sys.stdin.readline().rstrip().split())
stack = []

for _ in range(N) :
    stack.append(int(sys.stdin.readline().rstrip()))

cnt = 0

for j in range(len(stack) - 1, -1, -1):
    tmp = stack[j]
    if target >= tmp:
        cnt += target // tmp 
        target = target % tmp  
    if target == 0:
        break

print(cnt)