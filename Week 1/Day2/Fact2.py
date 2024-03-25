def factorial(num):
    product=1
    for x in range (1,num+1):
        product=product*x 
    return product

n=int(input("Enter Num :"))
if num<0:
    print("None")
else:
    print( "Factorial is ",factorial(num))