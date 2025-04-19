word_count = {}

def get_book_text(fp):
    with open(fp) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    count = len(text.split())
    return count

def count_chars(text):
    text_to_lower = text.lower();
    for ch in text_to_lower:
        word_count[ch] = word_count.get(ch, 0) + 1
    
    return word_count

def sorted_chars(char_dict):
    sorted_list = sorted(char_dict.items())
    return sorted_list