#Basic Calculator

again = "Y"
while again.upper() != "X":
    operation = input("Name the operation you would like to conduct (add, sub, mult, div): ").strip()
    while operation != "add" and operation != "sub" and operation != "mult" and operation != "div":
        print ("invalid input")
        operation = input("Name the operation you would like to conduct (add, sub, mult, div): ").strip()
    a = float(input(("Enter the first number: ")))
    b = float(input(("Enter the second number: ")))
    if operation.upper() == "ADD":
        result = float(a + b)
        print ("The result is",result)
    elif operation.upper() == "SUB":
        result = float(a - b)
        print ("The result is",result)
    elif operation.upper() == "MULT":
        result = float(a*b)
        print ("The result is",result)
    elif operation.upper() == "DIV":
        result = float(round((a/b),2))
        print ("The result is",result)
    again = input("Enter X to quit or any key to continue: ").strip()
