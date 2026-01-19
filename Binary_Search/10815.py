import sys

N = int(sys.stdin.readline().rstrip())
pool = set(map(int, sys.stdin.readline().split())) 

M = int(sys.stdin.readline().rstrip())
check = list(map(int, sys.stdin.readline().split())) 

result = []

for i in range(M):
    if check[i] in pool:  # set에서 O(1) 탐색
        result.append(1)
    else:
        result.append(0)

print(' '.join(map(str, result)))  