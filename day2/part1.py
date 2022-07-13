
with open("input.txt",'r') as f:
    data = f.read().split("\n")

def move(cur_row,cur_col,dirs):
    for dir in dirs:
        if dir == 'L':
            cur_col -= 1
            if cur_col < 0:
                cur_col = 0
        elif dir == 'R':
            cur_col += 1
            if cur_col > 2:
                cur_col = 2
        elif dir == 'U':
            cur_row -= 1
            if cur_row < 0:
                cur_row = 0
        else:
            cur_row += 1
            if cur_row > 2:
                cur_row = 2
    return [cur_row,cur_col]
                
if __name__ == "__main__":
     mat = [[1,2,3],[4,5,6],[7,8,9]]
     cur_row = 1
     cur_col = 1
     for d in data:
         cur_row,cur_col = move(cur_row,cur_col,d)
         value = mat[cur_row][cur_col]
         print("new row: {}, new col: {}, value: {}".format(cur_row,cur_col,value))
     # final answer: 38961
     
    