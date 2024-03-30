def f(x):
    return 5 * x ** 2 - x + 1/2

def d(x):
    return x ** 6 - 3 * x ** 2 + x - 1


def d2(x):
    return 6*x**5 - 6*x + 1




# Метод половинного деления
def method_of_dividing_a_segment_in_half(a, b, accuracy):
    left = a
    right = b
    while right - left >  2 * accuracy:
        x1 = (left + right - accuracy) / 2 
        x2 = (left + right + accuracy) / 2 
        y1 = f(x1)
        y2 = f(x2)
        if y1 > y2:
            left = x1
        else:
            right = x2
        print(left,right,x1,x2,f(x1),f(x2), right - left)
    return (left + right) / 2


# Метод золотого сечения
def method_of_golden_ratio(a, b, accuracy):
    x1 = a + 0.382 * (b - a)
    x2 = a + 0.618*(b - a)
    while abs(a - b) >= accuracy:
        if f(x1) < f(x2):
            b = x2
            x2 = x1
            x1 = a + 0.382 *(b - a)
        else:
            a = x1
            x1 = x2
            x2 = a + 0.618*(b - a) 
        print(a,b,x1,x2,f(x1),f(x2), b - a)
    return (a + b) / 2


# Метод хорд
def method_of_chords(a, b, accuracy):
    while True:
        x = round(a - d(a) / (d(a) - d(b)) * (a - b),5)
        dx = round(d(x),5)
        print(a,b,x,round(d(x),5),round(f(x),5), round(b - a,5))
        if abs(dx) <= accuracy:
            return x
        if dx > 0:
            b = x
        else:
            a = x

# Метод Ньютонаs
def method_of_newtons(accuracy, x0):
    x = x0
    while True:
        print(round(x,5),round(d(x),5))
        if abs(d(x)) <= accuracy:
            return x
        x = x - d(x) / d2(x)
        


a, b = -1,1
accuracy = 0.05
print("Результат метода половинного деления:", method_of_dividing_a_segment_in_half(a, b, accuracy))
print("Результат метода золотого сечения:",method_of_golden_ratio(a, b, accuracy))
print("Результат метода хорд:", method_of_chords(a, b, accuracy))
print("Результат метода Ньютона:", method_of_newtons(accuracy, 1.25))
