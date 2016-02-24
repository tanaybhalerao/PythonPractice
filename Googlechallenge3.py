#optimum solution
#A program which generates the shortest snippet from a phrase given a list of searched words. 
import re
from itertools import product

def answer(document, searchTerms):
    abc=dict()
    word_search=(searchword for searchword in searchTerms)
    word_ind_count=[[word,b.start()]for word in word_search for b in re.finditer(word,document)]
    for line in word_ind_count:
        if line[0] in abc:
            abc[line[0]].append(line[1])
        else:
            abc[line[0]] = [line[1]]

    mixxy=[([min(mix),max(mix)],max(mix)-min(mix)) for mix in product(*abc.values())]

    h=min(mixxy,key = lambda x:x[1])
    word_r=h[0]
    last_word = document[word_r[1]:].split()[0]
    return document[word_r[0]:word_r[1]]+last_word

j=answer("sdg bhan google program sdg google program",["google","program","sdg"])
print(j)