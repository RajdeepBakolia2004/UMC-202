x = [-2,-1,0,1,2,3]
y = [1,4,11,16,13,4]
n = len(x)
y = [[0 for i in range(n)]
        for j in range(n)];
y[0][0] = 1;
y[1][0] = 4;
y[2][0] = 11;
y[3][0] = 16;
y[4][0] = 13;
y[5][0] = 4;
 

for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1];
 
for i in range(n):
    print(x[i], end = "\t");
    for j in range(n - i):
        print(y[i][j], end = "\t");
    print("");
 