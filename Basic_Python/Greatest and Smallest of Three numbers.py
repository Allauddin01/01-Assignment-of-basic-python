#Greates and Smallest of three numbers
num1=int(input('Enter the num1 = '))
num2=int(input('Enter the num2 = '))    
num3=int(input('Enter the num3 = '))
if num1>num2 and num1>num3:
    print('num1 is greatest of num2 and num3 = ',num1)
elif num2>num1 and num2>num3:
    print('num2 is greates of num1 and num3 = ',num2)
    
elif num3>num1 and num3>num2:
    print('num3 is greatest of num1 and num2 = ',num3)
elif num1==num2 or num1==num3 or num2==num1 or num2==num3 or num3==num1 or num3==num2:
    print('num1,num2 and num3 are equal')
    