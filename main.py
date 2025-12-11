import sys
from stats import count_words, count_characters, sort_used_letters

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:
        book_path = sys.argv[1]
        book_content = (get_book_text(book_path))
        letters_not_sorted = count_characters(book_content)
        letters_sorted = sort_used_letters(letters_not_sorted)
        
        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        print(f"Found {count_words(book_content)} total words")
        print("--------- Character Count -------")

        for item in letters_sorted:
            char = item["char"]
            num = item["num"]

            if char.isalpha():
                print(f"{char}: {num}")

        print("============= END ===============")

def get_book_text(path_to_file):
    with open (path_to_file) as f:
        file_content = f.read()
    return  file_content
    
main()