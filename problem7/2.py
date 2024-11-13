from math import exp
def f(t : float ,y : float):
    return y-t**2+1
def solution(t : float):
    return (t+1)**2-0.5*exp(t)

def runge_kutta(t0 : float,y0 : float,h : float):
    k1 = h*f(t0,y0)
    k2 = h*f(t0+h/2,y0+k1/2)
    k3 = h*f(t0+h/2,y0+k2/2)
    k4 = h*f(t0+h,y0+k3)
    y = y0 + 1/6*(k1+2*k2+2*k3+k4)
    return y
def fixed(t : float,y1 : float,y0 : float,h : float):   
   result = y1
   i = 0
   while (result != y1 + (h/12)*(5*f(t + h,result) + 8*f(t,y1) - f(t-h,y0))) and (i < 10000):
       result = y1 + (h/12)*(5*f(t + h,result) + 8*f(t,y1) - f(t-h,y0))
       i += 1
   return result
def adam_moulton_two_step(t0 : float,y0 : float,h : float,b : float):
    y1 = runge_kutta(t0,y0,h)
    t = t0 + h
    print(f"t : {t0} w : {y0} y : {solution(t0)} error : {abs(y0-solution(t0))}")
    print(f"t : {t} w : {y1} y : {solution(t)} error : {abs(y1-solution(t))}")
    while t < b:
        y = fixed(t,y1,y0,h)
        y0 = y1
        y1 = y
        t = round(t + h,5)
        print(f"t : {t} w : {y} y : {solution(t)} error : {abs(y-solution(t))}")

if __name__ == "__main__":
    adam_moulton_two_step(0,0.5,0.5,2)