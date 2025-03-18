def word_count(string):
    count = len(string.split())
    return f"Found {count} total words"

def char_count(string):
    conv_string = string.lower()
    d = {}
    for char in conv_string:
        if char in d:
            d[char] = d[char] + 1
        else:
            d[char] = 1
    
    return d

def sort_chars(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))