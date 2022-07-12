with open('input.txt','r') as f:
    input = f.read().split(",")
    for i in range(len(input)):
        input[i] = input[i].strip()

direction = 'N'
x = 0
y = 0
for s in input:
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
print(abs(x)+abs(y))  #226
        
            
            