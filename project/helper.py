import numpy as np
"""
from typing import TypedDict
class indexDict(TypedDict):
    word:str    # A unique word
    index:int   # its corresponding index in the lookup nexword table
"""

class wordGenerator():

    def __init__(self, sample_str:str, **kwargs):

        self.wordlist_= self.get_word_list(self.getwords(sample_str))
        self.currword_nextwordtable_ = self.nextword_freq(sample_str)
        self.curr_next_sorted =  np.argsort(-1*self.currword_nextwordtable_)


    def getwords(self, str_inp:str)->dict:

        indexWords= dict()
        unique_words = 0

        str_inp=str_inp.rstrip()
        for line in str_inp.split('\n'):
            for word in line.split():
                if word not in indexWords:
                    indexWords[word]= unique_words
                    unique_words+=1
        return indexWords

    def get_word_list(self, indexWords:dict)->list:
        """
        Creates a List of Words to their corresponding indexes For ranking purposes
        """
        words = [0] * len(indexWords)
        for word, index in indexWords.items():
            words[index] = word

        return words

    def nextword_freq(self,str_inp:str)->dict:
        """
        str_inp
        """
        indexWords = self.getwords(str_inp)
        next_word_table = np.zeros( ( len(indexWords), len(indexWords) ) )
        str_inp=str_inp.rstrip()
        for line in str_inp.split('\n'):
            line_words = line.split()
            for i,word in enumerate(line_words[:-1]):
                # Get the next word
                next_word = line_words[i+1]
                #Get the respective index of word and the next word in the lookup table
                word_ind = indexWords[word]
                next_word_ind = indexWords[next_word]
                # Increment the value of the next word occurence corresponding to the current word
                next_word_table[word_ind, next_word_ind]+=1

        return next_word_table


    def get_next_word(self, cur_word:int )->str:
        """
        """
        pass


if __name__ == '__main__':
    pass
