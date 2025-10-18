import sys
from stats import get_words_count, get_chars_count, get_sorted_pairs

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    content = get_book_text(path_to_file)
    words = get_words_count(content)
    chars = get_chars_count(content)
    pairs = get_sorted_pairs(list(chars.keys()), list(chars.values()))

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")

    for pair in pairs:
        if(pair["char"].isalpha()):
            print(f"{pair['char']}: {pair['num']}")
    print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

main()
