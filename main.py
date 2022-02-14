import random
from datetime import datetime
start_t = datetime.now()

true = True


def pozdrav() -> None:
    print('Hi there!')

def uvod() -> None:
    pozdrav = "I have generated random 4 digit numbers, let's guess that!"
    pozdrav2 = 'Lets play bulls and cows!'
    print(pozdrav)
    print(pozdrav2)
    odd = '-' * len(pozdrav)
    print(odd)

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
    smycka = True
    while smycka:
            cislo = input('Enter a number: ')
            used = [] #list pro použitá čísla, slouží pro ošetření unikátnosti vloženého čísla
            used_in = []

            if cislo.isdigit() and len(str(cislo)) < 4:
                print('Number has to have lenght of 4 digits! You have less than 4.')

            elif cislo.isdigit() and len(str(cislo)) > 4:
                print('Number has to have lenght of 4 digits! You have more than 4.')

            elif cislo == num:
                print(f"You guessed that in {pokusy} guesses.")
                smycka = False

            elif len(cislo) == 4 and cislo.isnumeric():
                check = []

                for i, cislice in enumerate(cislo):
                        if cislice == num[i]:   #pokud je hádané číslo na stejném indexu
                            if cislice not in used_in and cislice not in used: #kontrola, jestli již není započítaný jako cow
                                pocet += 1
                                used_in.append(cislice)
                            if cislice not in used_in and cislice in used: #pokud je již jako cow, zmenši cow o 1
                                pocet +=1
                                used_in.append(cislice)
                                pocet_c -= 1


                        elif cislice in num and cislice not in used_in and cislice != num[i]:    ## pokud je číslo v hádaném, ale není na stejném indexu
                            if cislice not in used: #pokud číslice neni v listu použitých, zapíše jí tam a připíše +1
                                used.append(cislice)
                                pocet_c += 1
                                #if cislice in used:
                                    #print("You didn't write a unique number! Try it again!")
                        check.append(cislice)

                if len(set(check)) != 4: #zkontroluj, jestli nejsou zadané duplicitní hodnoty
                    print("You entered duplicated values!")
                else:
                    pass


                print(f"{pocet} bulls and {pocet_c} cows") #na konci každého pokusu vypíše stav hádaných čísel
                pocet = 0 #resetuje trefená čísla
                pocet_c = 0
            else:
                print("You didn't entered a numeric!")

hra() # spusti celý kód
stop_t = datetime.now()
print('Duration of your try: {}'.format(stop_t - start_t))