while True:
    Addition = ("+")
    Subtraction = ("-")
    Multiplication = ("*")
    Division = ("/")

    print("Select your Calculation process:")
    print(" + ")
    print(" - ")
    print(" * ")
    print(" / ")
    print("Enter e or E to exit ")
    Select = input("Enter your Calculation process : ")
    if Select == "e" or Select == "E":
        break
    num1 = float(input("Put the first number: "))
    num2 = float(input("Put the second number: "))

    if Select == "+":
        print(num1, "+", num2, "=", (num1+num2))

    elif Select == "-":
        print(num1, "-", num2, "=", (num1-num2))

    elif Select == "*":
        print(num1, "*", num2, "=", (num1*num2))

    elif Select == "/":
        if num2 == 0:
            print("ERROR")
    else:
        print(num1, "/", num2, "=", (num1/num2))
else:
    print("The Calculation process is Not Nounded")
