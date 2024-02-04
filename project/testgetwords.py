from main import getwords



strings = ["I I I are are OP",\
           "are you easy in your own mind",
           "How for Python Functions"]

unique_words = [ {'I', 'are', 'OP'},\
                 {"are", "you", "easy", "in","your", "own", "mind"},\
                 {"How", "for", "Python", "Functions"}
                ]


for string, unique_word in zip(strings, unique_words):
    indexWords = getwords(string)
    indices = list(indexWords.values())
    returnwords = set(indexWords.keys())

    assert returnwords == unique_word, f""" The Testcase: {string} fails.
    Expected Keys: {unique_word}
    Output Keys: {returnwords}
    """
    #TODO: Implement index unique checking

print( "all tests passed!" )
