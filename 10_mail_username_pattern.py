#regular expression packages are imported
import re 
#get email address
n=input("Enter Your Mail:")
check=re.findall("(\w+)@gmail.com$",n)
print(check)

