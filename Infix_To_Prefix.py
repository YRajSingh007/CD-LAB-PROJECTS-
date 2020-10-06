def infix():
    m=[]
    p=input("Enter The Infix Expression: ")
    for i in range(len(p)):
        m.append(p[i])
    m=m[::-1]
    l1=[]
    l2=[]
    for i in m:
        if(ord(i)>=97 and ord(i)<=122):
            l1.append(ord(i))
        else:
            l2.append(ord(i))
    l2=l2+l1
    l3=[]
    for j in l2:
        l3.append(chr(j))
    t="".join(l3)
    print(t)
    
infix()

output-> +*cba
