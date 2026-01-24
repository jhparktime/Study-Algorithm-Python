import sys
import re

N = int(sys.stdin.readline().rstrip())

for _ in range(N) :
    string = sys.stdin.readline().rstrip()
    pattern = r'^[ABCDEF]?A+F+C+[ABCDEF]?$'

    if re.fullmatch(pattern, string):
        print('Infected!')
    else:
        print('Good')