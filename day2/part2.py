with open("input.txt",'r') as f:
    data = f.read().split("\n")
    
def move(cur_row,cur_col,dirs,mat):
    for dir in dirs:
        if dir == 'L':
            if cur_col == 0 or  mat[cur_row][cur_col - 1] == 0 :
                continue
            else:
                cur_col -= 1
              
        elif dir == 'R':
            if cur_col == 4 or mat[cur_row][cur_col + 1] == 0:
                continue
            else:
                cur_col += 1
        elif dir == 'U':
            if cur_row == 0 or mat[cur_row - 1][cur_col] == 0:
                continue
            else:
                cur_row -=1
        else:
            if cur_row == 4 or mat[cur_row + 1][cur_col] == 0:
                continue
            else:
                cur_row += 1
    return [cur_row,cur_col]

if __name__ == "__main__":
    mat = [[0,0,1,0,0],
           [0,2,3,4,0],
           [5,6,7,8,9],
           [0,'A','B','C',0],
           [0,0,'D',0,0]]
    cur_row = 1
    cur_col = 1
    for d in data:
        cur_row,cur_col = move(cur_row,cur_col,d,mat)
        value = mat[cur_row][cur_col]
        print("new row: {}, new col: {}, value: {}".format(cur_row,cur_col,value))
    #final answer: 46C92