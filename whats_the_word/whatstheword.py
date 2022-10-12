import random
from typing import Counter
import requests
from bs4 import BeautifulSoup

#list of words which you dont want to have in your word pool (words not to include)
stop_list = [ "about", "blog", "contact", "find", "full", "have", "list", "need", "news", "their", "with", "your" ]

#word counter
word_count = Counter()

#webpage (adjust to the url you want to review)
base_url = 'https://www.wikipedia.org'
r = requests.get(base_url)

#parse the webpage into an element hierarchy and store in soup 
soup = BeautifulSoup(r.text, 'html.parser')

#Get only the main text of the page as list of words
pool = soup.get_text(" ", strip=True).lower().split()


#make word pool case insensitive and fish out every other symbol than small letters
count = 0
for x in range(0, len(pool)):
    for y in range(0,len(pool[x-count])):
        if ord(pool[x-count][y]) >= 65 and ord(pool[x-count][y]) <= 90:
            pool[x-count][y] = chr(ord(pool[x-count][y]) + 22)
        if ord(pool[x-count][y]) < 97 or ord(pool[x-count][y]) > 122:
            pool.remove(pool[x - count])
            count = count + 1
            break

#fish out duplicates
temp_pool = []
for x in range(0, len(pool)):
    if pool[x] not in temp_pool:
        temp_pool.append(pool[x]) 
pool = temp_pool

def checkletters(word, guess):
    word_quant    = [0] * 26  
    guess_quant   = [0] * 26
    for x in word:
        word_quant[ord(x) - 97] = word_quant[ord(x) - 97] + 1 
    for x in guess:
        guess_quant[ord(x) - 97] = guess_quant[ord(x) - 97] + 1
    for x in range(26):
        if(word_quant[x] > 0 and guess_quant[x] > 0):
            print(f'The letter {chr(x+97)} is {word_quant[x]} times in the word.') 

mistake = 0 #COUNTING FAILED GUESSES ON CURRENT RANDOM WORD
tries   = 2 #NUMBER OF TRIES PER RANDOM WORD

#############################################################################################

print('Welcome to What\'s the word?')
print(f'You chose the link {base_url}. The words to choose from are:')
print(pool)
print()
word = random.choice(pool)

while True:
    INPUT = input('What\'s the word?:')
    if INPUT.isalpha() == False:
        print(f'Input must contain ONLY letters')
    elif INPUT == word:
        print('HURRA')
        print()
        mistake = 0
        word = random.choice(pool)
    else:
        print(f'The word is wrong!')
        mistake = mistake + 1
        if mistake == tries:
            print('Loose! Next random words')
            print(f'The word was {word}.')
            print()
            mistake = 0
            word = random.choice(pool)
        else:
            checkletters(word, INPUT)