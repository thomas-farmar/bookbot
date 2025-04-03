import sys
from stats import get_character_counts, get_word_count, sort_character_counts


def get_book_text(filepath):
    with open(filepath, "r") as file:
        return file.read()


def main():
    len_args = len(sys.argv)
    if len_args != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_arg = sys.argv[1]
    book_text = get_book_text(book_arg)
    num_words = get_word_count(book_text)
    char_counts = get_character_counts(book_text)
    records = sort_character_counts(char_counts)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for record in records:
        if record["char"].isalpha():
            print(f"{record['char']}: {record['count']}")


if __name__ == "__main__":
    main()
