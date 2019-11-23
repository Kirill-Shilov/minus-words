from multiprocessing.dummy import Pool as ThreadPool
from datetime import datetime, date, time
from ahocorapy.keywordtree import KeywordTree
import os
import sys

class Minus_words:

    def __init__(self, filename, minus_words):
        self.filename = filename
        self.tree = KeywordTree(case_insensitive=True)
        for word in minus_words:
            self.tree.add(word)
        self.tree.finalize()

    def minus(self):
        pool = ThreadPool()
        self.pre_result = pool.map(self._minus_function, self.filename)
        self.result = filter(None, self.pre_result)
        pool.close()
        pool.join()
        return(self.result)

    def _minus_function(self, word):
        if self.tree.search(word):
            return(None)
        else:
            return(word)
        
if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        minus_file = sys.argv[2]
        minus_words = set()
        with open(minus_file, 'r', encoding='utf-8') as mf:
            for word in mf:
                minus_words.add(word.strip())
        input_file = set()
        with open(filename, 'r', encoding='utf-8') as fl:
            for word in fl:
                input_file.add(word.strip())
        minus_something = Minus_words(input_file, minus_words)
        result = minus_something.minus()
        infilename = sys.argv[1].split('/')[-1]
        result_name = '{}_{}'.format(datetime.now().strftime('%Y_%m_%d__%H_%M_%S'), infilename)
        if not os.path.isdir("results"):
            os.makedirs("results")
        with open('results/{}'.format(result_name),
                  'w', encoding='utf-8') as rf:
            for word in result:
                if word is not False:
                    rf.write('{}{}'.format(word, '\n'))
    except:
        print('/minus_words$ python3 minus/minus.py file_for_clearing minus_words_file')
