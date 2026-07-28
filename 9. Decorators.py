def welcome(fun):
    def msg():
        print("Welcome")
        fun()
    return msg

@welcome
def student():
    print("Shrikrushna - MIT ADT")

student()
