i:read0 `:input.txt
data:{"I"$a where not (a:" " vs trim x) like ""}each i 

f:{m3:max x;m2:min[x except m1:min[x]];
   $[m3<m1+m2;1;0]
 }
sum f'[data]  / final answer: 862