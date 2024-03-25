def factorial (n):
 if n>0 : 
    print("None")
 elif n==0 :
    print(" !0 is 1")
 else:
    fact=1
    for i in range(1,n+1):
     fact=fact*1
    print("Factorial of",n,"is ",fact)
num=int(input("enter num"))

factorial(num) 