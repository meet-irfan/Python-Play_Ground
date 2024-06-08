# Create the calculator Program
#take a input for user :
first = int(input("Take a first Number:"))
#select the operator :
operator = input(" Enter the operational (+/-% ): " )
#take second input :
second = int(input("Take a sencod Number: "))

if operator == "+":
    print(first + second)
elif operator == "-":
        print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "%":
    print(first % second)
elif operator == "/":
    print(first / second)

else:
    print("Sorry ")



