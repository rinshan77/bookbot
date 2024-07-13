import sys


def read_file(filepath):
    try:
        with open(filepath, 'r') as path:
            return path.read()
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return ""
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return ""

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

def word_count(book):
    lowercase_book = book.lower()
    words = lowercase_book.split()
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count



def main(book):
    print(f"--- Begin report of the entered document ---")  
    word_count = count_words(book)
    char_count = count_chars(book)
    sorted_chars = sort_dictionary(char_count)
    print(f"{word_count} words found in the document")
    print()
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    if len(sys.argv) == 1:
        filepath = input("Please enter the path to the text file: ")
    book = read_file(filepath)
    if book:
        main(book)
    else:
        print("Failed to read file. Please check the file path and try again.")
