

arr=[]
top=-1
size=int(input("Enter the size of the stack: "))
k=0
print("\n\t\t\tEnter the Following number to do the stack operation:\n")
while(k!=4):
    
    k=int(input("\n1) Push\n2) Pop\n3) Display\n4) Exit : \t\t"))
    if k==1:
        if top==size-1:
            print("\n\t\t\tOverFlow !!!")
            
        else:
            top+=1
            arr.append(int(input("Enter the number to push :")))
    elif k==2:
        if top==-1:
            print("\n\t\t\t\tUnderflow!!")
            
        else:
            print("\tThe popped element: ",arr[top])
            arr.pop(top)
            top-=1
    elif k==3:
        print(arr)
    else:
        break
