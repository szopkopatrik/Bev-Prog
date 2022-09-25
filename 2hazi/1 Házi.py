


def betuk_gyakorisaga(name):
    
    words = {}

    for i in range(len(sentence)):
        if sentence[i] != " ":
            if sentence[i] not in words:
                words[sentence[i]] = 1
            else:
                words[sentence[i]] += 1
        else:
            continue
    
    print(words)

def fordito(name):

    szavak = sentence.split()

    szavak = list(reversed(szavak))

    print(" ".join(szavak))
    
def in_list(name):

    lista = sentence.split()

    print(lista)
            
    
if __name__ == "__main__":
    
    sentence = input("Adjon meg egy mondatot: \n")

    print("Betűk gyakorisága: ")
    betuk_gyakorisaga(sentence)
    
    print("Fordítva: ")
    fordito(sentence)

    print("Listába rendezve szavanként: ")
    in_list(sentence)
