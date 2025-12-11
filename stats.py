def count_words(book_content):
    words = len(book_content.split())
    return f"Found {words} total words"

def count_characters(book_content):

    words = []
    used_letters = {}

    for word in book_content.split():

        word = word.lower()
        
        for letter in word:        
            try:
                used_letters[letter] += 1
            except KeyError:
                used_letters[letter] = 1

    return used_letters


def sort_on(items):
    return items["num"]

def sort_used_letters(letters_not_sorted):

    sorted_list = []

    for key, value in letters_not_sorted.items():
        new_dict = {"char": key, "num": value}
        sorted_list.append(new_dict)

    sorted_list.sort(reverse=True, key=sort_on)
    
    return sorted_list
