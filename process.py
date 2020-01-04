"""
this module processed the text and produces an abstract
"""

def processText(text):
    # split the text into words
    words = text.split()

    # filter words with dot
    words_with_dot = [0]
    for word in words:
        for char in word:
            if char == ".":
                words_with_dot.append(words.index(word))

    # seperate all sentences into an array
    sentences = []
    for index_i, item in enumerate(words_with_dot):
        if index_i != 0:
            if words_with_dot[index_i - 1] != 0:
                sentences.append(words[words_with_dot[index_i-1]+1:item + 1])    
            else:
                sentences.append(words[words_with_dot[index_i - 1]:item + 1])

    # next join the sentences together
    print(sentences)

    return text