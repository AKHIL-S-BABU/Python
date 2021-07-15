
#Suresh knows binary numbers very well. Unfortunately ,he forgot his bank account password , 
#but he remembered a number and if we reverse the binary digits of that number we will get his password.
#Help suresh to find his password. You will be given a variable name n which is a no of passwords 
#to find followed by n space separated numbers.You are required to give as output and passwords showing for each number.
#For Example , if n is 3 and numbers 35000,3467,94856 , you are expected to give as output 487653376, 3517972480 and 290357248.



def calc(k):
    b=0
    sum=0
    i=0
    p=32
    arr=[]
    while(i<32):
        if(k>0):
            r=int(k%2)
            arr.append(r)
            k=int(k/2)
        else:
            arr.append(0)
        sum=sum+(int(arr[b])*(2**(p-1)))
        p-=1
        b+=1
        i+=1
    return sum

n=int(input("Enter an Intiger: "))
lst=input("\nEnter numbers: ").split()
for i in range(n):
    #print(int(lst[i])+1)
    print("password",i+1,':',calc(int(lst[i])))
