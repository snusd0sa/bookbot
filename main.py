def main():
    path_to_book = "books/frankenstein.txt"
    text =read_file(path_to_book)
    #print(text)
    t = count_word(text)
    print(f"{t} words in the document")
    cc = character_count(text)
    print(cc)
    #
    sorted_list = sorter(cc)
    print (sorted_list)
    nice_list(sorted_list)
    
def read_file(path_to_file):
    with open(path_to_file) as f:
        t = f.read()
    return t

def count_word(text):
    t = len(text.split())
    return t
    
def character_count(s):
    dict ={}
    lowered = s.lower()
    s.replace(" ", "")
    for c in lowered:
        if c not in dict:
            dict.update({c:1})
        else:
            dict[c] += 1
        
    return dict

def sort(d):
    return d["num"]
def sorter(d):
    sorted_list = []
    for c in d:
        sorted_list.append({"char": c, "num": d[c]})

    sorted_list.sort(reverse=True, key=sort)
    return sorted_list

def nice_list(l):
    for ch in l:
        if ch['char'].isalpha():
            print(f"The {ch['char']} character was found {ch['num']} times")


main()
