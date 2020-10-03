#regular expression packages are imported
import re 

n=input("Enter Your Mail:")
check=re.findall("(\w+)@gmail.com$",n)
print(check)

