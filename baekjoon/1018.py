import sys

def cnt(new_board):
    w_renew = 0
    b_renew = 0

    # 8*8로 자른 new_board에 대하여
    # W로 시작하는 경우
    for m in range(8):
        for n in range(8):
            if((m%2 == 0 and n%2 ==0) or (m % 2 ==1 and n%2==1)):
                if new_board[m][n] != "W":
                    w_renew += 1
                
            elif ((m%2 == 0 and n%2 ==1) or (m % 2 ==1 and n%2==0)):
                if new_board[m][n] != "B":
                    w_renew += 1

    # B로 시작하는 경우
    for m in range(8):
        for n in range(8):
            if((m%2 == 0 and n%2 ==0) or (m % 2 ==1 and n%2==1)):
                if new_board[m][n] != "B":
                    b_renew += 1
                
            elif ((m%2 == 0 and n%2 ==1) or (m % 2 ==1 and n%2==0)):
                if new_board[m][n] != "W":
                    b_renew += 1                   

    return min(w_renew, b_renew)

m,n = map(int, input().split())
board = []

# board 입력받기
for i in range(m):
    board.append([i for i in sys.stdin.readline()][:-1])

min_renew = 1e9
renew = 0

for y in range(m-7):
    for x in range(n-7):
        # 8*8 board로 자르기.
        new_board = [row[y:y+8] for row in board[x:x+8]]
        renew = cnt(new_board)
        min_renew = min(min_renew, renew)

        print(new_board)


# print(min_renew)

