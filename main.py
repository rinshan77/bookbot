import sys
import string


def read_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as path:
            return path.read()
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied to access the file '{filepath}'.")
        sys.exit(2)
    except IOError as e:
        print(f"An I/O error occurred while reading the file: {e}")
        sys.exit(3)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(4)


def save_file(modified_book):
    save = (
        input("Would you like to save the modified document as a new file? (yes/no): ")
        .strip()
        .lower()
    )
    if save == "yes":
        path = input(
            "Enter the path and filename to save the document (e.g. /path/to/document.txt): "
        ).strip()
        try:
            with open(path, "w", encoding="utf-8") as file:
                file.write(modified_book)
            print(f"Document successfully saved to {path}!")
        except IOError as e:
            print(f"An error occurred while saving the document: {e}")
    else:
        print("The modified document was not saved.")


def count_chars(book):
    lowercase_book = book.lower()
    dictionary = {char: 0 for char in string.ascii_lowercase}
    for letter in lowercase_book:
        if letter in dictionary:
            dictionary[letter] += 1
    return dictionary


def word_count(book, specific_word=None):
    punctuation = string.punctuation + "“”"
    words = book.lower().split()
    word_dictionary = {}

    for word in words:
        clean_word = "".join(char for char in word if char not in punctuation)
        if clean_word:
            word_dictionary[clean_word] = word_dictionary.get(clean_word, 0) + 1

    if specific_word:
        specific_word_clean = "".join(
            char for char in specific_word.lower() if char not in punctuation
        )
        count = word_dictionary.get(specific_word_clean, 0)
        print(f"The word '{specific_word_clean}' appears {count} times.")
    else:
        return word_dictionary


def sort_words(word_count, start=0, end=None, reverse_order=False, group_once=False):
    sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    if end is None or end > len(sorted_words):
        end = len(sorted_words)

    if reverse_order:
        selected_words = sorted_words[start:end][::-1]
    else:
        selected_words = sorted_words[start:end]

    if group_once:
        words_once = [item for item in sorted_words if item[1] == 1]
        selected_words = [item for item in selected_words if item[1] != 1]
        print_count_table(selected_words, item_type="words")

        if words_once:
            print(f"\nWords which appear once: {len(words_once)} words")
            print(" | ".join([item[0] for item in words_once if item[0]]))
    else:
        print_count_table(selected_words, item_type="words")


def clean_up_text(text):
    while "  " in text:
        text = text.replace("  ", " ")
    punctuations = [".", "!", "?", "\n"]
    for p in punctuations:
        text = text.replace(p + " ", p + "")
    return text


def replacer(book, old_word, new_word, case_sensitive=True):
    lines = book.split("\n")
    replaced_lines = []
    len_old_word = len(old_word)

    for line in lines:
        new_line = []
        i = 0
        while i < len(line):
            segment = line[i : i + len_old_word]
            if case_sensitive:
                match = segment == old_word
            else:
                match = segment.lower() == old_word.lower()

            if (
                match
                and (i == 0 or not line[i - 1].isalpha())
                and (
                    i + len_old_word == len(line)
                    or not line[i + len_old_word].isalpha()
                )
            ):
                new_line.append(new_word)
                i += len_old_word
            else:
                new_line.append(line[i])
                i += 1
        replaced_lines.append("".join(new_line))

    return "\n".join(replaced_lines)


