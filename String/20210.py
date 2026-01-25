import sys
import functools
import re

priority = {}
for i in range(26):
    priority[chr(ord('A') + i)] = i * 2 + 1
    priority[chr(ord('a') + i)] = i * 2 + 2

def parse_string(s):
    return re.findall(r'\d+|[a-zA-Z]', s)

def compare(a, b):
    for i in range(min(len(a), len(b))):
        x, y = a[i], b[i]
        
        # 둘 다 숫자
        if x.isdigit() and y.isdigit():
            if int(x) != int(y):
                return -1 if int(x) < int(y) else 1
            if len(x) != len(y):
                return -1 if len(x) < len(y) else 1
        # 둘 다 문자
        elif x.isalpha() and y.isalpha():
            if priority[x] != priority[y]:
                return -1 if priority[x] < priority[y] else 1
        # 하나는 숫자, 하나는 문자 (숫자가 앞)
        else:
            return -1 if x.isdigit() else 1
    
    return -1 if len(a) < len(b) else (1 if len(a) > len(b) else 0)

N = int(sys.stdin.readline().rstrip())
strings = [sys.stdin.readline().rstrip() for _ in range(N)]

parsed = []
for s in strings:
    parsed.append(parse_string(s))

pairs = []
for i in range(N):
    pairs.append((strings[i], parsed[i]))

def compare_pairs(x, y):
    return compare(x[1], y[1])

pairs.sort(key=functools.cmp_to_key(compare_pairs))

for original_string, _ in pairs:
    print(original_string)

