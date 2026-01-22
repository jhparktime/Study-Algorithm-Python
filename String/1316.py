import sys

N = int(sys.stdin.readline().rstrip())
count = 0

for _ in range(N) :
    string = sys.stdin.readline().rstrip()

    seen = set()
    prev = ''
    is_group = True
    
    for ch in string:
        if ch != prev and ch in seen:
            is_group = False
            break
        seen.add(ch)
        prev = ch
    
    if is_group:
        count += 1

print(count)