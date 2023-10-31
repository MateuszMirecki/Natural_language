
def split_file_by_commas(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            # Read the file content
            file_content = file.read()

            # Split the content by commas
            elements = file_content.split(',')
            
            return elements
    except FileNotFoundError:
        return None

# Example usage:
# filename = 'Wojnicz.txt'
# result = split_file_by_commas(filename)

# if result is not None:
#     print("Elements:", result)
# else:
#     print(f"File '{filename}' not found.")



from collections import Counter

def count_and_multiply_words(arr):
    word_counts = Counter(arr)
    
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    counts = [count for _, count in sorted_words]
    
    results = [count * (index + 1) for index, count in enumerate(counts)]
    
    word_results = [[word, count, result] for (word, _), count, result in zip(sorted_words, counts, results)]
    
    return word_results

# word_array = ["apple", "banana", "apple", "cherry", "banana", "apple"]
# word_results = count_and_multiply_words(word_array)
# for word, count, result in word_results:
#     print(f"({word}, {count}, {result})")


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

