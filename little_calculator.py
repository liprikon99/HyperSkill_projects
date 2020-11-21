first_number = float(input())
second_number = float(input())
arithmetic_operation = input()
if second_number == 0.0 and arithmetic_operation in '/ , mod, div':
    print("Division by 0!")
else:
    if arithmetic_operation == '+':
        print(first_number + second_number)
    elif arithmetic_operation == '-':
        print(first_number - second_number)
    elif arithmetic_operation == '/':
        print(first_number / second_number)
    elif arithmetic_operation == '*':
        print(first_number * second_number)
    elif arithmetic_operation == 'mod':
        print(first_number % second_number)
    elif arithmetic_operation == 'pow':
        print(first_number ** second_number)
    elif arithmetic_operation == 'div':
        print(first_number // second_number)
