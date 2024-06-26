#calculation operations 
def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

##exception error when zero division is performed
def divide(a, b):
    try:
        return a/b
    except Exception as e:
        print(e)

def power(a, b):
    return a**b

def remainder(a, b):
    return a % b
#Finding pat calculations 
calc_history = []
def record_history(args):
    calc_history.append(args)

def history():
    if calc_history == []:
        print("No past calculations to show !")
    else:
        for i in calc_history:
            print(i)

## defined the select option and check with almost all the possiblities


def select_op(choice):
    if (choice == '#'):
        return -1
    elif (choice == '$'):
        return 0
    elif (choice in (' + ', ' - ', ' * ', ' / ', ' ^ ', ' % ')):
          # taking the 1st number for the user and making sure it is a number
        while (True):
            num1s = str(input("Enter first number : "))
            print(num1s)
            if num1s.endswith('$'):#to check $ symbol there to reset
                return 0
            if num1s.endswith('#'):#to check # symbol there to exit
                return -1
            try:
                num1 = float(num1s)
                break
            except:
                print("Ivalid number !, please enter again !")
                continue

        while (True):
            num2s = str(input("Enter second number : "))
            print(num2s)
            if num2s.endswith('$'):#to check $ symbol there to reset
                return 0
            if num2s.endswith('#'):#to check # symbol there to exit
                return -1
            try:
                num2 = float(num2s)
                break
            except:
                print("Ivalid number ! , please enter again !")
                continue

        result = 0.0
        last_calculation = ""
        if choice == '+':
            result = add(num1, num2)
            calc_history.extend(last_calculation)
        elif choice == '-':
            result = subtract(num1, num2)
        elif choice == '*':
            result = multiply(num1, num2)
        elif choice == '/':
            result = divide(num1, num2)
        elif choice == '^':
            result = power(num1, num2)
        elif choice == '%':
            result = remainder(num1, num2)
        else:
            print("Something Went Wrong !")

        last_calculation = "{0} {1} {2} = {3}".format(num1, choice, num2, result)
        print(last_calculation)
        record_history(last_calculation)

    elif choice == '?':
        history()    
        #calc_history.extend(last_calculation)

    else:
        print("Unrecognized operation")

while True:
    print("Select operation.")
    print("1.Add      : + ")
    print("2.Subtract : - ")
    print("3.Multiply : * ")
    print("4.Divide   : / ")
    print("5.Power    : ^ ")
    print("6.Remainder: % ")
    print("7.Terminate: # ")
    print("8.Reset    : $ ")
    print("8.History  : ? ")

    # take input from the user
    choice = input("Enter choice( + , - , * , / , ^ , % , # , $ , ? ): ")
    print(choice)
    if select_op(choice) == -1:
        #program ends here
        print("Done. Terminating")
        break