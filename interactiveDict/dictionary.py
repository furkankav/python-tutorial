import json
from difflib import get_close_matches

def translate(word):
    if word in data:
        return "\n".join(data[word])
    else:
        closeMatches = get_close_matches(word, data.keys())
        if len(closeMatches) > 0:
            meant = closeMatches[0]
            isYes = ""
            while(True):
                if isYes == "Y":
                    return "\n".join(data[meant])
                elif isYes == "N":
                    break
                else:
                    isYes = input ("Did you mean {}? Y for yes N for no! ".format(meant)).upper()

    return "The word doesn't exist. Please double check it. "

data = json.load(open("files/data.json"))

print("To exit type :q")
isExit = ""
while(True):
    word = input("Enter word: ")
    word = word.lower()
    if word == ":q":
        break
    print(translate(word))
