import random
from uzwords import words
def get_word():
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()

def display(user_letter, word):
    display_letter=""
    for letter in word:
        if letter in user_letter:
            display_letter+=letter
        else:
            display_letter+='-'
    return display_letter

def play():
    word=get_word()
    word_letter=set(word)
    user_letter=""
    print(f"Мен {len(word_letter)} хонали сўз ўйладим. Топа оласизми?")
    while len(word_letter)>0:
        print(display(user_letter, word))
        if len(user_letter)>0:
            print(f"Аввал киритган харфларингиз: {user_letter}")
        letter=input("Харф киритинг: ").upper()
        if letter in user_letter:
            print("Бу харфни аввал киритгансиз. Бошқа харф киритинг!")
            continue
        elif letter in word:
            word_letter.remove(letter)
            print(f"{letter} харфи тўғри")
        else:
            print("Афсуски бу харф йўқ")
        user_letter+=letter
    print(f"Табриклайман! {word} сўзини {len(user_letter)}та уринишда топдингиз.")

print(play())