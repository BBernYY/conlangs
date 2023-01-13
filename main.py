def load_word(indices):
    import linecache
    out = []
    for i in indices:
        out.append(linecache.getline('words.txt', i).replace("\n", ''))
    return out

def main(seed=None):
    import utils as ut # imports my customized utils module, with a test and timing function. https://GitHub.com/BBernYY/FancyCoding
    import numpy as np
    ut.timing.start()
    if seed:
        np.random.seed(seed)
    r = np.random.randint(466500)
    all_words = load_word(range(r,r+1))
    ut.timing.stop()
    return all_words


    



if __name__ == '__main__': # checks if the code is ran as a file
    print(main()) # starts the main function
