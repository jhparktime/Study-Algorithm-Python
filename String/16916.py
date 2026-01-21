import sys

string = sys.stdin.readline().rstrip()
partial = sys.stdin.readline().rstrip()

if partial in string : 
    print(1)
else :
    print(0)
    