'''
Import pathlib for finding file.txt,
Random for random word from file.txt,
os for cleaning terminal.
'''
import pathlib
from pathlib import Path
import random
import os

os.system('cls')


def hangman():
    '''logic game'''
    with open(Path(pathlib.Path.cwd(), 'WordsStock.txt'), encoding='utf-8') as path:
        word = random.choice([l[0:-1] for l in path])

    word_letters = list(word)
    close_word = len(word)*'_'
    used_letters = set(' ')
    all_letters = []
    attempt = 6
    os.system('cls')

    while attempt > 0:
        print('Ukraine version\n')
        print(f'Your word is {close_word.upper()} | try to guess '
        + str(close_word.count('_')) + ' letters.')
        print(f'You have an {attempt} attempts.')
        print(f'You wrote those letters: {used_letters}')
        answer = input('Guess the letter: ').lower()
        os.system('cls')
        used_letters.add(answer.upper())
        all_letters.append(answer.upper())

        for k, v in enumerate(word_letters):
            if v == answer:
                tpm = list(close_word)
                tpm[k] = v
                close_word = ''.join(tpm)

        if answer in word_letters:
            print(f'You guess the letter \'{answer.upper()}\'\n')
        elif answer not in word_letters:
            attempt -=1

        if all_letters.count(answer.upper()) > 1 and answer not in word_letters:
            print('You already use this word.\n')
            attempt += 1

        if close_word.count('_') == 0:
            print('You WIN!')
            print(f'You wrote those letters: {used_letters}')
            print(f'Your word is {close_word.upper()} | you guessed ALL ('
            + str(len(close_word)) + ') letters.')
            attempt = 0
        elif attempt == 0:
            print('You LOSE...')
            print(f'You wrote those letters: {used_letters}')
            print(f'Your word is {word.upper()} | you didn\'t guess '
            + str(close_word.count('_')) + ' letters out of ' + str(len(close_word)) + '.')

    print(game := input('Do you want to play again?[Т(так)/Н(Ні)]: '))

    while attempt == 0:
        if game.lower() == 'т':
            attempt = 6
            return hangman()
        if game.lower() == 'н':
            print('Goodbye!')
            break
        while game.lower != 'т' or game.lower != 'н':
            print('You must enter only \'Т\' or \'Н\' ')
            print(game:= input('Do you want to play again?[Т/Н]: '))
            break

hangman()
