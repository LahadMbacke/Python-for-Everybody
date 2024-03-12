expression =[ "235 + 52","223 - 34"]


for op in expression:

    # Split the expression into operands and operator
    operands = op.split()
    num1 = int(operands[0])
    operator = operands[1]
    num2 = int(operands[2])

    # Calculate the maximum length of the formatted numbers and operator
    max_length = max(len(str(num1)), len(str(num2)), len(operator))

    # Print the formatted expression and result
    print(f"{num1:>{max_length}}")
    print(f"{operator} {num2:>{max_length}}")
    print(f"{'-' * (max_length + 2)}")
