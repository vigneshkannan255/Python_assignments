x=0
ll=[]
while x==0:
    print("1.ADD\n2.VIEW\n3.EXIT")
    n=int(input("Enter Choice:"))
    e=[]
    if n==1:
        f=input("First Name:")
        e.append(f)
        l=input("Last Name:")
        e.append(l)
        d=input("DD-MM-YYYY:")
        e.append(d)
        i=f+l[0]+d[6:]
        e.append(i)
        ll.append(e)
    elif n==2:
        eid=input("Enter Employee ID:")
        for j in range(0,len(ll)):
                if(ll[j][3] == eid):
                    print("First Name:"+ll[j][0] +"\nLast Name:"+ll[j][1]+ "\nDOB:"+ll[j][2]+ "\nid:"+ll[j][3])

    elif n==3:
        x=1    
