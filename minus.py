from multiprocessing.dummy import Pool as ThreadPool
from datetime import datetime, date, time
import os
import sys

def minus_fn_closure(minus_fn, minus_words):
    return minus_fn

def minus_fn(word):
    success = True
    for minus_word in minus_words:
        if minus_word in word.lower():
            success = False
            return False
            break
    if success is True:  
        return word 

if __name__ == "__main__":
    try:
        filename = sys.argv[1]
        minus_file = sys.argv[2]
        minus_words = set()
        with open(minus_file, 'r', encoding='utf-8') as mf:
            for wrd in mf:
                minus_words.add(str(wrd.strip().lower()))

        input_file = set()
        with open(filename, 'r', encoding='utf-8') as fl:
            for wrd in fl:
                input_file.add(str(wrd.strip()))
        
        final_minus_function = minus_fn_closure(minus_fn, minus_words)
        pool = ThreadPool()
        result = pool.map(final_minus_function, input_file)
        pool.close()
        pool.join()
        infilename = sys.argv[1].split('/')[-1]
        result_name = '{}_{}'.format(infilename,
            datetime.now().strftime('%Y_%m_%d__%H_%M_%S'))
        with open('results/{}'.format(result_name),
                  'w', encoding='utf-8') as rf:
            for word in result:
                if word is not False:
                    rf.write('{}{}'.format(word, '\n'))
    except:
        print('python3 minus.py file_for_clearing minus_words_file')
