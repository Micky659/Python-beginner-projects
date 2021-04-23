import re
import winsound
from reference import punch, alphanum

sender = input()
pieces = re.findall(r"[\w']+|[,!?;:]", sender)

output = ""
reg = re.compile('^[. -]*$')


def encode(word):
    for key in alphanum.keys():
        word = word.lower().replace(key, alphanum[key])
    return word


# Only work for letters
def decode(morsecode):
    english = ""
    for morse in morsecode:
        for key, values in alphanum.items():
            morse = morse.replace(values, key)
        english = english + morse + " "
    print(english)


if bool(reg.match(sender)):
    code = sender.split(" ")
    decode(code)

for piece in pieces:
    if piece.isalnum():
        output = output + encode(piece) + " "
    elif piece in punch.keys():
        value = punch[piece]
        output = output + value + " "

print(output)
for letter in output:
    if letter == ".":
        winsound.Beep(400, 200)
    elif letter == "-":
        winsound.Beep(400, 500)
    else:
        winsound.Beep(37, 200)
