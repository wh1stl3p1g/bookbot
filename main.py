def main(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    print(f"--- Begin report of {filepath} ---")
    print(f"{word_count(file_contents)} words found in the document")
    unsorted = letter_count(file_contents)
    unsorted.sort(reverse=True, key=sort_this)
    for letter in unsorted:
        print(f"The '{letter['char']}' character was found {letter['num']} times")
    print("--- End report ---")
def word_count(string):
    words = string.split()
    return len(words)

def letter_count(string):
    lowercase = string.lower()
    letters = {}
    letter_dicts = []
    for letter in lowercase:
        if letter.isalpha():
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
    for letter, count in letters.items():
        dict_item = {"char": letter, "num": count}
        letter_dicts.append(dict_item)
    return letter_dicts

def sort_this(dictionary):
    return dictionary["num"]

    
main("books/frankenstein.txt")