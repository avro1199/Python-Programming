#Id: 03
#Name: Avro Biswas

# Grading from score

score = int(input('Enter a Score:'))

if(score > 100 or score < 0):
    print('Invalid Score !')
elif(score >= 80):
    print('A')
elif(score >= 70):
    print('B')
elif(score >= 60):
    print('C')
elif(score >= 50):
    print('D')
else:
    print('F')