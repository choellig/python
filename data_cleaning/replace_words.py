# replaces words in a strings

def censor(text, words):
    text = text.split()
    for item,i in enumerate(text):
        for word in words:
            if i == word:
                text[item] = "*" * len(word)
    return " ".join(text)

hacks = ("hack",)
print censor("this hack is wack hack", hacks)
# prints "this **** is wack ****"
