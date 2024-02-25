import random 
import string
ls=["amma","appa","samu","sr_i","kantha"]#a small list of words considered

def get_valid_word():
    wr=random.choice(ls)
    while '_'in wr or " "in wr:
        wr=random.choice(ls)
    return wr.upper()

def hangman():
    word=get_valid_word()
    wrds=set(word)
    alpabet=set(string.ascii_uppercase)
    used_wrd=set()
    while len(wrds)>0:
        print("u have used the letters"," ".join(used_wrd))

        curr_word=[letter if letter in used_wrd else "_" for letter in word]
        print("current word:"," ".join(curr_word))

        usr_inp=input("guess a letter:").upper()
        if usr_inp in alpabet - used_wrd:
            used_wrd.add(usr_inp)
            if usr_inp in wrds:
                wrds.remove(usr_inp)
        elif usr_inp in used_wrd:
            print(" u have already used this char")
        else:
            print("invalid char")
    print("u have won", curr_word)
hangman()