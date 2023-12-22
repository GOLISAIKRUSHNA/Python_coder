class Animal:

    def cat(self):
        print("i am cat of animal")
    def rabbit(self):
        print("i am a parent class of Animal")
    def gazelle(self,Name="dear"):
        print("i am a animal",Name)

class Bird(Animal):
    pass
    def cat(self):
        print("i am new cat of bird")
    def rabbit(self):
        super().rabbit()
    def gazelle(self,Name="dear"):
        super().gazelle(Name)
        print(Name,"was caught")
        
    
hiii=Bird()
# hiii.cat()
# hiii.rabbit()

hiii.gazelle("fox")