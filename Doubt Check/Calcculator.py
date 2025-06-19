print('Enter first number:')
first_number = float(input())
print('Enter second number:')
second_number = float(input())

print('Enter the operation you want to perform (+, -, *, /, %, //):')
operation = input()

if operation == '+':
    result = first_number + second_number
elif operation == '-':
    result = first_number - second_number
elif operation == '*':
    result = first_number * second_number
elif operation == '/':
    if second_number == 0:
        result = 'Error: Division by zero is not allowed.'
    else:
        result = first_number / second_number
elif operation == '%':
    result = first_number % second_number
elif operation == '//':
    result = first_number // second_number
else:
    result = 'Invalid operation'


print('The result is:', result)