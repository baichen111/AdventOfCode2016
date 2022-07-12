
def path(x0,y0,x1,y1,direction):
    if direction == 'N' or direction == 'E':
        step = 1
    else:
        step = -1
    
    if x0 == x1:
        return [(x0,yi) for yi in range(y0,y1,step)] 
    elif y0 == y1:
        return [(xi,y0) for xi in range(x0,x1,step)]

def main():
    with open('input.txt','r') as f:
        input = f.read().split(",")
        for i in range(len(input)):
            input[i] = input[i].strip()

    direction = 'N'
    x = 0
    y = 0
    count = set()
    for s in input:
        x0 = x
        y0 = y
        
        if direction == 'N':
            if s[0] == 'L':
                direction = 'W'
                x -= int(s[1:])
            elif s[0] == 'R':
                direction = 'E'
                x += int(s[1:])
        elif direction == 'W':
            if s[0] == 'L':
                direction = 'S'
                y -= int(s[1:])
            elif s[0] == 'R':
                direction = 'N'
                y += int(s[1:])
        elif direction == 'S':
            if s[0] == 'L':
                direction = 'E'
                x += int(s[1:])
            elif s[0] == 'R':
                direction = 'W'
                x -= int(s[1:])
        elif direction == 'E':
            if s[0] == 'L':
                direction = 'N'
                y += int(s[1:])
            elif s[0] == 'R':
                direction = 'S'
                y -= int(s[1:])
        for x_y in path(x0,y0,x,y,direction):
            if x_y in count:
                print(x_y)  #79
                return 
            count.add(x_y)
if __name__ == "__main__":
    main()            




    


        
            
            