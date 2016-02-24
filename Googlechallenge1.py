"""
Sort on sum of letters(a=1,b=2..z=26) in the word and if the sum is same then sort lexicographically.
"""
import operator

words=list()
sum_word=list()
final_names=list()

def answer(names):
    for word in names:
        temp=list()
        word=word.lower()
        for letter in word:
            if letter==" ":continue
            sum_letter=ord(letter) - 96
            temp.append(sum_letter)
        d=sum(temp)
        words.append(word)
        sum_word.append(d)
    bc=sorted(list(zip(words,sum_word)),key=operator.itemgetter(0),reverse=True)


    for k,v in sorted(bc,key=operator.itemgetter(1),reverse=True):
        final_names.append(k)
        print(k,v)
    return final_names



h=answer(["bcdal","bcdcj","a l","cj"])
print(h)