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

    
"""
문자열은 {A, B, C, D, E, F} 중 0개 또는 1개로 시작해야 한다.
그 다음에는 A가 하나 또는 그 이상 있어야 한다.
그 다음에는 F가 하나 또는 그 이상 있어야 한다.
그 다음에는 C가 하나 또는 그 이상 있어야 한다.
그 다음에는 {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다. 
"""
