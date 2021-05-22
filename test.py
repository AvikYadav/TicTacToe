import sys
import random
board = ['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
def isEmpty(pos,bo):
    if bo[pos] == ' ':return True
    else:return False
def Print_Board(bo):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print()
    print()
    print()
# def block(bo,player):
#     winnerMoves=[[1,2,3],
#                  [4,5,6],
#                  [7,8,9],
#                  [1,4,7],
#                  [3,6,9],
#                  [2,5,8],
#                  [1,5,7],
#                  [3,5,9]
#                  ]
#     for row in winnerMoves:
#         playerSpace = 0
#         emp = 0
#         for i in row:
#             # check if player is about to win
#             if bo[i] == player:
#                 playerSpace += 1
#             if bo[i] == ' ':
#                 emp = i
#             if playerSpace == 2:
#                 compMove(bo,emp)
#                 return True
def compMove(bo):
    move = 0
    possibleMoves = [x for x, letter in enumerate(bo) if letter == ' ' and x != 0]
    print(possibleMoves)
    for let in ['o','x']:
        for i in possibleMoves:
            boardCopy = bo[:]
            boardCopy[i] = let
            if winner(let,boardCopy):
                move = i
                return move
    #center
    if 5 in possibleMoves:
        move = 5
        return move

    #corner
    corner= []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            corner.append(i)

    if len(corner) > 0:
        ran = random.randint(0,len(corner))
        move = ran
        return move

    #edges
    edge = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edge.append(i)

    if len(edge) > 0:
        ran = random.randint(0, len(edge))
        move = ran
        return move

    # if not pos:
    #     possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    #     print(possibleMoves)
    #     length = len(possibleMoves)
    #     ran = random.randint(1,length-1)
    #     print(ran)
    #     print(possibleMoves[ran])
    #     process(possibleMoves[ran],'x',bo)
    # else:
    #     process(pos,'x',bo)

def playerMove(bo):
    try:
        inp = int(input('enter pos where you want to play your move 1-9 :'))
        if inp > 10:
            print('invalid location')
            playerMove(bo)
        if isEmpty(inp,bo):
            process(inp,'o',bo)
        else:
            print('invalid location ( already occupied )')
            playerMove(bo)
    except:
        print("pls enter a number ")
        playerMove(bo)
def process(pos,move,bo):
    bo[pos] = move

def BoardFull(bo):
    if bo.count(' ') > 0:  # Since we always have one blank element in board we must use > 1
        return False
    else:
        return True


def winner(player,bo):
    if bo[1] == player and bo[2] == player and bo[3] == player:
        return True
    if bo[4] == player and bo[5] == player and bo[6] == player:
        return True
    if bo[7] == player and bo[8] == player and bo[9] == player:
        return True
    if bo[1] == player and bo[4] == player and bo[7] == player:
        return True
    if bo[3] == player and bo[6] == player and bo[9] == player:
        return True
    if bo[2] == player and bo[5] == player and bo[8] == player:
        return True
    if bo[1] == player and bo[5] == player and bo[9] == player:
        return True
    if bo[3] == player and bo[5] == player and bo[7] == player:
        return True
    else:
        return False
def Main(bo):
    run = True
    while run:
        if winner('x', bo):
            print()
            print("----------------\n computer Wins\n -------------")
            print()
            break
        if winner('o', bo):
            print()
            print("----------------\n player Wins\n -------------")
            print()
            break
        if BoardFull(bo):
            print()
            print("----------------\n Tie Game ! \n -------------")
            print()
            break
        else:
            # if not block(bo,'o'):
            co = compMove(bo)
            process(co,'x',bo)
            Print_Board(bo)
            if winner('x', bo):
                print()
                print("----------------\n computer Wins\n -------------")
                print()
                break
            if winner('o', bo):
                print()
                print("----------------\n player Wins\n -------------")
                print()
                break
            if BoardFull(bo):
                print()
                print("----------------\n Tie Game ! \n -------------")
                print()
                break
            playerMove(bo)
            Print_Board(bo)

Main(board)