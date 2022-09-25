raw = input()

vowels = "aeiou"

if raw[-1] in "sx" or ( len(raw) >= 2 and raw[-2:] == "ch"):
    print(raw + "es")
elif raw[-1] == "y" and (len(raw) == 1 or (len(raw) > 1 and raw[-2] not in vowels)):
    print(raw[:-1] + "ies")
else:
    print(raw + "s")
    