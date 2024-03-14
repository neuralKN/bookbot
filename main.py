def count_words(text):
    return len(text.split()) 

def count_letters(text):
    lower = text.lower()

    count_dict = {}

    for char in lower:

        # Ignore any characters not in the alphabet
        if not char.isalpha():
            continue

        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    return count_dict

def sort_on(dict_item):
    return dict_item["num"]

def print_report(count_dict):
    
    list_of_dicts = [{"name": char, "num": val} for char, val in count_dict.items()]
    print(len(list_of_dicts))

    print("--- Begin report of books/frankenstein.txt ---")
    list_of_dicts.sort(reverse=True, key=sort_on)

    for dict_item in list_of_dicts:
        print(f" The {dict_item["name"]} character was found {dict_item["num"]} times") 
    
            

    
def main():
    with open("./books/frankenstein.txt") as file:
        file_contents = file.read()

    print("--- Begin report of books/frakenstein.txt ---") 
    print(f"{count_words(file_contents)} number of words in the document.")

    letters_count = count_letters(file_contents)
    print_report(letters_count)

    
main()
