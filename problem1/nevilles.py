import math
x = [1,1.3,1.6,1.9,2.2]
y = [0.7651997,0.620086,0.4554022,0.2818186,0.1103623]
n = len(x) - 1
a = eval(input("Enter the number = "))
array = [[y[_]] for _ in range(n+1)]
for i in range(1,n+1):
    l = array[i]
    for j in range(1,i+1):
        l.append(((a - x[i-j])*array[i][j-1] - (a - x[i])*array[i-1][j-1])/(x[i] - x[i-j]))
for i in range(n+1):
    l = array[i]
    print(f"{x[i]:4f} : ",end = '')
    for ele in l :
        print(f"{ele:.7f}" ,end = ' ')
    print()




