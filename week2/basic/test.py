n = int(input())

b = int(input())
def nsum(n):
    result = 0
    for i in range(n):
        result+=i
    return result

def recur(n):
    if n == 0:
        return 0
    if n < 0:
        return False
    else:
        return n+recur(n-1)
    
def exp(b,n):
    
    if n == 0:
        return 1
    else:
        return b*exp(b,n-1)
def expt(b,n):
    # if n == 0:
    #     return 1
    # if n % 2 == 0:
    #     return b*exp(n//2)
    # else:
    #     return 0
   pass

def fib(n):
 

    if n == 0 :
        return 0
    elif n == 1:
        return 1 
    
   
    return fib(n-1)+ fib(n-2)

