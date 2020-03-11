def to_roman(x):

	output = ''

	output += (x // 100)*'C'

	if x % 100 >= 90:
		output += 'XC'
	else:
		output +=  ((x % 100) // 50)*'L'

		if x % 50 >= 40:
			output += 'XL'

	if ((x % 50) // 10) <= 3:
		output += 'X' * ((x % 50) // 10)

	if (x % 10) == 9:
		output += 'IX'
	elif (x % 10) == 4:
		output += 'IV'
	elif (x % 10) >= 5:
		output += 'V'
	if (x % 5) < 4:
		output += 'I'*(x%5)

	#output += 'X' * ((x % 50) // 10)

	#output += (x % 100 >= 50)*'L'

	#output += ((x % 50) // 10)*'X'

	return output

N = 200

for n in range(N):
	print('{}: {}'.format(n, to_roman(n)))