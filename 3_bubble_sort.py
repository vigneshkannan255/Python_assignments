# n is used to get input from user 
n=input('Enter Length of Array:')
l=[]
temp=0
for i in range(0,n):
	a=input('Enter',a[i] )
	l.append(a)
for i in range(0,n):
	for j in range(0,n-1-i):
		if(l[j]>l[j+1]):
			temp=l[j]
			l[j]=l[j+1]
			l[j+1]=temp
print(l)
