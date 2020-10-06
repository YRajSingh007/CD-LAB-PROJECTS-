def prefix():
    a = input("Enter the Prefix Expression: ")
    a = a[::-1] 
    l = []
    symbols = ['*', '/', '%', '+', '-'] 
    for i in a:
        if i in symbols:
            a = l.pop() 
            b = l.pop() 
            temp = a+b+i          
            l.append(temp)  
        else:                 
            l.append(i) 
    t="".join(l)
    print(t)
prefix()
        
output-> ab*c+
