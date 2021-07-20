class calc:
    def __init__(self,aame,bame):
        self.a=aame
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
