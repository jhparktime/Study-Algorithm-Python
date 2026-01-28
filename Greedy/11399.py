import sys

N = int(sys.stdin.readline().rstrip())

stack = []

string = sys.stdin.readline().rstrip()
stack = list(map(int, string.split()))

stack.sort()

cnt = 0
for j in range(len(stack)) :
    tmp = 0
    for i in range(j+1) : 
        tmp += stack[i]
    cnt += tmp

print(cnt)