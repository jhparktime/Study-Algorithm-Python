import sys
from collections import defaultdict

N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    string = sys.stdin.readline().rstrip()
    idx = int(sys.stdin.readline().rstrip())
    
    char_positions = defaultdict(list)
    
    for i, s in enumerate(string):
        char_positions[s].append(i)
    
    min_len = float('inf')
    max_len = -1
    
    for char, positions in char_positions.items():
        if len(positions) < idx:
            continue
        
        for i in range(len(positions) - idx + 1):
            start = positions[i]
            end = positions[i + idx - 1]
            length = end - start + 1
            
            min_len = min(min_len, length)
            max_len = max(max_len, length)
    
    if max_len == -1:
        print(-1)
    else:
        print(min_len, max_len)