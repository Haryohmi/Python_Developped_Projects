#convert decimal numver to binary
#binary is number / 2 = quotient 
#binary is number % 2 = remainder
#print each remainder
#repeat loop for /

number = int(input('Enter number'))


while number > 1:
    remainder = number % 2
    quotient = number / 2 
    print(remainder)
    number = quotient

    if number == 1 or number == 0:
        print(number)