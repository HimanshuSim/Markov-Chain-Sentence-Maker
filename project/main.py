import numpy as np
"""
from typing import TypedDict
class indexDict(TypedDict):
    word:str    # A unique word
    index:int   # its corresponding index in the lookup nexword table
"""


def getwords(str_inp:str)->dict:

    indexWords= dict()
    unique_words = 0

    str_inp=str_inp.rstrip()
    for line in str_inp.split('\n'):
        for word in line:
            if word not in dict:
                dict[word]= unique_words
                unique_words+=1
    return indexWords


def nextword_freq(str_inp:str)->dict:
    """
    str_inp
    """
    indexWords = getword(str_inp)
    next_word_table = np.zeros( ( len(indexWords), len(indexWords) ) )
    str_inp=str_inp.rstrip()
    for line in str_inp.split('\n'):
        for i,word in enumerate(line[:-1]):
            # Get the next word
            next_word = line[i+1]
            #Get the respective index of word and the next word in the lookup table
            word_ind = indexWords[word]
            next_word_ind = indexWords[next_word]
            # Increment the value of the next word occurence corresponding to the current word
            next_word_table[word_ind, next_word_ind]+=1

    return next_word_table

def get_word_list(indexWords:dict):
    """
    Creates a List of Words to their corresponding indexes For ranking purposes
    """
    words = [0] * len(indexWords)

    for word, index in indexWords:
        words[index] = word

    return words
## Showing the possible coupling for a conversion to class abstraction in the future

#indexWords_ = getwords()
#WORD_LIST = get_word_list(indexWords_)


def get_next_word_votes(word_table:np.ndarray)->np.ndarray:
"""
Get back the sorted of next words corresponding to the word in the given row index
"""
    pass

def get_next_word(cur_word:str , word_list: list ,word_table)->str:
"""
"""
    pass
