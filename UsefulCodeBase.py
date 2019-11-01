# printing the frequency of vowels appeared in a text file
vlist = 'aeiou'
filepath = 'large_input.txt'
file = open(filepath, 'r', encoding="utf8")
file_content = file.read()
file_content = file_content.lower()

def get_inverted_dict(d):
    inverse = dict()
    # this invert will work only if you have only one value mapped to a key
    # In the case of dictionary of frequency of word or letter, there would be one-on-one mapping between keys and values
    # We will have only one frequency for each word or each letter
    for key in d:
        inverse[d[key]] = key
    return inverse

def get_freq_dict(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


if __name__ == "__main__":
    aplha_dict = get_freq_dict(file_content)
    print(aplha_dict)
    print(get_inverted_dict(aplha_dict))
