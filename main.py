def read_file(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def count_words(book):
        words = book.split()
        count = 0
        for word in words:
            count += 1
        return count

def count_chars(book):
    lowercase_book = book.lower()
    dictionary = {}
    for i in "abcdefghijklmnopqrstuvwxyz":
        dictionary[i] = 0
    for letter in lowercase_book:
        if letter in dictionary:
            dictionary[letter] += 1
    return dictionary   

def print_char_count_table(char_counts, columns=10):
    items = list(char_counts.items())
    for i in range(0, len(items), columns):
        row_items = items[i:i+columns]
        print(' '.join([f"{char}: {count:5}" for char, count in row_items]))

def count_get(item):
    return item[1]

def sort_dictionary(char_count):
    char_tuple = char_count.items()
    char_list = list(char_tuple)
    sorted_char_list = sorted(char_list, key=count_get, reverse=True)
    return sorted_char_list

def main(book):
    print("--- Begin report of books/frankenstein.txt ---")  
    word_count = count_words(book)
    char_count = count_chars(book)
    sorted_chars = sort_dictionary(char_count)
    print(f"{word_count} words found in the document")
    print()
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

if __name__ == "__main__":
    with open("books/frankenstein.txt") as f:
        book = read_file("books/frankenstein.txt")

    #print(book)
    #count_words(book)
    #print(count_chars(book))
    #print_char_count_table(count_chars(book))

main(book)

    