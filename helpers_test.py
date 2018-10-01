alpha = "abcdefghijklmnopqrstuvwxyz"

def alphabet_position(letter):
    letter = letter.lower()
    letter_num = ord(letter) - 97
    return letter_num

def rotate_character(char, rot):
    new_char = ''
    if char.isalpha() == True:
        pos = alphabet_position(char)
        rot_pos = (pos + rot) % 26
        if char.isupper() == True:
            new_char = new_char + chr(rot_pos + 97).upper()
        else:
            new_char = new_char + chr(rot_pos + 97)
    else:
        new_char = new_char + char
    return new_char