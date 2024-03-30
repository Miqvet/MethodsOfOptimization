def y(x):
    return (1/7) * x ** 7 - x**3 + (1/2) * x ** 2 - x


def calculate(x1, dx, epsilon):
    while True:
        x2 = x1 + dx

        y1 = y(x1)
        y2 = y(x2)
        print(y1, y2)

        if y1 > y2:
            x3 = x1 + 2 * dx
        else:
            x3 = x1 - dx
        print(x3)
        while True:
            print("------------------------------")
            print("X: ", x1,x2,x3)
            y1 = y(x1)
            y2 = y(x2)
            y3 = y(x3)
            print("Y: ",y1,y2,y3)
            if y1 == min(y1,y2,y3):
                x_min = x1
                y_min = y1
            elif y2 == min(y1,y2,y3):
                x_min = x2
                y_min = y2
            elif y3 == min(y1,y2,y3):
                x_min = x3
                y_min = y3

            if (x2 - x3) * y1 + (x3 - x1) * y2 + (x1 - x2) * y3 == 0:
                x1 = x_min
                break
            print("Xmin", x_min)    
            
            x_new = 0.5 * ((x2 ** 2 - x3 ** 2) * y1 + (x3 ** 2 - x1 ** 2) * y2 + (x1 ** 2 - x2 ** 2) * y3) / (
                    (x2 - x3) * y1 + (x3 - x1) * y2 + (x1 - x2) * y3)
            y_new = y(x_new)
            print("Полиномы")
            print(x_new)
            print(y_new)


            if abs((y_min - y_new) / y_new) < epsilon and abs(
                    (x_min - x_new) / x_new) < epsilon:
                return x_new
            elif x1 <= x_new <= x3:
                if y_new < y2:
                    if x_new < x2:
                        x3 = x2
                        x2 = x_new
                    else:
                        x1 = x2
                        x2 = x_new
                else:
                    if x_new < x2:
                        x1 = x_new
                    else:
                        x3 = x_new
            else:
                x1 = x_new
                print("Не выполнилось условие")
                break
            


print(calculate(1.25, 0.1, 0.0001))
