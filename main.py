def main():
    book_path = "Books/frankenstein.txt"
    file_contents = extract_text(book_path)
    book_length = word_count(file_contents)
    print(file_contents)
    print(f"Wow! Frankenstein is {book_length} words long!")

def extract_text(book):
    with open(book) as f:
        return f.read()

def word_count(text):
    return len(text.split())

main()