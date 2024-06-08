from re import *

file = open('file.txt', 'r')
s = file.read()

# print(s)

regx = f'<td>([^<>]*)</td><td>Bolliger &amp; Mabillard</td>'
lst = findall(regx, s)

print(lst)