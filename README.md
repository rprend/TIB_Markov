This parses all the This I Believe essays from thisibelieve.org and creates a Markov Chain based essay generator. 


Note that I have the TIB essays locally on my computer already, from a simple wget script based off the fact that the TIB website orders the essays 1,2,3,... You, however, don't need to worry about that, because I parsed the ~99000 essays to make uncollated_words.json. The json is a big old dictionary of form {"word": ["list","of","all","following","words"]. This json file was generated in tib_parser.py (run it on the full dataset only if you dare).

Essay_generator.py implements a simple Markov chain. Since every word w in any essay is in the dictionary, and since the corresponding value is a list of every single word that follows w in every essay,  we can follow this simple process:
1. Generate an initial random word from words_dict.keys()
2. Retrieve the list at words_dict[key]
3. Pick a random element in that list (this is a weighted probability), because multiple instances of common words will appear multiple times in the list)
4. Add to output string and be happy

TO USE:
Unzip uncollated_words.json
Run essay_generator.py with RANGE equal to the number of words you want your "essay" to be. 
Enjoy!
