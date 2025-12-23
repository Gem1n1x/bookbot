
def word_count(book_text):
 words = book_text.split()
 num_words = len(words)
 return num_words

def main():
    book_text = get_book_text("books/frankenstein.txt")

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    print(f"Found {num_words} total words")


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

from stats import word_count

main()

