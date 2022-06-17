import pathlib
from pathlib import Path
import random

path = open(Path(pathlib.Path.cwd(), 'WordsStock.txt'), encoding='utf-8')


def henagman():
    word = 'nemera'  #  (random.choice([l[0:-1] for l in path])
    word_latters = list(word.lower())
    close_word = len(word)*'_' 
    used_latters = list()
    attempt = 5

    print(f'Your word is {close_word} | has ' + str(close_word.count('_')) + ' latters.')
    answer = input('Guess the latter: ')
    used_latters.append(answer.upper())

    if answer.lower() in word_latters:
        for k, v in enumerate(word_latters):
            if v == answer.lower():
                tpm = [l for l in (close_word)]
                tpm[k] = v
                close_word = ''.join(tpm)
    return close_word 


print(henagman())