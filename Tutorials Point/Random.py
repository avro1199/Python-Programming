try:
	f = open("rj.txt", 'w')

	print(type(f),end="\n")

	for i in range(1,11,3):
		for j in range(1, 11, 2):
			print(i, j, " Rj Avro", sep="~", end= "\n\n", flush= False, file = f)
finally:
	print(type(i))
	f.close()