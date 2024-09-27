print("HeipäHei!") #AkiR-a

def hello(n):
    if n == 1:
        print("")
        return 1
    else:
        print("Hei!", end=" ")
        return hello(n - 1)

hello(4)
