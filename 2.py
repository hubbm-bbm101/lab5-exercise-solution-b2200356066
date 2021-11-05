n=input("Write your e-mail: ")
def x(a):
    if "@" in a and "." in a:
        return True

def y():
    try:
        if x(n)==True:
            print("Your mail is valid")
    except:
        print("Your mail is invalid")
y()        