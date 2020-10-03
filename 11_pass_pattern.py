import re
#this program check password is valid or not
n=input("Enter Your Password:")
check=re.findall("[a-z]{4}[0-9]{3}@",n)
if(check):
	print("valid Password")
else:
	print("invalid password")
