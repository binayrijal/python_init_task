class maths:
    def _init_(self,first, second):
        self.first=first
        self.second=second
        print("the first"+self.first+"the second"+self.second+"numbers")
    def add(self):
        sum=self.first+self.second
        print("the sum is"+str(sum)) 
v1=maths(5,6)
v1.add()           
