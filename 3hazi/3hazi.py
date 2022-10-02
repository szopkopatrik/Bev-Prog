


def triangle(a,b,c):

    if a < b + c and b < a + c and c < a + b:
        print("A", a ,",", b, "és", c ,"oldaú háromszög szerkeszthető.")
    else:
        print("A", a ,",", b, "és", c ,"oldaú háromszög NEM szerkeszthető.")
if __name__ == "__main__":
    
    print("Adja meg a háromszög 3 oldalát cm-ben:")
    a = int(input("a oldal (cm): "))
    b = int(input("b oldal (cm): "))
    c = int(input("c oldal (cm): "))

    triangle(a, b, c)
