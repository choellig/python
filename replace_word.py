# replaces words in a strings

def censor(text, word):
    text = text.split()
    for item,i in enumerate(text):
        if i == word:
            text[item] = "*" * len(word)
    return " ".join(text)


print censor("this hack is wack hack", "hack")
# prints "this **** is wack ****"
