from stats import (
    get_word_count, 
    get_characters_count, 
    sort_alpha_char_count
)

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = get_word_count(text)
        characters_dict = get_characters_count(text)
        alpha_char_count = sort_alpha_char_count(characters_dict)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for c in alpha_char_count:
            if c.isalpha():
                print(f"{c}: {characters_dict[c]}")
            else:
                pass
        print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
