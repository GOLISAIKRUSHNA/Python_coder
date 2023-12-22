class Animal:
    all_property={
        "name":"kaloob tulein",
        "Roll":"32",
        "Address":"london"
    }

    All_list=["kane",'kalob tulein',"gully","sailu"]
    
    def del_method(self,name):
        self.All_list.remove(name)
        return self.All_list

    def apna_method(self):
        return self.All_list
    

    def simple(self,hii):
        self.All_list.append(hii)
        return self.All_list.sort
    @property
    def get_gully(self):
        
        return self.All_list[1]

hii=Animal()
# gu=hii.get_gully
# print("good teacher for python is",gu)
# print(hii.apna_method())
# print(hii.All_list)
# print(hii.apna_method())
# print(hii.del_method("sailu"))
# bye=hii.get_gully
# print(bye)

print(hii.simple("sailu"))
print(hii.All_list)

