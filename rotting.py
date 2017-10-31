# Rot 0-25 for a string of text.

len_alphabet = 26
n = input(">>> ")
for i in range(len_alphabet):
    if i < 10:
        print("0"+str(i)+". ", end = "")
    else:
        print(str(i)+". ", end = "")
    for c in n:
	# alpha chars only are changed by rot
	# so find alpha chars first and only change those.
	# but then we have to decide if it's upper or lower case
        if c.isalpha():
            # rather than working out if it's upper or lower case we can just calculate the change required
            # that way it works for either!
            offset = ord(c.lower())-ord('a')
            diff = ((offset+i)%len_alphabet) - offset
            print(chr(ord(c) + diff), end = "")
        else: # Not alpha. (Thus might be numeric)
            print(c, end = "")
    print() # include a newline for readability
