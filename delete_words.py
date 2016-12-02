#delete words in a string
def censor(text, word):
    text = text.split()
    for item in text:
        if item == word:
            text.remove(word)
    return " ".join(text)

print censor("this hack is wack hack", "hack")

# prints "this is wack"
