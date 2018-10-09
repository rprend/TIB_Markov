import os
from bs4 import BeautifulSoup
import json

words_dict = {}

#96,579 total
counter = 0
file_path = "/home/rprendergast/Documents/School/TIB/"
write_path = "/home/rprendergast/Documents/UIUC/Projects/Tib_Markov/"
ranges = [500 * x for x in range(1,193)]
for x in range(1,96579):
    counter += 1
    if counter in ranges:
        print(counter)
    with open(file_path + "index.html.%d"%x) as TIB:
        unparsed_essay = BeautifulSoup(TIB,"html5lib").get_text()
#         print(unparsed_essay)
        if "Sponsor This Essay" in unparsed_essay:
            start_idx = unparsed_essay.index("Sponsor This Essay") + 19
        else:
            continue
        end_idx = unparsed_essay.index("\t\tDonate")
        parsed_essay = unparsed_essay[start_idx:end_idx]
        parsed_essay = parsed_essay.strip()
#         print(parsed_essay)
        parsed_essay_list = [a.strip() for a in parsed_essay.split(' ')]
        for idx,word in enumerate(parsed_essay_list):
            if (idx == len(parsed_essay_list) - 1):
                break
            if word not in words_dict:
                words_dict[word] = []
            words_dict[word].append(parsed_essay_list[idx+1])
            
print("WRITING TO JSON!!!!")
with open(write_path + 'uncollated_words.json','w') as uncoll_words:
    json.dump(words_dict, uncoll_words)
print("FINISHED!!!")
print(len(words_dict))
print(counter)