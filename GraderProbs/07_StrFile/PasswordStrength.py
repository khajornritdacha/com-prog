import string

def no_lowercase(t): # return True if no lowercase, otherwise return False
    for c in string.ascii_lowercase:
        if c in t:
            return False
    return True

def no_uppercase(t):
    for c in string.ascii_uppercase:
        if c in t:
            return False
    return True

def no_number(t):
    for c in t:
        if c.isdigit():
            return False
    return True

def no_symbol(t):
    for c in t:
        if not c.isalnum():
            return False
    return True

def character_repetition(t):
    for idx in range(0, len(t)-3):
        if t[idx] == t[idx+1] == t[idx+2] == t[idx+3]:
            return True
    return False

# Must do 2 ways check: 0->n and n->0
def number_sequence(t): 
    pat = "0123456789" * 2 
    return letter_sequence(t, pat)

def letter_sequence(t, pat = string.ascii_lowercase):
    t = t.lower()
    for idx in range(0, len(t)-3):
        cur = t[idx: idx+4]
        if cur in pat:
            return True
        if cur[::-1] in pat:
            return True

    return False

def keyboard_pattern(t):
    patterns = ["!@#$%^&*()_+",
            "QWERTYUIOP",
            "ASDFGHJKL",
            "ZXCVBNM"]
    
    for pat in patterns:
        if letter_sequence(t, pat.lower()):
            return True
    return False

#-----------------------------
passw = input().strip()
errors = []
if len(passw) < 8:
    errors.append("Less than 8 characters")
if no_lowercase(passw):
    errors.append("No lowercase letters")
if no_uppercase(passw):
    errors.append("No uppercase letters")
if no_number(passw):
    errors.append("No numbers")
if no_symbol(passw):
    errors.append("No symbols")
if character_repetition(passw):
    errors.append("Character repetition")
if number_sequence(passw):
    errors.append("Number sequence")
if letter_sequence(passw):
    errors.append("Letter sequence")
if keyboard_pattern(passw):
    errors.append("Keyboard pattern")

if len(errors) == 0:
    print("OK")
else:
    print("\n".join(errors))