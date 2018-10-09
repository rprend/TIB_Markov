import json
import random

file_path = "/home/rprendergast/Documents/UIUC/Projects/Tib_Markov/"
parsable_dict = {}
with open(file_path + 'uncollated_words.json','r') as uncollated_data:
    parsable_dict = json.load(uncollated_data)
final_str = ""
#parsed_dict = {"hi":["f","h"], "d":["v","zz","hi"],"f":["hi","d","d","d"],"zz":["f","f","hi"],"h":["h","ss"]}
dict_words = list(parsable_dict.keys())
first_word = random.choice(dict_words)
final_str += first_word + " "
last_word = first_word
RANGE = 650
percent = 0
percent_boop = 10
new_line_prob = 0.00
new_line_scale = 0.05
for x in range(RANGE):
    if x % (RANGE // 10) == 0:
        print("WORD #" + str(x) + ' ' + str(percent) + '%')
        percent += percent_boop
    if last_word in dict_words:
        last_word = random.choice(parsable_dict[last_word])
        if len(last_word) != 0 and last_word[-1] == '.':
            if (random.randrange(0,1) < new_line_prob):                
                last_word += '\n\t'
                new_line_prob = 0.00
            else:
                new_line_prob += new_line_scale

    else:            
        last_word = random.choice(dict_words)
    final_str += last_word + " "
with open(file_path + 'OUTPUT_ESSAY.docx', 'w') as new_essay:
    new_essay.write(final_str)