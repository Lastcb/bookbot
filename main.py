from stats import get_word_count, get_characters_count

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_word_count(text)
    characters_dict = get_characters_count(text)
    print(f"{num_words} words found in the document")
    print(characters_dict)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
