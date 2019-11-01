'''
run the following command
python -m doctest test_text_processing.txt
Testing on "short_input.txt"
>>> import TextProcessing as TP
>>> import os
>>> input_file_name = "short_input.txt"
>>> file = open(os.path.join(os.getcwd(), input_file_name), 'r', encoding="utf8")  # Opening the file
>>> file_raw_content = file.read()  # Reading the file, content will be a string
>>> file = open(os.path.join(os.getcwd(), "stop_words.txt"), 'r', encoding="utf8")  # Opening the file
>>> stop_words = file.read()  # Reading the file, content will be a string
>>> clean_content = TP.preprocess_content(file_raw_content)
>>> print(clean_content)
i initially had trouble deciding between the paperwhite and the voyage because reviews more or less said the same thing the paperwhite is great but if you have spending money go for the voyagefortunately i had friends who owned each so i ended up buying the paperwhite on this basis both models now have ppi so the dollar jump turns out pricey the voyages page press isnt always sensitive and if you are fine with a specific setting you dont need auto light adjustmentits been a week and i am loving my paperwhite no regrets the touch screen is receptive and easy to use and i keep the light at a specific setting regardless of the time of day in any case its not hard to change the setting either as youll only be changing the light level at a certain time of day not every now and then while readingalso glad that i went for the international shipping option with amazon extra expense but delivery was on time with tracking and i didnt need to worry about customs which i may have if i used a third party shipping servicepaperwhite voyage no regrets

>>> letter_freq_dict = {'i': 77, ' ': 193, 'n': 61, 't': 82, 'a': 69, 'l': 24, 'y': 25, 'h': 48, 'd': 34, 'r': 41, 'o': 51, 'u': 21, 'b': 11, 'e': 116, 'c': 19, 'g': 29, 'w': 21, 'p': 29, 'v': 15, 's': 50, 'm': 14, 'f': 13, 'j': 2, 'k': 3, 'z': 1, 'x': 2}


>>> letter_freq_dict == TP.get_letter_frequency_dict(clean_content)
True


>>> word_freq_dict = {'i': 9, 'initially': 1, 'had': 2, 'trouble': 1, 'deciding': 1, 'between': 1, 'the': 14, 'paperwhite': 4, 'and': 7, 'voyage': 2, 'because': 1, 'reviews': 1, 'more': 1, 'or': 1, 'less': 1, 'said': 1, 'same': 1, 'thing': 1, 'is': 2, 'great': 1, 'but': 2, 'if': 3, 'you': 3, 'have': 3, 'spending': 1, 'money': 1, 'go': 1, 'for': 2, 'voyagefortunately': 1, 'friends': 1, 'who': 1, 'owned': 1, 'each': 1, 'so': 2, 'ended': 1, 'up': 1, 'buying': 1, 'on': 2, 'this': 1, 'basis': 1, 'both': 1, 'models': 1, 'now': 2, 'ppi': 1, 'dollar': 1, 'jump': 1, 'turns': 1, 'out': 1, 'pricey': 1, 'voyages': 1, 'page': 1, 'press': 1, 'isnt': 1, 'always': 1, 'sensitive': 1, 'are': 1, 'fine': 1, 'with': 3, 'a': 5, 'specific': 2, 'setting': 3, 'dont': 1, 'need': 2, 'auto': 1, 'light': 3, 'adjustmentits': 1, 'been': 1, 'week': 1, 'am': 1, 'loving': 1, 'my': 1, 'no': 2, 'regrets': 2, 'touch': 1, 'screen': 1, 'receptive': 1, 'easy': 1, 'to': 3, 'use': 1, 'keep': 1, 'at': 2, 'regardless': 1, 'of': 3, 'time': 3, 'day': 2, 'in': 1, 'any': 1, 'case': 1, 'its': 1, 'not': 2, 'hard': 1, 'change': 1, 'either': 1, 'as': 1, 'youll': 1, 'only': 1, 'be': 1, 'changing': 1, 'level': 1, 'certain': 1, 'every': 1, 'then': 1, 'while': 1, 'readingalso': 1, 'glad': 1, 'that': 1, 'went': 1, 'international': 1, 'shipping': 2, 'option': 1, 'amazon': 1, 'extra': 1, 'expense': 1, 'delivery': 1, 'was': 1, 'tracking': 1, 'didnt': 1, 'worry': 1, 'about': 1, 'customs': 1, 'which': 1, 'may': 1, 'used': 1, 'third': 1, 'party': 1, 'servicepaperwhite': 1}
>>> word_freq_dict == TP.get_word_frequency_dict(clean_content)
True


>>> sort_list = sorted(['initially', 'trouble', 'deciding', 'paperwhite', 'voyage', 'reviews', 'less', 'said', 'thing', 'paperwhite', 'great', 'spending', 'money', 'go', 'voyagefortunately', 'friends', 'owned', 'ended', 'buying', 'paperwhite', 'basis', 'models', 'ppi', 'dollar', 'jump', 'turns', 'pricey', 'voyages', 'page', 'press', 'isnt', 'always', 'sensitive', 'fine', 'specific', 'setting', 'dont', 'need', 'auto', 'light', 'adjustmentits', 'week', 'loving', 'paperwhite', 'regrets', 'touch', 'screen', 'receptive', 'easy', 'keep', 'light', 'specific', 'setting', 'regardless', 'time', 'day', 'case', 'hard', 'change', 'setting', 'either', 'youll', 'changing', 'light', 'level', 'certain', 'time', 'day', 'every', 'readingalso', 'glad', 'went', 'international', 'shipping', 'option', 'amazon', 'extra', 'expense', 'delivery', 'time', 'tracking', 'didnt', 'need', 'worry', 'customs', 'may', 'used', 'third', 'party', 'shipping', 'servicepaperwhite', 'voyage', 'regrets'])
>>> sort_list == sorted(TP.get_useful_words(clean_content, stop_words))
True

>>> set_of_unique_words = set({'every', 'setting', 'fine', 'to', 'which', 'sensitive', 'need', 'hard', 'less', 'loving', 'used', 'at', 'voyagefortunately', 'tracking', 'ppi', 'models', 'that', 'of', 'third', 'a', 'dont', 'customs', 'great', 'my', 'is', 'keep', 'changing', 'worry', 'because', 'have', 'more', 'change', 'spending', 'on', 'case', 'trouble', 'day', 'now', 'no', 'shipping', 'said', 'about', 'or', 'been', 'i', 'didnt', 'voyages', 'while', 'international', 'may', 'glad', 'be', 'reviews', 'buying', 'adjustmentits', 'thing', 'same', 'ended', 'expense', 'option', 'money', 'turns', 'out', 'was', 'always', 'you', 'had', 'light', 'delivery', 'between', 'this', 'any', 'regrets', 'week', 'time', 'isnt', 'the', 'am', 'jump', 'servicepaperwhite', 'for', 'are', 'level', 'party', 'readingalso', 'friends', 'specific', 'both', 'use', 'deciding', 'paperwhite', 'pricey', 'initially', 'receptive', 'went', 'but', 'go', 'voyage', 'as', 'either', 'each', 'only', 'certain', 'amazon', 'up', 'if', 'extra', 'and', 'its', 'with', 'youll', 'then', 'page', 'auto', 'so', 'in', 'basis', 'dollar', 'touch', 'not', 'easy', 'screen', 'regardless', 'owned', 'press', 'who'})
>>> set_of_unique_words == TP.get_set_of_unique_words(clean_content)
True

>>> sorted_dict = {'paperwhite': 4, 'setting': 3, 'light': 3, 'time': 3, 'voyage': 2, 'specific': 2, 'need': 2, 'regrets': 2, 'day': 2, 'shipping': 2, 'initially': 1, 'trouble': 1, 'deciding': 1, 'reviews': 1, 'less': 1, 'said': 1, 'thing': 1, 'great': 1, 'spending': 1, 'money': 1, 'go': 1, 'voyagefortunately': 1, 'friends': 1, 'owned': 1, 'ended': 1, 'buying': 1, 'basis': 1, 'models': 1, 'ppi': 1, 'dollar': 1, 'jump': 1, 'turns': 1, 'pricey': 1, 'voyages': 1, 'page': 1, 'press': 1, 'isnt': 1, 'always': 1, 'sensitive': 1, 'fine': 1, 'dont': 1, 'auto': 1, 'adjustmentits': 1, 'week': 1, 'loving': 1, 'touch': 1, 'screen': 1, 'receptive': 1, 'easy': 1, 'keep': 1, 'regardless': 1, 'case': 1, 'hard': 1, 'change': 1, 'either': 1, 'youll': 1, 'changing': 1, 'level': 1, 'certain': 1, 'every': 1, 'readingalso': 1, 'glad': 1, 'went': 1, 'international': 1, 'option': 1, 'amazon': 1, 'extra': 1, 'expense': 1, 'delivery': 1, 'tracking': 1, 'didnt': 1, 'worry': 1, 'customs': 1, 'may': 1, 'used': 1, 'third': 1, 'party': 1, 'servicepaperwhite': 1}

>>> sorted_dict == TP.get_sorted_dict(TP.get_dictionary_of_useful_words(clean_content, stop_words))
True

>>> keywords = [('paperwhite', 4), ('setting', 3), ('light', 3), ('time', 3), ('voyage', 2), ('specific', 2), ('need', 2), ('regrets', 2), ('day', 2), ('shipping', 2)]
>>> keywords == TP.get_keywords(clean_content,stop_words)
True

'''

