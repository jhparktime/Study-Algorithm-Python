import sys

N, M = sys.stdin.readline().rstrip().split()

N = int(N)
M = int(M)

unseen = set([])
unlisten = set([])

for _ in range(N) :
    string = sys.stdin.readline().rstrip()
    unseen.add(string)

for _ in range(M) :
    string = sys.stdin.readline().rstrip()
    unlisten.add(string)

out = unseen & unlisten

print(len(out))
print("\n".join(sorted(out)))


