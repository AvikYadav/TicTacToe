import random
import sys
grid = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]
def display():
    print('1 ',grid[0])
    print('2 ', grid[1])
    print('3 ', grid[-1])
    print('    a      b    c')
def Input():
    inp = input('pls enter input in following manner - \nrow -1,2,3 and column - a,b,c\n then X/O seperated by space :')
    inp = inp.lower()
    inp = inp.split()
    print(inp)
    lent = len(inp)
    if lent ==3 :
        return inp
    else:
        print('invalid input ')
def Process(inp):
    if inp[0] == '1':
        if inp[1] == 'a':
            grid[0][0] = inp[-1]
        elif inp[1] == 'b':
            grid[0][1] = inp[-1]
        elif inp[1] == 'c':
            grid[0][-1] = inp[-1]
        else:
            print('invalid input')
    elif inp[0] == '2':
        if inp[1] == 'a':
            grid[1][0] = inp[-1]
        elif inp[1] == 'b':
            grid[1][1] = inp[-1]
        elif inp[1] == 'c':
            grid[1][-1] = inp[-1]
        else:
            print('invalid input')
    elif inp[0] == '3':
        if inp[1] == 'a':
            grid[-1][0] = inp[-1]
        elif inp[1] == 'b':
            grid[-1][1] = inp[-1]
        elif inp[1] == 'c':
            grid[-1][-1] = inp[-1]
        else:
            print('invalid input')
    else:
        print('invalid input')
def check(inp):
    if inp[-1] == 'x' or inp[-1] == 'o':
        return inp
    sys.exit('invalid input must use x or o')
def winner():
    isWin = False
    if grid[0][0] == 'x' and grid[1][0] == 'x' and grid[-1][0] == 'x':
        isWin = True
    if grid[0][0] == 'x' and grid[1][1] == 'x' and grid[-1][-1] == 'x':
        isWin = True
    if grid[0][0] == 'x' and grid[0][1] == 'x' and grid[0][-1] == 'x':
        isWin = True
    if grid[1][0] == 'x' and grid[1][1] == 'x' and grid[1][-1] == 'x':
        isWin = True
    if grid[-1][0] == 'x' and grid[-1][1] == 'x' and grid[-1][-1] == 'x':
        isWin = True
    if grid[0][1] == 'x' and grid[1][1] == 'x' and grid[-1][1] == 'x':
        isWin = True
    if grid[0][-1] == 'x' and grid[1][-1] == 'x' and grid[-1][-1] == 'x':
        isWin = True
    if grid[0][-1] == 'x' and grid[1][1] == 'x' and grid[-1][0] == 'x':
        isWin = True

    isWinO = False

    if grid[0][0] == 'o' and grid[1][0] == 'o' and grid[-1][0] == 'o':
        isWinO = True

    if grid[0][0] == 'o' and grid[1][1] == 'o' and grid[-1][-1] == 'o':
        isWinO = True

    if grid[0][0] == 'o' and grid[0][1] == 'o' and grid[0][-1] == 'o':
        isWinO = True

    if grid[1][0] == 'o' and grid[1][1] == 'o' and grid[1][-1] == 'o':
        isWinO = True

    if grid[-1][0] == 'o' and grid[-1][1] == 'o' and grid[-1][-1] == 'o':
        isWinO = True
    if grid[0][1] == 'o' and grid[1][1] == 'o' and grid[-1][1] == 'o':
        isWinO = True

    if grid[0][-1] == 'o' and grid[1][-1] == 'o' and grid[-1][-1] == 'o':
        isWinO = True

    if grid[0][-1] == 'o' and grid[1][1] == 'o' and grid[-1][0] == 'o':
        isWinO = True
    if isWin:
        print("X win")
        sys.exit('game over')
    if isWinO:
        print("o win")
        sys.exit('game over')
for i in range(111):
    turn = ""
    if i == 0:
        turn = 'ai turn'
        print(turn)
    elif i%2 == 0:
        turn = 'x turn'
        print(turn)
    else:
        turn = 'o turn'
        print(turn)
    display()
    inp = Input()
    inp = check(inp)
    Process(inp)
    winner()
