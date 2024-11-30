def main():
    books = [
        {"Book": "Frankenstein", "Path": "Books/frankenstein.txt"},
        {"Book": "Romeo & Juliet", "Path": "Books/romeo_&_juliet.txt"},
        {"Book": "Moby Dick", "Path": "Books/moby_dick.txt"},
        {"Book": "Little Women", "Path": "Books/little_women.txt"}
    ]

    print("We have the following books to choose from:\n")

    book_list_count = 0
    for book in books:
        book_list_count += 1
        print(f"{book_list_count}: {book['Book']}")
    
    while True:
        book_choice_input = input("\nWhich book would you like to analyze? ")
        book_choice_input = int(book_choice_input)
        try:
            if 1 <= book_choice_input <= len(books):
                book_choice = books[book_choice_input - 1]
                print(f"Ahhh, {book_choice['Book']}, great choice!\n")
                break
            else:
                print(f"Sorry, we don't have that many books! Please enter a number between 1 and {len(books)}")
        except ValueError:
            print("Numbers only please!")

    file_contents = extract_text(book_choice['Path'])
    book_length = word_count(file_contents)
    letter_count = char_count(file_contents)
    sorted_count = sorted_chars(letter_count)
    
    print(f"--- Begin report of {book_choice['Book']} ---")
    print(f"{book_length} words found in the document\n")
    for count in sorted_count:
        print(f"The '{count[0]}' character was found {count[1]} times")
    print("--- End report ---")

def extract_text(book):
    with open(book) as f:
        return f.read()

def word_count(text):
    return len(text.split())

def char_count(chars):
    letters = {}
    for char in chars:
        char = char.lower()
        if char.isalpha():
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
    
    return letters

def sort_by(dict):
    return dict[1]

def sorted_chars(dict):
    
    list_of_dict = list(dict.items())
    list_of_dict.sort(reverse=True, key=sort_by)
    return list_of_dict

main()