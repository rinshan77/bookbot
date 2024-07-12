def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def count_words():
    with open("books/frankenstein.txt") as f:
        content = f.read()
        words = content.split()
        count = 0
        for word in words:
            count += 1
    print(count)




if __name__ == "__main__":
    count_words()