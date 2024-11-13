def u_cal(u, n):
    temp = u
    for i in range(1, n):
        temp = temp * (u + i)
    return temp

def fact(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

n = 4;
x = [0.1,0.2,0.3,0.4]
     
# y[][] is used for difference table
# with y[][0] used for input
y = [[0 for i in range(n)]
        for j in range(n)];
y[0][0] = -0.62049958;
y[1][0] = -0.28398668;
y[2][0] = 0.00660095;
y[3][0] = 0.24842440;

# Calculating the backward difference table
for i in range(1, n):
    for j in range(n - 1, i - 1, -1):
        y[j][i] = y[j][i - 1] - y[j - 1][i - 1]

# Displaying the backward difference table
for i in range(n):
    for j in range(i + 1):
        print(y[i][j], end="\t")
    print()

value = -1/3

def backward(value, degree):
    sum = y[n - 1][0]
    u = (value - x[n - 1]) / (x[1] - x[0])
    for i in range(1, degree + 1):
        sum = sum + (u_cal(u, i) * y[n - 1][i]) / fact(i)
    return sum
print("The value of f(-1/3) for degree 4 is:", backward(value, 0))
print("The value of f(-1/3) for degree 1 is:", backward(value, 1))
print("The value of f(-1/3) for degree 2 is:", backward(value, 2))
print("The value of f(-1/3) for degree 3 is:", backward(value, 3))

