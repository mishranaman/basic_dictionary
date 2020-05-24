import json
from difflib import get_close_matches

data = json.load(open("data.json"))
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches (word, data.keys()))>0:
        yo = input("Did you mean %s Instead? Enter Y for yes and N for No"  %get_close_matches(word, data.keys())[0])
        if yo == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yo == "N":
            return "Word not found in dictionary"
        else:
            return "We did not understand"
    else:
        return "The word does not exist, Please enter a correct word"

word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
