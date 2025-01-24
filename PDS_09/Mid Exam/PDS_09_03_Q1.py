#Id: 03
#Name: Avro Biswas

# Find largest number among three user-provided inputs

a = int(input('Enter the first Number:'))
b = int(input('Enter the second Number:'))
c = int(input('Enter the third Number:'))

# largest = max(a, b, c)
largest = 0

if a >= b:
    if a >= c:
        largest = a
    else:
        largest = c
else:
    if b >= c:
        largest = b
    else:
        largest = c

print(f'\nThe largest is: {largest}')

