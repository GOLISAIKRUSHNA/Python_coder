class Animal:

    animal_type =" noname"
    def __init__(self,give="sai"):
        self.hiii=give
        print("Reached Animal name",self.hiii)
        # print(give)
       
    def name(self):
        print("getting from animal __inti__:",self.hiii)



class New(Animal):

    def __init__(self, give):
        print(give)
        super().__init__(give)
        print("now it is new class")
        self.animal_type="New"
        print(self.animal_type)


hii=New("method")
hii.name()
