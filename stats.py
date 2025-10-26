def count_words(file_contents):
    split_file_contents = file_contents.split()
    num_words = len(split_file_contents)
    return num_words

def count_charakters (file_contents):
    file_contents = file_contents.lower()
    letter_dictionary = {}
    for letter in file_contents:
        if letter in letter_dictionary: #bokstav er der
            letter_dictionary[letter] += 1
        else: #bokstav er ikke der
            letter_dictionary[letter] = 1
    return letter_dictionary

def sort_on(item):
    return item["num"] 

def sorted_dictionary(letter_dictionary):
    results = []
    for letter, count in letter_dictionary.items():
        if letter.isalpha():
            results.append({"char": letter, "num": count})
    results.sort(reverse=True, key=sort_on)
    return results