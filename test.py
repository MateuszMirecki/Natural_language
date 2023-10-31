import nltk
from nltk.util import ngrams

def extract_ngrams(data, num):
    n_grams = ngrams(nltk.word_tokenize(data), num)
    return [ ' '.join(grams) for grams in n_grams]

# My_text = 'Jack is very good in mathematics but he is not that much good in science'

# print("1-gram of the sample text: ", extract_ngrams(My_text, 1), '\n')
# print("2-gram of the sample text: ", extract_ngrams(My_text, 2), '\n')
# print("3-gram of the sample text: ", extract_ngrams(My_text, 3), '\n')
# print("4-gram of the sample text: ", extract_ngrams(My_text, 4), '\n')