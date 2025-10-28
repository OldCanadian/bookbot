def get_number_of_words(book_text: str) -> int:
    word_list = book_text.split()
    word_count = len(word_list)
    return word_count

def get_character_count(book_text: str) -> dict[str, int]:
    my_dict: dict[str, int] = {}
    for char in book_text:
        if char.lower() in my_dict:
            my_dict[char.lower()] += 1
        else:
            my_dict[char.lower()] = 1
    return my_dict

def sorted_dict(my_dict: dict[str, int]) -> dict[str, int]:
    new_char_dict: dict[str, int] = {}
    sorted_char_dict: dict[str, int] = sorted(my_dict.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    for key, value in sorted_char_dict:
        if key.isalpha():
            new_char_dict[key] = value
    return new_char_dict


