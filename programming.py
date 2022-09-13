#1. Write a Python Program to Find LCM?



number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
if number_1 > number_2:
    greater = number_1
else:
    greater = number_2
while(True):
    if((greater % number_1 == 0) and (greater % number_2 == 0)):
        lcm = greater
        break
    greater += 1
print("LCM of",number_1,"and",number_2,"=",greater)


#2. Write a Python Program to Find HCF?


number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if number_1 > number_2:
    minimum = number_2
else:
    minimum = number_1

for i in range(1, minimum+1):
    if((number_1 % i == 0) and (number_2 % i == 0)):
        hcf = i
print("hcf/gcd of",number_1,"and",number_2,"=",hcf)


#3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

def DecimalToOther():
    num = int(input('Enter a Number: '))
    print(f'Binary Number -> {bin(num)}')
    print(f'Octal Number -> {oct(num)}')
    print(f'Hexadecimal Number -> {hex(num)}')

DecimalToOther()


#4. Write a Python Program To Find ASCII value of a character?


def charToAscii():
    char = input('Enter a Character: ')
    if len(char) > 1:
        print('Please Enter a Single Character')
    else:
        print(f'Ascii Character of {char} is {ord(char)}')

charToAscii()


#5. Write a Python Program to Make a Simple Calculator with 4 Basic Mathematical operations ?


import operator

ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

print('Select a Arithmetic Operation: \
        \n1.Addition(+)\
        \n2.Division(-)\
        \n2.Multiplication(*)\
        \n4.Division(/)\
        \n3.Stop(0)\n')

while True:
    operator = input('Enter a arithmetic operation -> ')
    if operator == '0':
        print("Program Stopped successfully")
        break
    elif operator not in ['+', '-', '*', '/']:
        print("Please enter a valid operator")
    else:
        num_1 = int(input('\nEnter 1st Number: '))
        num_2 = int(input('Enter 2nd Number: '))
        print(f'{num_1}{operator}{num_2}={ops[operator](num_1, num_2)}\n')





