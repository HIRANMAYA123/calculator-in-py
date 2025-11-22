print("Welcome to the swimple python calculator!")
print("Please select your desired calculation:")
print("1-Add")
print("2-Subtract")
print("3-Multiply")
print("4-Divide")
while True:
    choice=input("Enter choice 1/2/3/4:")
    if choice in ('1', '2', '3', '4'):
        try:
            num1=float(input("Enter first number-"))
            num2=float(input("Enter second number-"))
        except ValueError:
            print("Invalid input")
            continue
        if choice=='1':
            result=num1+num2
            print(f"{num1}+{num2}={result}")
        elif choice=='2':
            result=num1-num2
            print(f"{num1}-{num2}={result}")
        elif choice=='3':
            result=num1*num2
            print(f"{num1}*{num2}={result}")
        elif choice=='4':
            if num2==0:
                print("error")
            else:
                result=num1/num2
                print(f"{num1}/{num2}={result}")
        next_calculation=input("Do you want to perform another calculation?yes/no-")
        if next_calculation.lower()=="no":
            print("Thanks for using the calculator")
            break
    else:
        print("Invalid Input-Please enter a choice between 1 and 4")
