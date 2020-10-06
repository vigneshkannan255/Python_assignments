#regular expression packages are imported
import re
a='Poorani1ko23'
#finding all alpha char in a & storing in match
match=(re.findall("\D+",a))
#finding all digits in a & storing in match1
match1=(re.findall("\d+",a))
#match,match1 will be a list so we are using *operator to separate by space
print(*match,*match1)

