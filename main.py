from stats import get_book_text, count_words, count_chars, sorted_chars
import sys

if (len(sys.argv) != 2):
    raise Exception("Usage: python3 main.py <path_to_book>")
    
def main():
    text = get_book_text(sys.argv[1])
    count = count_words(text)
    count_ch = count_chars(text)
    sorted = sorted_chars(count_ch)
    print("============ BOOKBOT ============\n"
        f"Analyzing book found at {sys.argv[1]}...\n"
        "----------- Word Count ----------\n"
        f"Found {count} total words\n"
        "--------- Character Count -------"
        )
    for item, val in sorted:
        if (item.isalpha()):
            print(f"{item}: {val}")
    print("============= END ===============")

main()