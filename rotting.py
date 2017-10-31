# Rot 0-25 for a string of text.

len_alphabet = 26
n = input(">>> ")
for i in range(len_alphabet):
    if i < 10:
        print("0"+str(i)+". ", end = "")
    else:
        print(str(i)+". ", end = "")
    for c in n:
        if c.isalpha():
            if c.isupper(): # Uppercase letters
                print(chr((ord(c)-ord('A')+i)%len_alphabet+ord('A')), end = "")
            else: # Lowercase letters
                print(chr((ord(c)-ord('a')+i)%len_alphabet+ord('a')), end = "")
        else: # Not alpha. (Thus might be numeric)
            print(c, end = "")
    print() # include a newline for readability
