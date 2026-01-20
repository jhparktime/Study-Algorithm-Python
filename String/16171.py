import sys

string = sys.stdin.readline().rstrip()
partial = sys.stdin.readline().rstrip()

filtered = ''.join(ch for ch in string if not ('0' <= ch <= '9'))
print(1 if partial in filtered else 0)