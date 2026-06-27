                                    #Assignment Function
#1. Write a Py fun. to sum the number in the list.
def sum_list(numbers):
    return sum(numbers)

myList=[4,7,9,3,2]
print(sum_list(myList))


#2.write a py func. to return a string.
def revstr(string):
    return ''.join (reversed(string))    # return string[::-1]

name="Hello"
print(revstr(name))


# 3. py program to make a simple calculaor using function
def calc(a,b,opr):
    if opr=='+':
        return a+b
    elif opr=='-':
        return a-b
    elif opr=='*':
        return a*b
    elif opr=='/':
        if b!=0:
            return a/b
        else:
            return "Error: Can't divided by zero "
        
    else:
        return "Invalid operator"
    
print(calc(10, 5, '+'))  
print(calc(10, 5, '-'))  
print(calc(10, 5, '*'))  
print(calc(10, 0, '/')) 


# 4. py program to display calender using function
 
import calendar

def show_calendar(year, month):
    
    print(calendar.month(year, month))

def show_year_calendar(year):
    
    print(calendar.calendar(year))

year = int(input("Enter year: "))
month = int(input("Enter month 1-12: "))
show_calendar(year, month)


# 5. power (0-9) of 2 using anonymous function

power_of_2= lambda x: 2**x
for i in range (10):
    print(f"2^{i}={power_of_2(i)}")

# 6. To calculate factorial of no.

def factorial(n):
    if n<0:
        return " There is no Factorial of neg no."
    elif n==0 or n==1:
        return 1
    else:
        fact=1
        for i in range(1,n+1):
            fact*=i
        return fact
    
print(factorial(10))


# 7. Take list and return a new list with unique element of the first list.

def unique_list(lst):
    return list(set(lst))

print(unique_list([2,2,3,4,1,1,1,3,7,6,5,4,8,6,8,6,5,4,5,2,2,3]))


# 8. py program to check the no is perfect or nor.

def is_perfect(n):
    if n<2:
        return False
    divisor_sum=0
    for i in range(1,n):
        if n%i==0:
            divisor_sum +=i

    return divisor_sum==n
    
print(is_perfect(6))
print(is_perfect(12))
print(is_perfect(28))


# 9. check the string is palindrome or not

def is_palindrome(string):
    string=string.lower().replace(" ","")
    return string==string[::-1]

print(is_palindrome("mohit"))
print(is_palindrome("madam"))
print(is_palindrome("12321"))
print(is_palindrome("asappasa"))


# 10. python func. that print first n row of pascal triangle 
def pascal_triangle(n):
    triangle=[]
    for i in range(n):
        row=[1]

        if i>0:
            prev_row= triangle[i-1]
            for j in range(len(prev_row)-1):
                row.append(prev_row[j]+prev_row[j+1])
            row.append(1)
        triangle.append(row)

        print(" "*(n-i-1), end="")
        for num in row:
            print(num, end=" ")
        print()

pascal_triangle(5)


#11. single function calculator
'''
def calculator(a,b):
    return{
        "addition": a+b ,
        "subtraction": a-b,
        "multiplication": a*b,
        "division": a/b if b!=0 else " Can't divide by zero"
    }

result=calculator(10,5)
print(result)'''

def calculator(a,b):
    print(f"Addition: {a+b}")
    print(f"Subtraction: {a-b}")
    print(f"Multiplication: {a*b}")
    if b!=0:
        print(f"Division: {a/b}")
    else:
        print(f"Division: Can't divide by zero ")

calculator(23,11)