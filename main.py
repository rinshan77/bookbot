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

def print_char_count_table(sorted_chars, columns=10):
    for i in range(0, len(sorted_chars), columns):
        row_items = sorted_chars[i:i+columns]
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

def sort_words(word_count, start=0, end=None):
    sorted_words = sorted(word_count.items(), key=count_get, reverse=True)
    selected_words = sorted_words[start:end]
    for word, count in selected_words:
        print(f"The word '{word}' appears {count} times")

def count_specific_word(book, word):
    word = word.lower()
    words= book.lower().split()
    count = 0
    for w in words:
        if w == word:
            count += 1
    print(f"The word '{word}' appears {count} times.")

    

def main(book):
    while True:
        print("\nChoose an option:")
        print("1) Print the entire document on screen.")
        print("2) Count how many times each letter of the alphabet appears in the document.")
        print("3) List how many times every single word in the document appears.")
        print("4) List the most common words from place a to b.")
        print("5) Count how many times a given word appears in the document.")
        print("6) Exit")
        choice = input("Please enter your choice:")

        if choice == '1':
            print (f"\n --- Start of the document --- \n {book}\n--- End of the document ---")
        elif choice == '2':
            char_count = count_chars(book)
            sorted_chars = sort_dictionary(char_count)
            print_char_count_table(sorted_chars)
        elif choice == '3':
            words_count = word_count(book)
            sort_words(words_count)
        elif choice == '4':
            try:
                start, end = map(int, input("Enter the starting and ending ranks separated by space (e.g. 100 150): ").split())
                words_count = word_count(book)
                sort_words(words_count, start - 1, end)
            except ValueError:
                print("Invalid input. Please enter two integers separated by space.")
        elif choice == '5':
            word = input("Enter the specific word:")
            count_specific_word(book, word)
        elif choice == '6':
            print("Exiting, have a fantastic day!")
            break
        else:
            print("That's not an option, try again")



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
