# read the input file as a string
# replace the \n with  spaces
# split at the spaces
# make a set of the resulting list
# remove the non-letters begnning of the words
# order the set
# join the set into a string
# output it to a file

import re
import sys

def word_set(input_file):
    with open(input_file) as x:
        file_string=x.read()

    file_string=file_string.replace('\n',' ')
    file_string=file_string.replace('-',' ')
    words_list=file_string.split(' ')
    initial_word_set=set(words_list)
    #mapping the initial set to a new set with clean begnning and ends from non-letters
    word_set=set(map(lambda x: re.sub('(.*?)([a-z].*[a-z])(.*)', '\\2', x, flags=re.IGNORECASE) , initial_word_set))
    #note: the filtering isnt very clean, but as an initial its good enough
    word_set=sorted(word_set)
    with open('output.txt','w') as x:
        x.write( 'number of words:'+str(len(word_set))+'\n\n'+ ' '.join(word_set))

word_set(sys.argv[1])
