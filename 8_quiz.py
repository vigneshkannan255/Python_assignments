n=int(input('Enter number of student:'))
for i in range(n):
	f=open('s_00'+str(i),'a')
	print("question1\na\nb\nc")
	f.write('1,'+input()+'\n')
	print("question2\na\nb\nc")
	f.write('2,'+input()+'\n')
	print("question3\na\nb\nc")
	f.write('3,'+input()+'\n')
	print("question4\na\nb\nc")
	f.write('4,'+input()+'\n')
	print("question5\na\nb\nc")
	f.write('5,'+input()+'\n')
	f.close

k=open('key.txt','r')
c=0
r=open('result.txt','w')
for j in range(0,n):
	s=open('s_00'+str(i),'r')
	for i in range(1,6):
		if(k.readline() == s.readline()):
			c+=1
	r.write('s_00'+str(j)+'-'+str(c))
k.close()
s.close()
r.close()
