import re
#process input string data
with open("input.txt",'r') as f:
    data = f.read().split("\n")
    for i in range(len(data)):
        data[i] = [x.strip() for x in data[i].strip().split("\t")]
input = [re.split(r'\s{2,}',x)  for d in data for x in d]

c = 0
for d in input:   
    for i in range(len(d)):
        d[i] = int(d[i])
    m1 = min(d)
    m3 = max(d)
    d.remove(m1)
    m2 = min(d)
    if m1 + m2 > m3:
        c += 1
print(c) # final answer: 862
        