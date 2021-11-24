import random

# Convert diceware file to dict
def dice_dict(fl):
    d = {}
    with open(fl) as f:
        lines = f.readlines()
        for l in lines:
            c = l.split()
            d[c[0]] = c[1]
    return d

def gen_passphrase(n):
    d = dice_dict("diceware.txt")
    phrase = ""
    for i in range(0, n):
        key = ""
        for j in range(0, 5):
            s = random.randint(1, 6)
            key = key + str(s)
        phrase = phrase + d[key] + " "
    return phrase

print(gen_passphrase(5))

# Note: you shouldn't use the random module for security purposes, secret is better