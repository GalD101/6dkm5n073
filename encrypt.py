# unique = []
import random

letters_no_six = 'abcdeghijkmnopqstuvwyz'
mapping = {
    'I': 'T', # mod 6 === 3
    'h': 'f', # mod 6 === 2
    'a': 's', # mod 6 === 1 (because left has no btns we go right)
    't': 'e', # mod 6 === 2
    'e': 'r', # mod 6 === 2 (again after reaching the edge on the left side we go back right)
    'b': 'c', # mod 6 === 2
    'i': 't', # mod 6 === 3
    'n': 'v', # mod 6 === 2
    'g': 'f', # mod 6 === 1
    'm': 'n', # mod 6 === 1
    'y': 't', # mod 6 === 1
    's': 'a', # mod 6 === 1
    'l': 'l', # mod 6 === 0 (no PHYSICAL MOVEMENT here)
    'f': 'f', # mod 6 === 0 (dont MOVE)
    'w': 't', # mod 6 === 5 (when reaching the edge, change direction (from left to right))
    'o': 'y', # mod 6 === 3
    'd': 'd', # mod 6 === 4 (this is a case where we land on the same one but the algorithm stays the same. go left, when you reach the end, switch direction (r)) in this case we land back in the same spot
    'v': 'x', # mod 6 === 4 (again, when reaching the edge go right (from l to r))
    'r': 'r', # mod 6 === 0 (stay)
    'p': 'y', # mod 6 === 4
    'c': 'x', # mod 6 === 3 (after you reached the edge go back)
    'u': 'r', # mod 6 === 3
    'k': 'd', # mod 6 === 5
    'x': 'x', # mod 6 === 0 (dont MOVE left)
    'z': 'c', # mod 6 === 2 (this is a weird case. we have a dead end on left so we go right two steps to c)
    '.': '.', # non alphabetic stays the same
    'j': 'd', # mod 6 === 4
    '1': '`', # mod 6 === 1 (special case, numbers will use their value unlike letters that use index)
    '6': '^', # numbers change to corresponding symbol
    'q': 'y', # mod 6 === 5 (left is blocked, so switch right)
    'E': 'R', # mod 6 === 5 (switch directions when you encounter a dead end)
    ',': ',', # dont change cuz this has no numerical meaning
    'F': 'F', # mod 6 === 0 dont move left (or right)
    "'": "'", # no numerical meaning so stay the same (yeah its useless i know)
    'W': 'T', # mod 6 === 5 (again, switch direction if you reach a dead end)
    'A': 'S', # mod 6 === 1 dead end on left -> go right
    'N': 'V', # mod 6 === 2
    'T': 'E', # mod 6 === 2
    'O': 'Y', # mod 6 === 3
    'K': 'D', # mod 6 === 5
    'L': 'L', # mod 6 === 0 (dont move)
    'M': 'N', # mod 6 === 1
    'Y': 'T', # mod 6 === 1
    'S': 'A', # mod 6 === 1
    '4': '$', # numbers change to corresponding symbol
    '2': '@', # numbers change to corresponding symbol
    '0': ')', # numbers change to corresponding symbol
    'G': 'F', # mod 6 === 1
    'H': 'F', # mod 6 === 2
    'B': 'C', # mod 6 === 2
    '?': '?', # keep symbols as they are
    '"': '"', # keep symbols as they are
    'P': 'Y', # mod 6 === 4
    'J': 'D', # mod 6 === 4
    'C': 'X', # mod 6 === 3 (remember to change directions on dead end)
    'V': 'X', # mod 6 === 4 (again, change direction once you get to an edge)
    'U': 'T', # mod 6 === 2
    'R': 'R', # mod 6 === 0 (18 is divisble by six so dont shift your keyboard)
    'D': 'D', # mod 6 === 4 (go 2 steps left -> dead end -> 2 steps right land in the same place)
    ':': ':', # symbols dont change and this is useless
    '!': '!', # but not really useless
}
language = {
    'v': 'ה',
    'V': 'V',
    'f': 'כ',
    'e': 'ק',
    ':': ':',
    'a': 'ש',
    '^': '^',
    'l': 'ך',
    'L': 'L', # (it is useless)
    '?': '?',
    '$': '$',
    's': 'ד',
    'S': 'S',
    't': 'א',
    'T': 'T',
    'c': 'ב',
    'C': 'C',
    "'": ",",
    '"': '"',
    'n': 'מ',
    'r': 'ר',
    '!': '!',
    'x': 'ס',
    'X': 'X',
    'F': 'F',
    'd': 'ג',
    'D': 'D',
    '`': '`',
    ',': 'ת',
    '.': 'ץ',
    '@': '@',
    '(': ')',
    'y': 'ט',
    'Y': 'Y',
    'N': 'N',
    'E': 'E',
    'A': 'A',
    'R': 'R',
    '!': '!',
}

# with open('6dkm5n073', 'r') as filp:
#     for line in filp:
#         print(line)
#         for letter in line:
#             if not letter in unique:
#                 unique.append(letter)

# print(unique)

raw_text = ""
with open('6dkm5n073', 'r') as leet_speak:
    for line in leet_speak:
        raw_text += line
        # fnyg im not sure if its the actual terminology
        # this will make it a lot harder to decrypt (I think)
        for l in line:
            if (ord(l) % 6 == 0):
                raw_text += ( ''.join(random.choice(letters_no_six) for i in range(1)) )
                

enc_text = raw_text
for key, val in mapping.items():
    enc_text = enc_text.replace(key, val)

for key, val in language.items():
    enc_text = enc_text.replace(key, val)



with open('enc', 'w') as enc:
    enc.write(enc_text)

# a410c9304993aba0ed74421482aaa731fb76f55225b08e51b09b59806c816810
# a71b72043284cc3a800c31439de4fe8fb4f138182b90ad8e345f9477625fdbb6