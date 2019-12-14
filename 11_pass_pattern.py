import re
n=input("Enter Your Password:")
check=re.findall("[a-z]{4}[0-9]{3}@",n)
if(check):
	print("valid Password")
else:
	print("invalid password")
