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
