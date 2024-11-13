
n = 4;
x = [-0.75,-0.5,-0.25,0];
     
# y[][] is used for difference table
# with y[][0] used for input
y = [[0 for i in range(n)]
        for j in range(n)];
y[0][0] = -.07181250;
y[1][0] = -.02475;
y[2][0] = 0.3349375;
y[3][0] = 1.101000;
 

for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j + 1][i - 1] - y[j][i - 1];
 
for i in range(n):
    print(x[i], end = "\t");
    for j in range(n - i):
        print(y[i][j], end = "\t");
    print("");
 
# Value to interpolate at
value = -1/3;
#using the formula to interpolate degree 1
def interpolate(value,degree):
    result = 0
    for i in range(degree):
        temp = y[0][0]
        for j in range(i):
            temp *= (value-x[j])
        result += temp
    return result
print("The value of f(-1/3) for degree 1 is: ",interpolate(value,1))
print("The value of f(-1/3) for degree 2 is: ",interpolate(value,2))
print("The value of f(-1/3) for degree 3 is: ",interpolate(value,3))
print("The value of f(-1/3) for degree 4 is: ",interpolate(value,4))


