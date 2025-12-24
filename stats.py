def get_num_words(book_text):
 words = book_text.split()
 num_words = len(words)
 return num_words

def get_chars_dict(text):
    counter = {}
    for ch in text:
        ch_lower = ch.lower()
        if ch_lower in counter:
            counter[ch_lower] += 1
        else:
            counter[ch_lower] = 1
    return counter

def sort_on(item):
    return item[num]

def chars_dict_sorted_list(counter):
    chars_list = []
    for ch, count in counter.items():
        dict_list = {"char": ch, "num": count}
        chars_list.append(dict_list)
    chars_list.sort(key=sort_on, reverse=True)
    return chars_list

def sort_on(item):
    return item["num"]
