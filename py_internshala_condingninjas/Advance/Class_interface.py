class Animal:
    a=10
    b=20
    def chase(self):
        raise NotImplementedError
    def eat(self):
        raise NameError
    def bye(self):
        print(self.a+self.b)
    kavita="krishna"
    
    
class new(Animal):
    attri_properties="overwrite data changes from 1class to 2class"
    see="same data use in parent and child class"
    def chase(self):
        print("chase function")
    def eat(self):
        print("eatfunction")
        return super().bye()

hii=new()
# hii.chase()
# hii.eat()
# hii.chal
hii.eat()
print(hii.kavita)
print("done with class and inheritance and class interface")
