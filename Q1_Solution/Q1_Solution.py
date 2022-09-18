def factorial(any_number):
    fact = 1
    for i in range(1,any_number+1):
        fact = fact*i
    return fact
        
def sumofdigitfact(any_number):
    fact_number = str(factorial(any_number))
    sumfact = 0
    for i in fact_number:
        sumfact = int(i)+sumfact
    return fact_number,sumfact
    

number = 100
fctorial,summ = sumofdigitfact(number)

print(f"\n\nThe sum of the digits in the factorial of number {number} is: {summ}")