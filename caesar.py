from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    #takes a text input and encrypts it into a new string (new_text), which is returned
    new_text = ''
    for i in range(len(text)):
        #goes character by character, using the rotate_character function to rotate a letter 
        #from text and add it to new_text
        new_text = new_text + rotate_character(text[i], rot)
    return new_text

def main():
    phrase = input("Type a message:\n")
    rot = int(input("Rotate by:\n"))
    print(encrypt(phrase,rot))

if __name__ == "__main__":
    main()