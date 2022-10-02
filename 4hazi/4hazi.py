


def hanyados(a,b):

    try:
        hanyadoss = a / b
        print(hanyadoss)

    except ZeroDivisionError:

        print("Division by zero not allowed")
    
    print("Out of try except blocks")
    

if __name__ == "__main__":

    while True:
        a = int(input("Ente 'a' value: "))
        b = int(input("Ente 'b' value: "))

        hanyados(a,b)
