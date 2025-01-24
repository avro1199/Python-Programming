#Id: 03
#Name: Avro Biswas

# Calculate sum of first n natural numbers

n = int(input('Enter the value of N:'))

# Method 01
# sum = int(n*(n+1)/2)

# Method 02
sum = 0
for num in range(1, n+1):
    sum += num

print(sum)
