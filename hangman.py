import requests
import random

def print_word(guess_word):
    tmp_word = ""
    for n in range (len(guess_word)):
        tmp_word += guess_word[n]+" "
    print(tmp_word)

def print_human(life):
    match life:
        case 6:
            print('''
            |-----
            |    
            |
            |
            |''')
        case 5:
            print('''
            |-----
            |    O
            |
            |
            |''')
        case 4:
            print('''
            |-----
            |    O
            |    |
            |
            |''')
        case 3:
            print('''
            |-----
            |   \O
            |    |
            |
            |''')
        case 2:
            print('''
            |-----
            |   \O/
            |    |
            |
            |''')
        case 1:
            print('''
            |-----
            |   \O/
            |    |
            |   /
            |''')
        case 0:
            print('''
            |-----
            |   \O/
            |    |
            |   / \\
            |''')      

def word_define():
    word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
    response = requests.get(word_site)
    words = response.content.splitlines()
    target_word = str(random.choice(words).lower())
    target_word = target_word[2:-1]
    return target_word    

def check_char(target_word,character):
    initial_check =target_word.find(character)
    if initial_check >= 0 and initial_check < len(target_word):
        ind = [initial_check]
        continue_check = True
        while continue_check:
            #target_word = target_word[initial_check+1:]
            initial_check = target_word.find(character, initial_check+1)
            if initial_check == -1:
                continue_check = False
                return ind
            else:
                ind.append(initial_check)
    else:
        return []

def initialization():
    target_word = word_define()
    life = 6
    guess_word = []
    for character in range(len(target_word)):
        guess_word.append("_")
    print_word(guess_word)
    return target_word, guess_word, life
    
def play_routine(target_word, guess_word, life):
    #check input
    game_over = False

    while(not game_over):
        guess_char = ""
        while not len(guess_char) == 1: 
            guess_char = input("Please guess only one character: ").lower()
        
        char_found_ind = check_char(target_word,guess_char)
        if len(char_found_ind) > 0:
            for index in char_found_ind:
                guess_word[index] = guess_char
            print_word(guess_word)
        else:
            print_human(life)
            print_word(guess_word)
            life -=1
        
        if life < 0:
            game_over = True
            print(f"You Lose! The word is {target_word}")
            
        elif not "_" in guess_word:
            game_over = True
            print("You Win!")
    
def hangman():
    [target_word, guess_word, life] = initialization()    
    play_routine(target_word, guess_word, life)
    print("Game Over!!!!")

hangman()
            
            

            
        


    

        
        

