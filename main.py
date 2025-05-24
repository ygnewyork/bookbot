import sys
from stats import words_count, char_counts, sorted

def get_book_text(name):
    with open(name) as f:
        file_contents = f.read()
        return file_contents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    count = words_count(text)
    dicts = (char_counts(text))
    result = sorted(dicts)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for abc in result:
        if abc["char"].isalpha():
            print(f"{abc['char']}: {abc['num']}")
    print("============= END ===============")


main()
