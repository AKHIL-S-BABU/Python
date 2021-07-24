

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

OUTPUT
Enter the size of the stack: 3

                        Enter the Following number to do the stack operation:


1) Push
2) Pop
3) Display
4) Exit :               2

                                Underflow!!

1) Push
2) Pop
3) Display
4) Exit :               1
Enter the number to push :10

1) Push
2) Pop
3) Display
4) Exit :               1
Enter the number to push :15

1) Push
2) Pop
3) Display
4) Exit :               1
Enter the number to push :20

1) Push
2) Pop
3) Display
4) Exit :               3
[10, 15, 20]

1) Push
2) Pop
3) Display
4) Exit :               1

                        OverFlow !!!

1) Push
2) Pop
3) Display
4) Exit :               4
    
    Thank You Happy Coding!
