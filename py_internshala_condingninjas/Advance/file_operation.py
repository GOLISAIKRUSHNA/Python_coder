# with open("hii.txt","r") as file:
#     bro=file.read()
#     print(bro)


# with open("new.txt","a") as file:
#     file.write("\nwelcome to py world\n")
#     file.write("This is 2 Line\n")
#     file.write("\t\tThis is third line the file")


# with open("chal.txt","r") as chal:
#     # print(file.read())
#     new =chal.readlines()

# for there in new:
#     if "gmail"in there:
#         print(there)
#         print(chal)



filename=input("enter the filename")

content=input("contents:")

with open(filename,"w") as file:
    file.write(content)

yes_no=input("y or n")
if yes_no=="y":
    with open(filename,"r")as file:
        print(file.read())




