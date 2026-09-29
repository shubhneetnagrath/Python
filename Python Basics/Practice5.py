def count_vowels(text):
    i = 0
    for n in text:
        if n in "AEIOUaeiou":
          i+=1
    return(i)
