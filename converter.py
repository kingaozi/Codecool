print("Welcome to my binary and decimal number converter.")
print("By entering the number you choose, you must first enter the number you chose, " +\
 "and type the second number as 10 for decimal or 2 for binary numbers. \n" )

while True:
    while True:
        try:                                                    #split - to split two numbers in input
            number1, number2 =map(int, input("Enter two numbers: ").split()) #number1 - chosen number
            break                                              #number2 - 2 for binary, 10 for decimal
        except ValueError: #letter
            print("You can't use letters!")

    while number2 != 2 and number2 !=10: #repeat until number2 will be 2 or 10
        if number2 != 2 :
            print("The second number should be 2 or 10")
            number1, number2 =map(int, input("Enter two numbers: ").split())  
        if number2 != 10:
            print("The second number should be 2 or 10")
            number1, number2 =map(int, input("Enter two numbers: ").split())
    
                         
    if number2 == 10: 
        def converted_to_binary(number1):
            if number1 > 1:
                converted_to_binary(number1//2) #floor division
            print(number1 % 2, end = '')

        converted_to_binary(number1)
        print(" " , "2")

    elif number2 == 2:
        converted_to_decimal = int(str(number1), 2)
        print(converted_to_decimal, " " , "10")
