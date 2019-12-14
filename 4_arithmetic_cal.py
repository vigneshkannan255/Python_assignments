a=0
while(a=0)
	choice=input('1.ADD\n2.SUB\n3.MUL\n4.DIV\n5.Exit')
	x=input('Enter A:')
	y=input('Enter B:')	
	if(choice == 1):
		print(x+y)
	elif(choice == 2):
		print(x-y)
	elif(choice == 3):
		print(x*y)
	elif(choice == 4):
		print(x/y)
	elif(choice == 5):
		a=1
	elif(choice > 5):
		print('choose any one of the above option')
	
