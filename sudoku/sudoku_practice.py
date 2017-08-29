#class point:
#    def __int__(self,x,y):
#        self.x=x
#        self.y=y
#        self.available=[]
#        self.value=0

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.available = []
        self.value = 0

def rownum(p, sudoku):
    row=set(sudoku[p.y*9:(p.y+1)*9])
    row.remove(0)
    return row

def colnum(p, sudoku):
    col=[]
    length=len(sudoku)
    for i in range(p.x,length,9):
        col.append(sudoku[i])
    col=set(col)
    col.remove(0)
    return col


def blocknum(p, sudoku):
    block_row=p.y//3
    block_col=p.x//3
    block=[]
    start=block_col*3+block_row*3*9
    for i in range(start,start+3):
        block.append(sudoku[i])
    for i in range(start+9,start+3+9):
        block.append(sudoku[i])
    for i in range(start+9+9,start+3+9+9):
        block.append(sudoku[i])
    block=set(block)
    block.remove(0)
    return block

def init(sudoku):
    pointlist=[]
    length=len(sudoku)
    for i in range(length):
        if sudoku[i]==0:
            p=point(i%9,i//9)
            for j in range(1,10):
                if j not in rownum(p,sudoku) and j not in colnum(p,sudoku) and j not in blocknum(p,sudoku):
                    p.available.append(j)
            pointlist.append(p)
    return pointlist

def tryinsert(p,sudoku):
    a_num=p.available
    for v in a_num:
        p.value=v
        if check(p,sudoku):
            sudoku[p.y * 9 + p.x] = p.value
            if len(pointlist) <= 0:#done!
                showSudoku(sudoku)
                exit()
            p2=pointlist.pop()
            tryinsert(p2,sudoku)
            sudoku[p2.y * 9 + p2.x] = 0 #回到上一级
            sudoku[p.y * 9 + p.x] = 0
            p2.value = 0
            pointlist.append(p2)
        else:
            pass

def showSudoku(sudoku):
    for j in range(9):
        for i in range(9):
            print('%d ' % (sudoku[j * 9 + i]), end='')
        print('')


def check(p, sudoku):
    if p.value == 0:
        print('not assign value to point p!!')
        return False
    if p.value not in rownum(p, sudoku) and p.value not in colnum(p, sudoku) and p.value not in blocknum(p, sudoku):
        return True
    else:
        return False

if __name__ == '__main__':
    sudoku = [
        8, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 3, 6, 0, 0, 0, 0, 0,
        0, 7, 0, 0, 9, 0, 2, 0, 0,
        0, 5, 0, 0, 0, 7, 0, 0, 0,
        0, 0, 0, 0, 4, 5, 7, 0, 0,
        0, 0, 0, 1, 0, 0, 0, 3, 0,
        0, 0, 1, 0, 0, 0, 0, 6, 8,
        0, 0, 8, 5, 0, 0, 0, 1, 0,
        0, 9, 0, 0, 0, 0, 4, 0, 0,
    ]
    pointlist=init(sudoku)
    showSudoku(sudoku)
    print("\n")
    p=pointlist.pop()
    tryinsert(p,sudoku)