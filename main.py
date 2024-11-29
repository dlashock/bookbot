def main():
    book_path = "Books/frankenstein.txt"
    file_contents = extract_text(book_path)
    book_length = word_count(file_contents)
    letter_count = char_count(file_contents)
    sorted_count = sorted_chars(letter_count)
    
    print(f"--- Begin report of {book_path} ---")
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
    
    #return list(sorted(dict.items(), key=lambda item: item[1], reverse=True))

main()