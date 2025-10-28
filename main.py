import sys

from stats import get_number_of_words, get_character_count, sorted_dict

def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main(file_path: str):
    # print(get_book_text(file_path))
    book_text = get_book_text(file_path)
    num_words = get_number_of_words(book_text)
    char_dict = sorted_dict(get_character_count(book_text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    # print(char_dict)
    for key, value in char_dict.items():
        print(f"{key}: {value}")
    print("============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        main(sys.argv[1])