import os
import re

# Change everything to non-class implementations before posting
def preprocess_content(content):
   # makes a copy of the "self.content"
   clean_content = content[:]
   clean_content= clean_content.lower()  # converts everything to lowercase
   #cc= clean_content.split('.') #splits the text wherever there's a period
   #cc = (" ".join(cc))  #joins the text and replaces the periods with spaces
   cc = re.findall(r'[A-Za-z ]', clean_content) #now clean_content only includes alphabets and spaces
   clean_content = ""  #creates an empty string
   for item in cc:
       clean_content += item  #adding items in clean_content
       print(clean_content)
   return clean_content
   # remove everything but a-z/A-Z/ and spaces from the text
   # returns the cleaned content


def get_letter_frequency_dict(clean_content):
   # works on self.clean_content
   # create a dictionary of the letters and their corresponding frequencies
   fd = dict()  #creating a dictionary
   for letter in clean_content:
       if letter in fd:
           fd[letter] = fd[letter] + 1  #keeps count of the frequency
       else:
           fd[letter] = 1
   # letter_freq_dict = {'a': 0}  # dummy assignment, frequency of a is 0
   return fd  # returns a dictionary with (key: value) => (letter:frequency)


def get_word_frequency_dict(clean_content):
   # works on self.clean_content
   # create a dictionary of words and their corresponding frequencies
   word_list = clean_content.split()  #splits a string at the delimiter(whitespace)
   word_freq_dict = dict()
   for word in word_list:
       if word in word_freq_dict:
           word_freq_dict[word] = word_freq_dict[word] +1  #keeps count of the frequency
       else:
           word_freq_dict[word] = 1
   #word_freq_dict = {'dummy': 0}  # dummy assignment
   return word_freq_dict  #returns a dictionary with (key: value) => (word:frequency)


