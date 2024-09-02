def main():
    path = "books/frankenstein.txt"
    contents = get_book_text(path)
    word_count = count_words(contents)
    char_count = count_characters(contents)
    print_report(path, word_count, char_count)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        #print(file_contents)
        return file_contents

def count_words(file_contents):
    count = 0
    words = file_contents.split()
    for word in words:
        count += 1
    return count

def count_characters(contents):
    word_characters = {}
    
    lowered_contents = contents.lower()
    for char in lowered_contents:
        if char in word_characters:
            word_characters[char] += 1
        else:
            word_characters[char] = 1
        
    #print(word_characters)
    return word_characters

def sort_list(dict):
    return dict["num"]

def print_report(path, word_count, char_count):
    sorted_list = []
    for pair in char_count:
        sorted_list.append({"char": pair, "num":char_count[pair]})

    sorted_list.sort(reverse=True, key=sort_list)

    print(f"--- Begin report of {path} ---") 
    print(f"{word_count} words found in the document\n")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"The {item['char']} character was found {item['num']} times")
    print(f"--- End report ---") 


main()