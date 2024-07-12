def read_file(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def count_words(book):
        words = book.split()
        count = 0
        for word in words:
            count += 1
        print(f"The number of words in this book are {count}.")

def count_chars(book):
    lowercase_book = book.lower()
    dictionary = {}
    for i in "abcdefghijklmnopqrstuvwxyz":
        dictionary[i] = 0
        for letter in lowercase_book:
            if letter in dictionary:
                dictionary[letter] += 1
    return dictionary   

def print_char_counts_table(char_counts, columns=10):
    items = list(char_counts.items())
    print("The amount of each letter appearing in the book is:")
    for i in range(0, len(items), columns):
        row_items = items[i:i+columns]
        print(' '.join([f"{char}: {count:5}" for char, count in row_items]))

if __name__ == "__main__":
    with open("books/frankenstein.txt") as f:
        book = read_file("books/frankenstein.txt")

    #print(book)
    count_words(book)
    print_char_counts_table(count_chars(book))