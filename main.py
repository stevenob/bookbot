def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    # print(text)
    # count_text(text)
    # print(count_letters(text))
    print_report(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_text(text):
    words = text.split()
    print(len(words))

def count_letters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def print_report(text):
    chars = count_letters(text)
    letters = []
    for key, value in chars.items():
        if key.isalpha():
            temp = [key,value]
            letters.append(temp)
    letters.sort()
    print(f"--- Begin report of books/frankenstein.txt ---\n{count_text(text)} words found in the document")
    for i in range(len(letters)):
        print(f"The '{letters[i][0]}' character was found {letters[i][1]} times")



main()