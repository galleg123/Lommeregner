


def getNumberInput():
    num = input("\nInput a number:\n")
    return num

def performCalculation():
    
    currentValue = float(getNumberInput())

    while(True):
        operation = input("\nChoose operator by writing (+, -, *, /), if done write nothing:\n")

        if operation == "":
            break


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
    
