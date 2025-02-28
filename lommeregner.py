

# Function to get number input from User
def getNumberInput():
    try:
        num = float(input("\nInput a number:\n"))
    except:
        print("Not a number")
        num = getNumberInput()
    return num



#The main function that runs
def performCalculation():
    
    currentValue = getNumberInput()


    # Loop until specific input from user have been received
    while(True):
        operation = input("\nChoose operator by writing (+, -, *, /, sqrt, ^), if done write q:\n")

        if operation == "q":
            break

        
        # Switch case on operation to perform different actions based on input
        match operation:
            case "+":
                newNumber = getNumberInput()
                currentValue += newNumber
            case "-":
                newNumber = getNumberInput()
                currentValue -= newNumber
            case "*":
                newNumber = getNumberInput()
                currentValue *= newNumber
            case "/":
                newNumber = getNumberInput()
                currentValue /= newNumber
            case "sqrt":
                currentValue = currentValue ** 0.5
            case "^":
                newNumber = getNumberInput()
                currentValue = currentValue ** newNumber
            case _:
                print("Invalid input")


        print(f'\nCurrent Total is: {currentValue}')
    
    print(f'\nTotal equals: {currentValue}')





if __name__ == "__main__":
    performCalculation()
    
