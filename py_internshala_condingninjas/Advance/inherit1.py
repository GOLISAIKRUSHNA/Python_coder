class inherit1:
    first_change="Orange"

    def speak(self):
        print("rawwwrrr")

    def cat(self):
        print("meow")

class baffalo(inherit1):
    first_change="white"
    def speak(self):
        print("abbaaaa..")

class new(baffalo):
    first_change="pink"

    def speak(self):
        return super().speak()
    
ajja=new()
ajja.speak()
print(ajja.first_change)


