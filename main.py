
def collatz(x):
    result=[]
    while(x!=1):
        result.append(x)
        if(x%2==0):
            x=x2(x)
        else:
            x=x3_1(x)
    result.append(x)
    return result


def x3_1(x):
    return x * 3 + 1

def x2(x):
    return x / 2
  
def f1(x):
    while True:
        try:
            x = int(input("Введите валидное число:\n"))
            return x
        except:
            pass