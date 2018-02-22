import os
import re

file = 'DataFiles/PyParagraph.txt'

with open(file, 'r') as text:
    print(text)

    lines = text.read()
    wordcount = len(re.findall('\w+', lines))
    sentencecount = len(re.findall('[\.?!]', lines))
    letterscount = len(re.findall('[a-zA-Z0-9]', lines))
    #letterscount = len(re.findall('\w', lines))
    print(letterscount)

print("Approximate Word Count : " + str(wordcount))
print("Approximate Sentence Count : " + str(sentencecount))
print("Average Sentence Length : " + str(wordcount/sentencecount))
print("Average Letter Count : " + str(letterscount/wordcount))
