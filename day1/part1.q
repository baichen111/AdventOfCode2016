i:trim each "," vs first read0 `:input.txt
d:`dir`x_pos`y_pos!(`N;0;0)

result:{ 
  $["L"=first y;
    [$[x[`dir]=`N;[x[`x_pos]-:"I"$1_y;x[`dir]:`W];
      x[`dir]=`W;[x[`y_pos]-:"I"$1_y;x[`dir]:`S];
      x[`dir]=`S;[x[`x_pos]+:"I"$1_y;x[`dir]:`E];
      x[`dir]=`E;[x[`y_pos]+:"I"$1_y;x[`dir]:`N]];];
  "R"=first y;
    [$[x[`dir]=`N;[x[`x_pos]+:"I"$1_y;x[`dir]:`E];
      x[`dir]=`E;[x[`y_pos]-:"I"$1_y;x[`dir]:`S];
      x[`dir]=`S;[x[`x_pos]-:"I"$1_y;x[`dir]:`W];
      x[`dir]=`W;[x[`y_pos]+:"I"$1_y;x[`dir]:`N]]];];x}/[d;i]
sum result`x_pos`y_pos  / 226