import os


# Change everything to non-class implementations before posting
def preprocess_content(content):
    # makes a copy of the "self.content"
    cleaned_content = content[:]
    # remove everything but a-z/A-Z/ and spaces from the text
    # returns the cleaned content
    return cleaned_content


def get_letter_frequency_dict(clean_content):
    # works on self.clean_content
    # create a dictionary of the letters and their corresponding frequencies
    # returns a dictionary with (key: value) => (letter:frequency)
    letter_freq_dict = {'a': 0}  # dummy assignment, frequency of a is 0
    return letter_freq_dict


def get_word_frequency_dict(clean_content):
    # works on self.clean_content
    # create a dictionary of words and their corresponding frequencies
    # returns a dictionary with (key: value) => (word:frequency)
    word_freq_dict = {'dummy': 0}  # dummy assignment
    return word_freq_dict


def get_set_of_unique_words(clearn_content):
    # works on self.clean_content
    # returns a "set" of unique words (set here is a data structure)
    # Makes use of set
    unique_word_set = set()  # dummy assignment
    return unique_word_set


def get_useful_words(clean_content, stop_words):
    # works on self.clean_content
    # returns list of NON-stopwords (see Stopwords.txt under Support_files folder)

    useful_word_list = []  # dummy assignment
    return useful_word_list


def get_keywords(clean_content):
    # works on self.clean_content
    # makes use of useful words in the word dictionary
    # returns a list of UPTO 6 most frequent NON-stopwords words (see Stopwords.txt)
    possible_keywords = []  # dummy assignment
    return possible_keywords


def get_sorted_dict(dictionary):
    # A dictionary was considered to be unordered However, from Python 3.5+ versions, the order of elements in a
    # dictionary is the order in which they have been added To find the most frequent letter or word, you need to
    # have the dictionary sorted based on its values all the values of a dictionary can be obtained using
    # dictionary.values() You need to think about how can you get the sorted dictionary based on the frequencies (
    # values instead of keys) One way is to get the invert dictionary (see UsefulCodeBase)
    sorted_dictionary = dict()  # Dummy blank dictionary
    # Do not ue any ready made functions taken from online sources
    # Develop your own logic and explain it in your comments.
    return sorted_dictionary


# Helper function to print a dictionary (line by line)
def print_dictionary(dict_in):
    for key in dict_in:
        print(key, ': ', dict_in[key])


# ***************Everything before this remains the same********************#
if __name__ == "__main__":
    # Reading stop words
    # In computing, stop words are words which are filtered out before processing of natural language data (text).[1]
    # Stop words are generally the most common words in a language; there is no single universal list of stop words used
    # by all natural language processing tools, and indeed not all tools even use such a list. Some tools avoid removing
    # stop words to support phrase search. Read more https://en.wikipedia.org/wiki/Stop_words
    stop_word_file = "stop_words.txt"
    file = open(os.path.join(os.getcwd(), stop_word_file), 'r',
                encoding="utf8")
    stop_words = file.read()

    input_file_name = "short_input.txt"
    file = open(os.path.join(os.getcwd(), input_file_name), 'r', encoding="utf8")  # Opening the file
    file_raw_content = file.read()  # Reading the file, content will be a string
    print(file_raw_content)  # comment this line if you dont want to see the content
    clean_content = preprocess_content(file_raw_content)  # Implement preprocess() function to get the clean content
    print(clean_content)  # comment this line if you dont want to see the clean_content
    print('The dictionary of letter freq:')
    print_dictionary(get_letter_frequency_dict(clean_content))
    print('The dictionary of word freq:')
    print_dictionary(get_word_frequency_dict(clean_content))
    print('Useful words:', get_useful_words(clean_content, stop_words))
    print('Unique words:', get_set_of_unique_words(clean_content))
    print('The sorted dictionary:')
    print_dictionary(get_sorted_dict(clean_content))
    print('The list of keywords:', get_keywords(clean_content))

