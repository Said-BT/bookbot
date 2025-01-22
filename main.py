def read_book(filename):
    with open(filename) as book:
        file_contents = book.read()
        return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    text = text.lower()
    results = {}

    for char in text:
        if char in results:
            results[char] += 1
        else:
            results[char] = 1

    return results

def main():
    text = read_book('books/frankenstein.txt')

    print('--- Begin report of books/frankenstein.txt ---')
    print(f'{count_words(text)} words found in the document')
    print()
    result = count_chars(text)

    result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))

    for key, value in result.items():
        if 'a' <= key <= 'z':
            print(f"The '{key}' character was found {value} times")
    print('--- End report ---')
main()
