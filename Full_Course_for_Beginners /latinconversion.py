# Latin Handwriting
# -------------------
# J = I
# U = V
# W = VV

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "j":
            if letter.isupper():
                translation = translation + "I"
            else:
                translation = translation + "i"
        elif letter.lower() in "u":
            if letter.isupper():
                translation = translation + "V"
            else:
                translation = translation + "v"
        elif letter.lower() in "w":
            if letter.isupper():
                translation = translation + "VV"
            else:
                translation = translation + "vv"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter some Latin: ")))
