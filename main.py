from stats import get_num_words, get_chars_dict, chars_dict_sorted_list
import sys
def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book_text = get_book_text(sys.argv[1])

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("Analyzing book found at", sys.argv[1])
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    chars_dict = get_chars_dict(text)
    sorted_chars = chars_dict_sorted_list(chars_dict)
    print("--------- Character Count -------")
    for item in sorted_chars:
        ch = item["char"]
        count = item["num"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {count}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()

