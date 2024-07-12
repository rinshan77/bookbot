def print_book(book):
        print(book)

def count_words(book):
        words = book.split()
        count = 0
        for word in words:
            count += 1
        print(count)

def read_file(filepath):
    with open(filepath, 'r') as f:
        return f.read()

if __name__ == "__main__":
    with open("books/frankenstein.txt") as f:
        book = read_file("books/frankenstein.txt")

    print_book(book)
    count_words(book)