board = input()

start = -1
tmp = []

for i in range(len(board)) :
    if board[i] == '.' :
        if start == -1 : # 처음 만나는 .이 아님
            continue
        else : 
            length = i - start

            if length % 2 == 1 : # length가 길이가 짝수가 아니면 못 채움
                print(-1)
                exit()

            else :
                while length != 0 :
                    if length >= 4 : 
                        tmp.append('AAAA')
                        length -= 4
                    else :
                        tmp.append('BB')
                        length -= 2
                replacement = ''.join(tmp)
                board = board[:start] + replacement + board[i:]

                tmp = []
            start = -1

    elif board[i] == 'X' :
        if start == -1 :
            start = i

if start != -1:
    length = len(board) - start
    if length % 2 == 1:
        print(-1)
        exit()
    else:
        while length != 0:
            if length >= 4:
                tmp.append('AAAA')
                length -= 4
            else:
                tmp.append('BB')
                length -= 2
        replacement = ''.join(tmp)
        board = board[:start] + replacement

if 'X' in board:
    print(-1)
else:
    print(board)
    