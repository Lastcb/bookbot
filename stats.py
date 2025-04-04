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
