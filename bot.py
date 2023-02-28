def mathbot():
    user=input("User:")
    while True:
        operator = input("Bot: What mathematical operation do i want to do? \n User:")
        operand1 = 0
        operand2 = 0
        result = 0
        flg = False

        if operator != '+' and operator !='add' and operator !='addition' and operator != '-' and operator !='subtract' and operator !='subraction' and operator != '/' and operator !='divide' and operator !='division' and operator != '*'  and operator !='multiply' and operator !='multiplication':
            print("Bot: Sorry, I don't understand that operation. Please try again.")
        else:
            # Get user input
            operand1 = input("Bot: Enter first operand: ")
            operand2 = input("Bot: Enter second operand: ")
            
            # Calculate result
            if operator == '+' or operator =='add' or operator =='addition':
                result = float(operand1) + float(operand2)
            elif operator == '-' or operator =='subtract' or operator =='subraction':
                result = float(operand1) - float(operand2)
            elif operator == '*' or operator =='multiply' or operator =='multiplication' :
                result = float(operand1) * float(operand2)
            elif operator == '/' or operator =='divide' or operator =='division':
                if operand2 == '0':
                    flg = True
                    print("Bot: Cant be 0, enter valid operand!")
                else:
                    result = float(operand1) / float(operand2)

            # Show result
            if flg == False:
                print("Bot:", result)

        # Check if user wants to perform another operation
        another_operation = input("Bot: Would you like to perform another operation? (yes/no): \n User:")
        if another_operation.lower() in ["no", "n"]:
            print("Bot:Thank You...")
            break


mathbot()
