print('what is your problem?\n')

response = str(input('Enter response: '))

print('Have you had this problem before \n')

print ('1.Yes\n2.No?\n')
response = int(input('Enter option: '))

match response:
	case 1:
		print('Well you have it again')
	case 2:
		print('Well you have it now')

