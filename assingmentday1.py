#multiplication table
"""
n=int(input('Enter a number: '))
print('Multiplication table')
for i in range(1,10):
    print(n,'*',i,'=',i*n)
    
"""    

#Counting vowels and consonants
'''
v=['a','e','i','o','u','A','E','I','O','U']
vow=0
c=0
s=str(input('Enter a string: '))
for i in range (len(s)):
    if s[i] in v :
        vow=vow+1
    elif s[i]!=' ':
        c=c+1
    else:
        c=c
print('Number of vowels:',vow)
print('Number of consonants:',c)

'''
 
#Dictionary
'''
from PyDictionary import PyDictionary
dictionary = PyDictionary()
while True:
       wrd = input('Enter a word: ')
       m = dictionary.meaning(wrd)
       print(f"Meaning of '{wrd}':\n{m}")
       c=int(input('Enter 1 to continue,2 to exit: '))
       if c==2:
             break
'''

#Calculator
'''
class Calculator:
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        if y == 0:
            return "Cannot divide by zero"
        return x / y

calc = Calculator()

while True:
    print("Calculator")
    print("1.Addition  2.Subtraction  3.Multiplication  4.Division  5.Exit")
    c= int(input("Enter choice: "))

    if c==5:
        break
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if c==1:
             print('Sum of the two numbers: ',calc.add(num1, num2))
        elif c ==2:
            print('Difference=',calc.sub(num1, num2))
        elif c==3:
            print('Product=',calc.mul(num1, num2))
        elif c==4:
            print('Quotient=',calc.div(num1,num2))
        
        else:
            print("Error")
            
'''
        