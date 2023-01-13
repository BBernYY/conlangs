ALL_WORDS = range(466550)
def load_words(indices, filename): # loads spefic range of words to save memory
    import linecache
    out = []
    for i in indices:
        out.append(linecache.getline(filename, i).replace("\n", ''))
    return out

def random_word(vowels, consonants, combination, seed): # generate a word
    import random
    random.seed(seed)
    out = ""
    for i in combination:
        # A '@' means a vowel, and a '#' means a consonant. So #@#@#@-word will guarantee a word with 3 consonants, 3 vowels, plus a suffix of -word.
        out += random.choice(vowels) if i == "@" else random.choice(consonants) if i == '#' else i
    return out

def generate_language(vowels, consonants, combination, seed): # generate a custom word for every word in the english language
    import numpy as np
    ct = 0
    a = []
    np.random.seed(seed)
    for _ in load_words(ALL_WORDS, 'words.txt'):
        ct += 1
        a.append(random_word(vowels, consonants, combination, np.random.randint(np.iinfo(np.int32).max)))
        if ct % 10000 == 0:
            open('language.lan', 'a').write("\n".join(a)+'\n')
            a = []
    open('language.lan', 'a').write("\n".join(a)+'\n')

def find_word_id(filename, word): # find the id of a word in a language
    words = open(filename, 'r').readlines()
    for i in range(len(words)):
        if words[i] == word+'\n':
            return i+1


def main(seed=None):
    import utils as ut # imports my customized utils module, with a test and timing function. https://GitHub.com/BBernYY/FancyCoding
    import numpy as np
    if seed:
        np.random.seed(seed)
    r = np.random.randint(466500)
    all_words = load_words(range(r,r+1))
    ut.timing.stop()
    return all_words


    



if __name__ == '__main__': # checks if the code is ran as a file
    from random import randint as rndnt
    import utils as ut
    n = rndnt(0, 1000)
    open('language.lan', 'wb').write(bytes())
    ut.timing.start()
    print(generate_language(['a', 'e', 'i', 'o', 'u'], ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'], '#@#@#@', 1)) # starts the main function
    wordid = find_word_id('words.txt', 'hello')
    print(load_words(range(wordid, wordid+1), 'language.lan'))
    ut.timing.stop()
