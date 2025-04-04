from stats import get_characters_count

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    characters_dict = get_characters_count(text)

    
    print(sort_alpha_char_count(characters_dict))
def sort_alpha_char_count(dict):
    for c in sorted(dict, key=dict.get, reverse=True):
        if c.isalpha() == True:
            print(c, dict[c])
        else:
            pass
def get_book_text(path):
    with open(path) as f:
        return f.read()
main()
