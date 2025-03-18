from stats import word_count, char_count, sort_chars
import sys

def get_book_text(input):
    with open(input) as f:
        file_contents = f.read()
    return file_contents 

def create_report(text):
    wc = word_count(text)
    cc = char_count(text)
    sorted_cc = sort_chars(cc)
    print(f"============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"{wc}")
    print("--------- Character Count -------")
    
    for key, value in sorted_cc.items():
        if key.isalpha():
            print(f"{key}: {str(value)}")
    
    print("============= END ===============")

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        create_report(text)
    
main()
