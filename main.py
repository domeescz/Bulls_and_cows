import random
from datetime import datetime
start_t = datetime.now()

true = True


def pozdrav() -> None:
    print('Hi there!')

def uvod() -> None:
    pozdrav = 'I have generated random 4 digit number, lets guess that!'
    pozdrav2 = 'Lets play bulls and cows!'
    print(pozdrav)
    print(pozdrav2)
    odd = '-' * len(pozdrav)
    print(odd)

def number_is_not_numeric(cislo): #kontroluje, jestli je vstup číselný
    if cislo.isalpha():
        say = print("You didn't entered a digit number! Try it again")
        return say

def hra():
    pozdrav() #vypíše pozdrav
    uvod()  #vypíše úvodní informace

    num = "0000"  #kontrola unikátnosti náhodného čísla
    while len(set(num)) != 4:
        num = str(random.choice(range(1000, 10000)))
    #print(num)
    pocet = 0
    pocet_c = 0
    pokusy = 1
    while True:
            cislo = input('Enter a number: ')
            used = [] #list pro použitá čísla, slouží pro ošetření unikátnosti vloženého čísla
            if cislo.isalpha():
                print("You didn't entered a numeric number!")

            if cislo.isdigit() and len(str(cislo)) < 4:
                print('Number has to have lenght of 4 digits! You have less than 4.')

            elif cislo.isdigit() and len(str(cislo)) > 4:
                print('Number has to have lenght of 4 digits! You have more than 4.')

            if cislo.isdigit() and cislo == num:
                print(f"You guessed that in {pokusy} guesses.")
                return


            elif len(cislo) == 4:
                    for i, cislice in enumerate(cislo):
                        if cislice == num[i]:
                            pocet += 1


                    for i, cislice in enumerate(cislo):
                        if cislice in num and cislice != num[i]:
                            pocet_c += 1

                    print(f"{pocet} bulls and {pocet_c} cows")
                    pocet = 0
                    pocet_c = 0
                    pokusy += 1

            #else:
                #print('Not right')


hra() # spusti celý kód
stop_t = datetime.now()
print('Duration of your try: {}'.format(stop_t - start_t))