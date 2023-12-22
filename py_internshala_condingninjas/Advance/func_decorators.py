
def my_decorators(fink):
    def hiii():
        print('chalu')
        fink()
        print("khatam")
    return hiii


@my_decorators
def func():
    print("My name is Saikrushna Goli")

func()