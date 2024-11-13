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

def fixed(t : float,y2 : float,y1 : float,y0 : float,h : float):   
   result = y2
   i = 0
   while (result != y2 + (h/24)*(9*f(t+h,result) + 19*f(t,y2) - 5*f(t-h,y1) + f(t-2*h,y0))) and (i < 10000):
       result = y2 + (h/24)*(9*f(t+h,result) + 19*f(t,y2) - 5*f(t-h,y1) + f(t-2*h,y0))
       i += 1
   return result

def adam_basforth_three_step(t0 : float,y0 : float,h : float,b : float):
    y1 = runge_kutta(t0,y0,h)
    y2 = runge_kutta(t0+h,y1,h)
    t = t0 + 2*h
    print(f"t : {t0} w : {y0} y : {solution(t0)} error : {abs(y0-solution(t0))}")
    print(f"t : {t-h} w : {y1} y : {solution(t-h)} error : {abs(y1-solution(t-h))}")
    print(f"t : {t} w : {y2} y : {solution(t)} error : {abs(y2-solution(t))}")
    while t < b:
        y = y2 + (h/12)*(23*f(t,y2) - 16*f(t-h,y1) + 5*f(t-2*h,y0))
        y0 = y1
        y1 = y2
        y2 = y
        t = round(t + h,5)
        print(f"t : {t} w : {y} y : {solution(t)} error : {abs(y-solution(t))}")

def adam_moulton_three_step(t0 : float,y0 : float,h : float,b : float):
    y1 = runge_kutta(t0,y0,h)
    y2 = runge_kutta(t0+h,y1,h)
    t = t0 + 2*h
    print(f"t : {t} w : {y2} y : {solution(t)} error : {abs(y2-solution(t))}")
    print(f"t : {t0} w : {y0} y : {solution(t0)} error : {abs(y0-solution(t0))}")
    print(f"t : {t} w : {y1} y : {solution(t)} error : {abs(y1-solution(t))}")
    while t < b:
        y = fixed(t,y2,y1,y0,h)
        y0 = y1
        y1 = y2
        y2 = y
        t = round(t + h,5)
        print(f"t : {t} w : {y} y : {solution(t)} error : {abs(y-solution(t))}")

if __name__ == "__main__":
    adam_basforth_three_step(0,0.5,0.2,2)
    adam_moulton_three_step(0,0.5,0.2,2)

