def reverse_string(text):
    newlist =[]
    for n in text:
        newlist.append(n)
    newlist.reverse()
    newword = "".join(newlist)
    return(newword)
