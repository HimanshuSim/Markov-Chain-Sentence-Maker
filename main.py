import numpy as np
"""
from typing import TypedDict
class indexDict(TypedDict):
    word:str    # A unique word
    index:int   # its corresponding index in the lookup nexword table
"""


def getword(str_inp:str)->dict:

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
