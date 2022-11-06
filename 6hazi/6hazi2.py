


def palindrom(text):
    return text == text[::-1]
if __name__ == "__main__":
    print("It is an English palindrom checker! Only use english words/text without dots/commas/exclamation mark!")
    text = input("Write a text or write words: ")
    k = palindrom(text)
    if k:
        print("Yes,it's a palindrom.")
    else:
        print("No, it is not a palindrom.")
