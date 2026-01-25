import sys

N = int(sys.stdin.readline().rstrip())

stack = []
for _ in range(N):
    stack.append(int(sys.stdin.readline().rstrip()))

stack.sort(reverse=True)  # 내림차순 정렬

payload = []

while len(stack) > 0 :
    tmp = stack.pop()
    payload.append(tmp * (len(stack) + 1))

print(max(payload))