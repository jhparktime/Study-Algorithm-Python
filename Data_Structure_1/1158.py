import sys

N, K = sys.stdin.readline().split()
N = int(N)
K = int(K)

list = [i for i in range(1, N+1)]
out = []
ptr = 0

for _ in range(N) :
    ptr = ptr + K - 1  
    while ptr >= len(list) :  
        ptr = ptr - len(list)
    out.append(list.pop(ptr))  # ptr 위치의 요소 제거

result = '<'
for j in range(len(out)):
    if j > 0:
        result += ', '
    result += str(out[j])
result += '>'
print(result)