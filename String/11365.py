import sys

while True :
    string = sys.stdin.readline().rstrip()
    if string == 'END' :
        break
    else :        
        print(''.join(reversed(string)))
    