def add(x,y):
    return x + y

def subtract(x,y):
    if x > y:
        print(x - y)
    else:
        print(y-x)

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0:
        raise ValueError("Can not divide by Zero...!!")
    return x / y
def square(x):
    return x*x


#print(add(20,6))





