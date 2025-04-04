def get_word_count(text):
    words = text.split()
    return len(words)

def get_characters_count(text):
    characters = {}
    for c in text:
        lowered = c.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters

def sort_alpha_char_count(dict):
    c = sorted(dict, key=dict.get, reverse=True)
    return c


    #for c in sorted(dict, key=dict.get, reverse=True):
     #   if c.isalpha() == True:
      #      return(c, dict[c])
       # else:
        #    pass
    #return c