def replace_word(book):
    modified_book = book

    while True:
        words = input(
            "Please enter the word you wish replaced in the document followed by the word you want it replaced with. \n"
            "Enter one word only to remove the word from the document: "
        ).split()

        if len(words) not in [1, 2]:
            print(
                "Invalid input. Please enter one or two words. Try again or type 'quit' to exit."
            )
            continue

        if words[0].lower() == "quit":
            print("Exiting replace word operation.")
            return modified_book

        case_sensitive = (
            input("Should the replacement be case-sensitive? (yes or no): ")
            .strip()
            .lower()
            == "yes"
        )

        if len(words) == 1:
            removal_word = words[0]
            book_temp = replacer(modified_book, removal_word, "", case_sensitive)

            if (case_sensitive and removal_word in modified_book) or (
                not case_sensitive and removal_word.lower() in modified_book.lower()
            ):
                modified_book = clean_up_text(book_temp)
                sensitivity = "case-sensitive" if case_sensitive else "case-insensitive"
                print(f"'{removal_word}' removed from the document ({sensitivity}).")
            else:
                print(f"'{removal_word}' was not found in the document. Try again.")
                continue
        else:
            replace_word, with_word = words
            book_temp = replacer(modified_book, replace_word, with_word, case_sensitive)

            if (case_sensitive and replace_word in modified_book) or (
                not case_sensitive and replace_word.lower() in modified_book.lower()
            ):
                modified_book = book_temp
                sensitivity = "case-sensitive" if case_sensitive else "case-insensitive"
                print(f"'{replace_word}' replaced with '{with_word}' ({sensitivity}).")
            else:
                print(f"'{replace_word}' was not found in the document. Try again.")
                continue

        print("\n --- Start of the modified document --- \n")
        print(modified_book)
        print("\n --- End of the modified document --- \n")

        save_decision = (
            input("Do you want to save the changes to the working document? (yes/no): ")
            .strip()
            .lower()
        )
        if save_decision == "yes":
            save_file(modified_book)
            print("Changes saved to working document.")
        else:
            print("Changes not saved to working document.")

        # Ask if user wishes to continue modifying the document
        continue_modification = (
            input("Do you wish to modify other words in the document? (yes/no): ")
            .strip()
            .lower()
        )
        if continue_modification == "no":
            return modified_book
        else:
            print("Continuing to modify the document.")


def print_count_table(sorted_items, columns=10, item_type="letters"):
    for i in range(0, len(sorted_items), columns):
        row_items = sorted_items[i : i + columns]
        if item_type == "letters":
            print(" | ".join([f"'{item}': {count:5}" for item, count in row_items]))
        elif item_type == "words":
            print(" | ".join([f"'{item}': {count}" for item, count in row_items]))


def main(book):
    while True:
        print("\nChoose an option:")
        print("1) Print the entire document on screen.")
        print(
            "2) Count how many times each letter of the alphabet appears in the document."
        )
        print("3) List how many times every single word in the document appears.")
        print("3.1) Same as option 3 but group words that appear only once.")
        print("4) List the most common words from rank 'a' to rank 'b'.")
        print("5) Count how many times a given word appears in the document.")
        print("6) Replace or remove a word in the document.")
        print("7) Save the current working document.")
        print("8) Exit")
        choice = input("Please enter your choice: ")

        if choice == "1":
            print(
                f"\n --- Start of the document --- \n {book}\n--- End of the document ---"
            )
        elif choice == "2":
            char_count = count_chars(book)
            sorted_chars = sorted(
                char_count.items(), key=lambda item: item[1], reverse=True
            )
            print_count_table(sorted_chars)
        elif choice == "3":
            words_count = word_count(book)
            sort_words(words_count)
        elif choice == "3.1":
            words_count = word_count(book)
            sort_words(words_count, group_once=True)
        elif choice == "4":
            try:
                start, end = map(
                    int,
                    input(
                        "Enter the starting and ending ranks separated by space (e.g. 100 150): "
                    ).split(),
                )
                words_count = word_count(book)
                if start > end:
                    sort_words(words_count, end - 1, start, reverse_order=True)
                else:
                    sort_words(words_count, start - 1, end)
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")
        elif choice == "5":
            word = input("Enter the specific word:")
            word_count(book, word)
        elif choice == "6":
            book = replace_word(book)
        elif choice == "7":
            save_filename = input("Enter the filename to save the document: ")
            with open(save_filename, "w") as file:
                file.write(book)
            print(f"Document saved to {save_filename}.")
        elif choice == "8":
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
