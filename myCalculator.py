#Get a experssion,returns true if expression is number (including negative) false otherwise
def is_numebr(expression):
    if isinstance(expression,int):
        return True
    if expression[0] == '-':
        myExpression = expression.replace('-','1')
        return myExpression.isdigit()
    return expression.isdigit()

#Main caluclautor
expression = input("To Add Two Numbers Press: +\nTo Subtract Two Numbers Press: -\nTo Add Multiply Numbers Press: *\n"
                   "To Divide Two Numbers Press: / \nTo Power Two Numbers Press: **\n")
#check for valid input
while expression != '+' and expression != '-' and expression != '*' and expression != '/' and expression != '**':
    print("This calculator don't support this expression\n")
    expression = input("Please, enter a valid input\n")
#gets two numbers, check for validation
num1 = input("Enter your first Num\n")
while not is_numebr(num1):
    print("This is not a number!\n")
    num1 = input("Please, enter a valid input\n")
num2 = input("Enter your second Num\n")
while not is_numebr(num2):
    print("This is not a number!\n")
    num2 = input("Please, enter a valid input\n")
#covert the input into int after validation
num1 = int(num1)
num2 = int(num2)
#adding
if expression == '+':
    num3 = num1 + num2
#subtracting
if expression == '-':
    num3 = num1 - num2
#multipication
if expression == '*':
    num3 = num1 * num2
#divide, if divider is zero, ask for another divider
if expression == '/':
    while num2 == 0 or not is_numebr(num2):
        print("Can't Divide in zero!\n")
        num2 = input("Please, enter a valid divider\n")
    num2 = int(num2)
    num3 = num1 / num2
#power, if both the base and the power are zero, ask for another base and power
if expression == '**':
    while (num2 == 0 and num1 == 0) or not is_numebr(num1) or not is_numebr(num2):
        print("Can't power zero in zero! change your input\n")
        num1 = input("Please, enter a valid base\n")
        num2 = input("Please, enter a valid power\n")
    num1 = int(num1)
    num2 = int(num2)
    num3 = num1 ** num2
print("Resulrt:",num3)