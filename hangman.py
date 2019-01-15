import random

def main():
    LIFE = 10
    WORDS = []
    
    with open('Data/words.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            WORDS.append(line)
    
    game_not_exit = True
    while game_not_exit:
        # Get word
        word = random.choice(WORDS)
        block = '_' * len(word)
        guess_time = 0
        guessed = []
        not_got_it = True
        
        # Guess
        while not_got_it and guess_time < LIFE:
            print('Word: ' + block)
            if len(guessed) > 0:
                print('Guessed: ' + ' '.join(guessed))
            ch = '0'
            
            # Get char
            while not ch.isalpha() or ch in guessed:
                ch = input('Guess a alphabet: ')[0]
            guessed.append(ch)
            
            # Check
            get_ch = False
            for i in range(len(word)):
                if word[i] == ch:
                    block = block[:i] + ch + block[i + 1:]
                    get_ch = True
            
            if word == block:
                not_got_it = False
            
            if not get_ch:
                guess_time = guess_time + 1
                print('Wrong alphabet, {} time(s) left!\n'.format(LIFE - guess_time))
            else:
                print('')
        
        if not_got_it:
            print('You lose! It\'s {}.'.format(word))
        else:
            print('You win! It\'s {}.'.format(word))
        
        yes_or_no = input('Wanna play again?[y/n] ')
        if not yes_or_no.lower() == 'y':
            game_not_exit = False
        print('\n')

if __name__ == '__main__':
    main()