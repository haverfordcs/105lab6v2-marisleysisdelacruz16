Course: CS 105, Fall 2019, Haverford College
Created by: Rajesh Kumar
Due Date: Midnight, October 29th, 2019
# This is pair-programming lab
# You need to read about the styles, ethics, and guidelines of pair programming in general
# This source (https://medium.com/@weblab_tech/pair-programming-guide-a76ca43ff389) is helpful

Significant Pair Programming Markers
During Pairing
    Let me drive
    Could you assist me?
    Let’s do it together
    Here’s my plan
    What plan do you have in mind?
    How does this code block work? Let’s perform unit test
    I’m tired? What’s up?
    I don’t get the point. Draw me a design
    Did we overlook something?
    Take a Short Break
    Can we take a break?
    Can we switch roles?
    Let’s go out for a cup of coffee
Remember
    Don’t force it
    Give your partner an opportunity to drive at the RIGHT time
    Encourage open communication
    Don’t ignore breaks
    Trust
    Identify your mistakes
    Criticize yourself first
    Slow down

<Member1 name: Marisleysis De La Cruz >
<Member2 name: Tazkia Afra >

Problem: implement some text processing functions
Allowed: You can use anything that is supplied to you with Python 3.7
Restrictions: You are not allowed to use any foreign package unless stated otherwise
Goal: to test your knowledge and skills in dealing with Python's basic data structures (string, list, dictionary).

Terms and Definitions:

Stop Words:
    A stop word is a commonly used word (such as “the”, “a”, “an”, “in”) that a search engine has been programmed
    to ignore, both when indexing entries for searching and when retrieving them as the result of a search query.
    See the stopwords.txt file for the list of words that you have to use.

The specific tasks that you have to accomplish are listed below:
(1) Read and understand the code in order to implement the following functions
(2) preproces_content(content): remove spaces if there is more than one space anywhere across the text
(3) get_letter_frequency_dict(clean_content): works on the cleaned_content (or preprocessed content), and returns a dictionary of frequency of each unique letter
(4) get_word_frequency_dict(clean_content): works on the cleaned_content (or preprocessed content), and returns a dictionary of frequency of each unique word
(5) get_set_of_unique_words(clean_content): returns a "set" of unique words, makes use of the set data structure
(6) get_useful_words(clean_content,stop_words): works on the cleaned content, returns list of NON-stopwords (see stopwords.txt), in other words removed stop-words from the original list of words
(7) get_keywords(clean_content): works on the useful words, and returns a list of 6 most frequent NON-stopwords words (see stopwords.txt)
(8) get_sorted_dict(dictionary): works on the dictionary obtained from the get_word_frequency
(9) Test and verify each of the functions on the short_input.txt file
(10) Report your results on the large_input.txt file

