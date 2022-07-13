import re
import numpy as np
#process input string data
with open("input.txt",'r') as f:
    data = f.read().split("\n")
    for i in range(len(data)):
        data[i] = [x.strip() for x in data[i].strip().split("\t")]
input = [re.split(r'\s{2,}',x)  for d in data for x in d]
input = np.array(input).transpose().flatten().tolist()
input = [list(map(int,[input[i],input[i+1],input[i+2]])) for i in range(0,len(input),3)]

#count triangle
def count(input):
    c = 0
    for d in input:   
        m1 = min(d)
        m3 = max(d)
        d.remove(m1)
        m2 = min(d)
        if m1 + m2 > m3:
            c += 1
    return c
print(count(input)) # final answer: 1577
