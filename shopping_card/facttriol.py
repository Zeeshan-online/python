def factorial(n):
    num = int(input("enter the value = "))  
    if n < 0:
        return"Factroial is not defined for nagative numbers."
    
    result = 1
    while n > 0:
       result *= n

       n -= 1

       return result
    
    print(num)
    

    