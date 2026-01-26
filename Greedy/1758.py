import sys

N = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(N) :
    stack.append(int(sys.stdin.readline().rstrip()))

stack.sort(reverse=True)

tip = 0

for i in range(1, len(stack)+1) :
    if stack[i-1] - i + 1  < 0 :
        pass
    else :
        tip += stack[i-1] - i + 1

print(tip)