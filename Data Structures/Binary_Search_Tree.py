#Pytyhon program to implenement a Binay seach Tree 


class bst: 
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

        # This func is used to add child nodes to the tree
        #Since this is a binary search three elements are to added based on their value
        #thus i used (value<data) for poninting towards left side and (value>data ) to point towards right side
    def adchild(self,data): 
        if(data==self.data):
            return
        if(data<self.data):
            if(self.left):
                self.left.adchild(data)
            else:
                self.left=bst(data)
        else:
            if(self.right):
                self.right.adchild(data)
            else:
                self.right=bst(data)
     
     #INORDER traversel is one of the three traversal methods 
      # here            
    def inorder(self):
        el=[]
        if(self.left):
            el=el+self.left.inorder()
        el.append(self.data)
        if(self.right):
            el+=self.right.inorder()
        return el
      
    def search(self,d):
        if(d==self.data):
            return "found"
        if(d<self.data):
            if(self.left):
                return self.left.search(d)
            else:
                return "Not found"
        if(d>self.data):
            if(self.right):
                return self.right.search(d)
            else:
                return "Not found"
              
#     def build(el):          #This is to insert values in the BST with a array
#         r=bst(el[0])
#         for i in range(1,len(el)):
#             r.adchild(el[i])
#         return r

a=bst(17)
a.adchild(4)
a.adchild(1)
a.adchild(20)
a.adchild(23)
a.adchild(9)
a.adchild(23)
a.adchild(18)
a.adchild(34)


print(a.inorder())
print(a.search(1))


#           ******** OUTPUT  **********
#           [1, 4, 9, 17, 18, 20, 23, 34]
#           found











