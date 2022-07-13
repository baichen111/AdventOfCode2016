data:read0 `:input.txt
mat: 3 3#1+til 9

pos:1 1
f:{[pos;dirs] 
   {
    $[y="U";x[0]-:1;y="D";x[0]+:1;y="L";x[1]-:1;y="R";x[1]+:1];
    $[x[0]<=0;x[0]:0;x[0]>2;x[0]:2];
    $[x[1]<0;x[1]:0;x[1]>2;x[1]:2];
    x}/[pos;dirs] 
 }
new_pos:f\[pos;data]   
mat ./:new_pos   / final answer: 38961