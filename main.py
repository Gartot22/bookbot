import sys

    


def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return str(file_contents)

def final_print(sorted_letter_list, num_words):
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + book_path) 
    print("----------- Word Count ----------")
    print("Found " + str(num_words) + " total words")
    print("--------- Character Count -------")
    for item in sorted_letter_list:
        print(item["char"] + ": " + str(item["num"]))
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    

    file_contents = get_book_text(book_path)
    from stats import count_words
    num_words = count_words(file_contents)
    

    from stats import count_charakters
    letter_dictionary = count_charakters(file_contents)
    

    from stats import sorted_dictionary
    sorted_letter_list = sorted_dictionary(letter_dictionary)
    final_print(sorted_letter_list, num_words)

main()