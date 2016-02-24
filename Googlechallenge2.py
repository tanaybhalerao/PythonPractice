"""
Solution for google challenge: check for unique access codes from a list of access codes: original and reverse words are considered same.
"""
def answer(x):
    wordlist=list(set(x))
    for word in wordlist:
        word_rev=word[::-1]
        if word_rev!=word_rev[::-1]:
            if word_rev in wordlist:
                wordlist.remove(word_rev)
            else:
                 pass
    return len(wordlist)