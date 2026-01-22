import sys

N = int(sys.stdin.readline().rstrip())
file = {}

for _ in range(N) :
    string = sys.stdin.readline().rstrip().split('.')
    sub = string[-1]

    if sub not in file.keys() :
        file[sub] = 1
    else :
        file[sub] += 1

out = sorted(file)

for i in range(len(file)) :
    print(f"{out[i]} {file[out[i]]}")