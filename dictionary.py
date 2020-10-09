import json
from difflib import get_close_matches

data  = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))> 0 :
        print("Do you mean %s instead" %get_close_matches(word,data.keys())[0])
        decide = input("Press Y for Yes or N for No")
        if decide == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide == "N":
            return("No such word exists")
        else:
            print("You have entered wrong input")
    else:
        print("No such word exists")


word = input("Enter a word: ")

output = translate(word)
print(output)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
