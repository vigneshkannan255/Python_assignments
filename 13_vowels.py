f=open('a.txt','r') #a.txt (filename)
total=0
for line in f.read():
    #below line is check the character is vowel or not
    if(line=='a' or line=='e' or line=='i' or line=='o' or line=='u' or line=='A' or line=='E' or line=='I' or line=='O' or line=='U'):
        total+=1
f=open('a.txt','a')
f.write('Number of vowels in the file :'+str(total))
f.close()
