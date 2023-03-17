#LCM stands for Least Common Multiple. It is a mathematical concept used to find the smallest positive 
#integer that is a multiple of two or more numbers.

def lcm(a,b):
    if a>b:
        greater=a
    elif b>a:
        greater=b

    while(True):
        if((greater%a==0) and (greater%b==0)):
            lcm=greater
            break
        greater=greater+1
    return lcm

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
print("The least common denomitor of "+str(num1)+" and " +str(num2)+" is: "+str(lcm(num1,num2)))
