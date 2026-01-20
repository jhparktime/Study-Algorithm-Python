import sys

start = list(map(int, sys.stdin.readline().rstrip().split(':')))
end = list(map(int, sys.stdin.readline().rstrip().split(':')))

start_sec = start[0] * 3600 + start[1] * 60 + start[2]
end_sec = end[0] * 3600 + end[1] * 60 + end[2]

diff = end_sec - start_sec

if diff <= 0:
    diff += 24 * 3600

h = diff // 3600
m = (diff % 3600) // 60
s = diff % 60

print(f"{h:02d}:{m:02d}:{s:02d}")