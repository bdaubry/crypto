from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    new_text = ''
    keyind = 0
    for i in range(len(text)):
        if text[i].isalpha():
            new_text = new_text + rotate_character(text[i], alphabet_position(key[keyind % len(key)]))
            keyind += 1
        else:
            new_text = new_text + text[i]
    return new_text

def main():
    from sys import argv
    phrase = input("Type a message:\n")
    try:
        print(encrypt(phrase,argv[1]))
    except IndexError:
        key = input("Key:\n")
        print(encrypt(phrase,key))

if __name__ == "__main__":
    main()