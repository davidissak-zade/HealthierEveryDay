def my_capitalize(txt):
    words = []
    words = txt.split(' ')
    out = ''
    for i in range(0, len(words)):
        words[i] = words[i].capitalize()
        out += words[i] + " "
    return out

