def alphabet_position(letter):
    #takes a letter as input, turns it lowercase, and finds the number using the ord function. 
    #since we're trying to use A = 0, B = 1, etc, we have to subtract 97 so that the returned number 
    #is correct.
    letter = letter.lower()
    letter_num = ord(letter) - 97
    return letter_num

def rotate_character(char, rot):
    #rotates a single character by a custom 'rot', or rotation value
    new_char = ''
    if char.isalpha() == True:
        #if the character is an alphabetic character, it proceeds with this code. Otherwise, it just appends
        #the non-alpha value to new_char using 'else' below
        pos = alphabet_position(char)
        rot_pos = (pos + rot) % 26
        #below is how I dealt with needing to keep upper case characters upper case in the return value. Since
        #pos is just a number, we can look at the character 'char' that was passed to the function. If it's upper
        #case, the new character is make upper case during addition to the string
        if char.isupper() == True:
            new_char = new_char + chr(rot_pos + 97).upper()
        else:
            new_char = new_char + chr(rot_pos + 97)
    else:
        new_char = new_char + char
    return new_char