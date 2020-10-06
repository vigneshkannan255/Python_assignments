#regular expression packages are imported
import re 
#get email address
n=input("Enter Your Mail:")
check=re.findall("(\w+)@gmail.com$",n)
#all emails will be stored in the check variable and it is printed
print(check)

