class Test:
    def __init__(self,name,grade):
        self.__name=name
        self.grade=grade
        self.msg = self.__name + " get " +self.grade 
    @property    
    def method(self):
        return self.__name + " got " + self.grade
    @method.setter
    def method(self,sent):
       name,grade = sent.split(' ')
       self.__name = name
       self.grade = grade
    @method.deleter
    def method(self):
        del self.grade

s1=Test("vijay","B")
print(s1.msg)
print(s1._Test__name)
s1.grade="A2"
print(s1.msg)
print(s1.method)
s1.method="vk A"
print(s1.method)
s1.method
print(s1.method)
