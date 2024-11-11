from math import log
def main1():
    def f(t : float, y : float) -> float:
        return 1 + y/t

    def df(t : float, y : float) -> float:
        return -y/(t**2) +(1/t + y/(t**2))
    def solution(t):
        return t*log(t) + 2*t
    def taylor_order2(a : float ,h : float,b : float, y0 : float):
        y = y0
        t = a
        while t < (b+h):
            print(f"t : {t} w : {y} y : {solution(t)} error : {abs(y - solution(t))}")
            y = y + h*f(t,y) + (h*h*df(t,y))/2
            t = round(t+h,5)
    if __name__ == "__main__":
        taylor_order2(1,0.25,2,2)

def main2():
    def f(t : float, y : float) -> float:
        return 1 + y/t
    def solution(t):
        return t*log(t) + 2*t
    def rk2(a : float ,h : float,b : float, y0 : float):
        y = y0
        t = a
        while t < (b+h):
            print(f"t : {t} w : {y} y : {solution(t)} error : {abs(y - solution(t))}")
            y = y + h*f(t + h/2,y + h*f(t,y)/2)
            t = round(t+h,5)
    if __name__ == "__main__":
        rk2(1,0.25,2,2)

def main3():
    def f(t : float, y : float) -> float:
        return 1 + y/t
    def solution(t):
        return t*log(t) + 2*t
    def fixed(t : float, y : float, h : float) -> float:
        result = y 
        i = 1
        while (result != (y + (h*(f(t,y) + f(t+h,result)))/2)) and (i < 100000):
            result = (y + (h*(f(t,y) + f(t+h,result)))/2)
            i += 1
        return result
    def trapezoidal2(a : float ,h : float,b : float, y0 : float):
        y = y0
        t = a
        while t < (b+h):
            print(f"t : {t} w : {y} y : {solution(t)} error : {abs(y - solution(t))}")
            y = fixed(t,y,h)
            t = round(t+h,5)
    if __name__ == "__main__":
        trapezoidal2(1,0.25,2,2)


if __name__ == "__main__":
    print("taylor order 2")
    main1()
    print("runge kutta - 2")
    main2()
    print("trapezoidal")
    main3()

