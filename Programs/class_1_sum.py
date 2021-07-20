
#Class Introduction
#program to add,multiplicate,division using class function


class calc:
    def __init__(self,aame,bame):
        self.a=aame #just to know that you dont have to use self.a=a all the time
        self.b=bame
        
    def add(self):
        ad=self.a+self.b
        print("Sum is ",ad)
        
    def mul(self):
        mul=self.a*self.b
        print("Multi is ",mul)
        
    def div(self):
        div=self.a/self.b
        print("Div is ",div)

sample=calc(4,6)
sample.add()
sample.mul()
sample.div()


#output:
Sum is  10
Multi is  24
Div is  0.6666666666666666
