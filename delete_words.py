def censor(text, words):
    text = text.split()
    censored_text = [item for item in text if item not in words]
    return " ".join(censored_text)
    
hacks = ("hack", "wack", "is")
print censor("this hack is wack hack", hacks)
# prints "this"
