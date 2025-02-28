

# Function to get number input from User
def getNumberInput():
    num = input("\nInput a number:\n")
    return num



#The main function that runs
def performCalculation():
    
    currentValue = float(getNumberInput())


    # Loop until specific input from user have been received
    while(True):
        operation = input("\nChoose operator by writing (+, -, *, /), if done write nothing:\n")

        if operation == "":
            break

        
        # Switch case on operation to perform different actions based on input
        match operation:
            case "+":
                newNumber = float(getNumberInput())
                currentValue += newNumber
            case "-":
                newNumber = float(getNumberInput())
                currentValue -= newNumber
            case "*":
                newNumber = float(getNumberInput())
                currentValue *= newNumber
            case "/":
                newNumber = float(getNumberInput())
                currentValue /= newNumber
            case _:
                print("Invalid input")


        print(f'\nCurrent Total is: {currentValue}')
    
    print(f'\nTotal equals: currentValue {currentValue}')





if __name__ == "__main__":
    performCalculation()
    