def get_set_of_unique_words(clean_content):
   # works on self.clean_content
   # returns a "set" of unique words (set here is a data structure)
   # Makes use of set
   unique_word_set = set()  # dummy assignment
   for word in get_word_frequency_dict(clean_content):
       unique_word_set.add(word)  #adds each word to unique_word_set

   return unique_word_set


def get_useful_words(clean_content, stop_words):
   # works on self.clean_content
   # returns list of NON-stopwords (see Stopwords.txt under Support_files folder)
   useful_word_list = []
   for word in get_set_of_unique_words(clean_content):
       if word not in stop_words:
           useful_word_list.append(word)  #adds each word to useful_word_list
   return useful_word_list


def get_keywords(clean_content,stop_words):
    # works on self.clean_content
    # makes use of useful words in the word dictionary
    # returns a list of UPTO 6 most frequent NON-stopwords words (see Stopwords.txt)
    possible_keywords = []  # dummy assignment
    dictionary= get_sorted_dict(clean_content) #getting words from get_sorted_dict
    for word in dictionary:
        if word not in stop_words:
            possible_keywords.append(word)
    if len(possible_keywords) < 6:  #for if there are less than six words in total then it just returns all the words with that same frequency
        return possible_keywords
    else:
        threshold= possible_keywords[5]     #if there is a tie for the sixth position, take all the words that are tied
        newlist=[]
        for i in possible_keywords:
            if dictionary[i] >= dictionary[threshold]:
                newlist.append(i)
        return newlist

def get_sorted_dict(clean_content):
    # A dictionary was considered to be unordered However, from Python 3.5+ versions, the order of elements in a
    # dictionary is the order in which they have been added To find the most frequent letter or word, you need to
    # have the dictionary sorted based on its values all the values of a dictionary can be obtained using
    # dictionary.values() You need to think about how can you get the sorted dictionary based on the frequencies (
    # values instead of keys) One way is to get the invert dictionary (see UsefulCodeBase)

    dictionary = get_word_frequency_dict(clean_content) #getting words from get_word_frequency dictionary

    sorted_dictionary = dict()  # Dummy blank dictionary

    for word in dictionary:  #inverse of dict
        value = dictionary[word]
        if value not in sorted_dictionary:
            sorted_dictionary[value] = [word]
        else:
            sorted_dictionary[value].append(word)

    tuples=[(key,sorted_dictionary[key]) for key in sorted_dictionary] #creating tuples that represent the key and value in the dictionary

    sorted_list=tuples[:]

    for i in range(len(tuples)):   #using bubble sort to sort the dictionary
        for i in range(len(tuples) - 1, 0, -1):
            for j in range(i):
                if sorted_list[j][0] < sorted_list[j + 1][0]:
                    temp = sorted_list[j]
                    sorted_list[j] = sorted_list[j + 1]
                    sorted_list[j + 1] = temp

    sorted_dictionary= dict() #converts the tuples back into a dictionary
    for i in sorted_list:
        for j in i[1]:
            sorted_dictionary[j]=i[0]


    # Do not use any ready made functions taken from online sources
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

    input_file_name = "large_input.txt"
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
    print('The list of keywords:', get_keywords(clean_content, stop_words))

import doctest
doctest.testmod()