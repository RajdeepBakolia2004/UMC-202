from math import exp,sin
def f1(t : float, y1: float, y2 : float):
    return y2
def f2(t : float, y1 : float, y2 : float):
    return 2*y2-2*y1 + exp(2*t)*sin(t)

def rk4(a: float, b:float, h:float, y1:float, y2:float):
    t = a
    print(f"t : {t} w1 : {y1} w2 : {y2}")
    while t < b:
        k11 = h*f1(t,y1,y2)
        k12 = h*f2(t,y1,y2)
        k21 = h*f1(t+h/2,y1+k11/2,y2+k12/2)
        k22 = h*f2(t+h/2,y1+k11/2,y2+k12/2)
        k31 = h*f1(t+h/2,y1+k21/2,y2+k22/2)
        k32 = h*f2(t+h/2,y1+k21/2,y2+k22/2)
        k41 = h*f1(t+h,y1+k31,y2+k32)
        k42 = h*f2(t+h,y1+k31,y2+k32)
        y1 = y1 + 1/6*(k11+2*k21+2*k31+k41)
        y2 = y2 + 1/6*(k12+2*k22+2*k32+k42)
        t = round(t + h,5)
        print(f"t : {t} w1 : {y1} w2 : {y2}")

if __name__ == "__main__":
    rk4(0,1,0.1,-0.4,-0.6)
