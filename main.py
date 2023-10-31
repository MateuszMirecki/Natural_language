from utils import split_file_by_commas, count_and_multiply_words, extract_ngrams
import statistics
from collections import Counter

wojnicz = split_file_by_commas("Wojnicz.txt")
wikipedia = split_file_by_commas("uklad_sloneczny.txt")

count_wojnicz = count_and_multiply_words(wojnicz)
count_wikipedia = count_and_multiply_words(wikipedia)

# wojnicz_zipf = []
# wikipedia_zipf = []

# for elem in count_wikipedia:
#     wikipedia_zipf.append(elem[2])

# for elem in count_wojnicz:
#     wojnicz_zipf.append(elem[2])

# min_wiki = min(wikipedia_zipf)
# max_wiki = max(wikipedia_zipf)
# min_wojnicz = min(wojnicz_zipf)
# max_wojnicz = max(wojnicz_zipf)

# biggest_diff_wiki = max_wiki - min_wiki
# biggest_diff_wojnicz = max_wojnicz - min_wojnicz

# odcylenie_wiki = statistics.stdev(wikipedia_zipf)
# odcylenie_wojnicz = statistics.stdev(wojnicz_zipf)

# print(f"Min zipf value for wikipedia text is {min_wiki}")
# print(f"Min zipf value for wikipedia text is {max_wiki}")
# print(f"Max difference zipf for wikipedia is {biggest_diff_wiki}")
# print(f"Odchylenie wiki is {odcylenie_wiki}")

# print(f"Min zipf value for wojnicz text is {min_wojnicz}")
# print(f"Min zipf value for wojnicz text is {max_wojnicz}")
# print(f"Max difference zipf for wojnicz is {biggest_diff_wiki}")
# print(f"Odchylenie wojnicz is {odcylenie_wojnicz}")

woj_txt = ' '.join(wojnicz).lower()
wiki_txt = ' '.join(wikipedia).lower()


ngrams = True
wiki_ngrams = []
i=0
while(ngrams):
    temp_ngrams = extract_ngrams(wiki_txt, i+2)
    temp_ngrams_unique = list(set([i for i in temp_ngrams if temp_ngrams.count(i)>1]))
    wiki_ngrams.append(temp_ngrams_unique)
    if len(wiki_ngrams[i])>0:
        pass
    else:
        ngrams = False
    i+=1


for j in range(len(wiki_ngrams)-1):
    elems_to_remove = [] 
    for elem in wiki_ngrams[j]:
        for elem2 in wiki_ngrams[j+1]:
            if elem in elem2:
                elems_to_remove.append(elem)
    for elem in list(set(elems_to_remove)):
        wiki_ngrams[j].remove(elem)


# print(wiki_ngrams)

# elems_to_remove = list(set(elems_to_remove))
# for elem in elems_to_remove:
#     wiki_2.remove(elem)


# elems_to_remove = [] 
# for elem in wiki_3:
#     for elem2 in wiki_4:
#         if elem in elem2:
#             elems_to_remove.append(elem)

# elems_to_remove = list(set(elems_to_remove))
# for elem in elems_to_remove:
#     wiki_3.remove(elem)

# print(len(wiki_2))
# print(len(wiki_3))



# woj_2_grams = extract_ngrams(woj_txt, 2)
# woj_3_grams = extract_ngrams(woj_txt, 3)
# woj_4_grams = extract_ngrams(woj_txt, 4)

# woj_2 = set([i for i in woj_2_grams if woj_2_grams.count(i)>1])
# woj_3 = set([i for i in woj_3_grams if woj_3_grams.count(i)>1])
# woj_4 = set([i for i in woj_4_grams if woj_4_grams.count(i)>1])

# # Use Counter to count occurrences
# element_count_wojnicz = Counter(wojnicz)

# # Get the top 10 most occurring elements
# top_20_elements_wojnicz = element_count_wojnicz.most_common(20)

# # Display the results
# for element, count in top_20_elements_wojnicz:
#     print(f"Element {element}: Count {count}")


# # Use Counter to count occurrences
# element_count_wiki = Counter(wojnicz)

# # Get the top 10 most occurring elements
# top_20_elements_wiki = element_count_wiki.most_common(20)

# # Display the results
# for element, count in top_20_elements_wiki:
#     print(f"Element {element}: Count {count}")

# Use Counter to count occurrences
element_count = Counter(wikipedia)

# Get the top 10 most occurring elements
top_20_elements = [element for element, count in element_count.most_common(20)]

# Create a dictionary to count unique elements on the next index for each top element
unique_element_count = {element: 0 for element in top_20_elements}

for i in range(1, len(wikipedia)):
    current_element = wikipedia[i]
    next_element = wikipedia[i - 1]

    if current_element in top_20_elements and next_element not in top_20_elements:
        unique_element_count[current_element] += 1

# Display the results
for element, count in unique_element_count.items():
    print(f"Element {element}: {count} unique elements index before")


