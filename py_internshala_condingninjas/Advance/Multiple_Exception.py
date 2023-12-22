num=input()
num2=input()
try: 
    num=int(num)
    num2=int(num)
    total=num/num2
    # print(NameError)
except ZeroDivisionError:
    print("zero divion bro")
# except ValueError:
#     print("abc input error value error")
# except NameError:
#     print("simple error")asd

except Exception as e:
    print("error in above")
    print("error caught with exception")
    print(type(e))
 
    