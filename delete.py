# delete characters in a string
def anti_vowel(text):
    vowels = "aioueAIOUE"
    for v in vowels:
        text = text.replace(v, "")
    return text

print anti_vowel("Hey You!")
