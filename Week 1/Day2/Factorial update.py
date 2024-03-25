from math import factorial
def fatorial(num):
    if type(num) is not int:
        return None
    if num<0:
        return None
    if num==0:
        return 1
    return num*factorial(num-1)
   
 
   
    
    

    