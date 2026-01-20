import sys

arr = []

for _ in range(5) : 
    string = sys.stdin.readline().rstrip()
    arr.append(string)

out = []

for j in range(15) :
    for i in range(5) :
        if len(arr[i]) > j :
            out.append(arr[i][j])
        else :
            continue

print(''.join(ch for ch in out))