def main():
    code=input("Enter The Code: ")       #Code has to be separated with space
    l=code.split(" ")
    #splits String Into List
    keywords=["and","for","if","else","else if","break","int","float","char","while","continue","sizeof","long","return","switch"]  
    #keyswords array
    operators=["+","-","/","=","<",">","++","--","&",">=","<=","!=","%"]
    #operators array
    separators=[",",";"]
    for i in l:
    #for loop to find tokens
        if(i in keywords):
            print(i," is a Keyword")
        elif(i in operators):
            print(i," is an Operator")
        elif(i in separators):
            print(i," is a Separator")
        else:
            print(i," is an Identifier")
main()

#sample array
Enter The Code: int a = b + c ;                                                                                                                 
int  is a Keyword                                                                                                                               
a  is an Identifier                                                                                                                             
=  is an Operator                                                                                                                               
b  is an Identifier                                                                                                                             
+  is an Operator                                                                                                                               
c  is an Identifier                                                                                                                             
;  is a Separator 
