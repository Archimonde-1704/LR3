def f1():
    while True:
        try:
            x = int(input("Введите валидное число:\n"))
            return x
        except:
            pass

def x2(x):
    return x / 2

def x3_1(x):
    return x * 3 + 1

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

if __name__=='__main__':
      print(collatz(f1())



  
