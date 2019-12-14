import re 

n=input("Enter Your Mail:")
check=re.findall("[a-z0-9]@gmail.com$",n)
if(check):
	print("valid mail address")
else:
	print("invalid mail address")

