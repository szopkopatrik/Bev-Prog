



def atvalto(a, b):

    a = int(a)
    
    if b == "cm":
        print(round(a * 0.39, 2),"inches")
        
    elif b == "inch":
        print(round(a * 2.54, 2),"cm-es")
        
    elif b != "cm" or "inch":
        print("Not correct unit!")

if __name__ == "__main__":
    
    a, b = input("Adjon meg egy számot és egy mértékegységet (cm/inch): \n"), input()

    atvalto(a, b)
