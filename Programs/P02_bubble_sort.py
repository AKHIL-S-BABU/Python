from random import randint as rt
arr=[]
for i in range(10):
    arr.append(rt(0,100))
print("Array before sort:\n",arr)
def sorted(f,a,b):
    for i in range(a,b):
        for j in range(a,b):
            if(f[j]>f[j+1]):
                f[j],f[j+1]=f[j+1],f[j]
print("The array after bubble sort:\n",arr)
