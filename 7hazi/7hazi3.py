


def destroy():
    lines = []
    with open("hazi.txt", "r", encoding="UTF-8") as file:
        lines = file.readlines()

    with open("hazi.txt", "w", encoding="UTF-8") as file:
        for line in lines:
            if not line.isspace():
                file.write(line)

    mgh = ['a', 'á', 'e', 'é', 'i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű', 'y']
    irj = ['.', ',', '-', '!', '"', '?', '!', '(', ')']
    darabolt = []
    for k in range(len(lines)):
        lines[k] = lines[k].lower()

    for k in lines:
        for i in k:
            if i not in mgh:
                darabolt += i
    darabolt2 = []
    for s in darabolt:
        if s not in irj:
            darabolt2 += s

    darabolt3 = ''.join(darabolt2)

    with open("hazi.txt", "w", encoding="UTF-8") as file:
        file.write(darabolt3)
    
if __name__ == "__main__":
    destroy()