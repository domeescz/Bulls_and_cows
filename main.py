import random
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

def hra():
    pozdrav() #vypíše pozdrav
    uvod()  #vypíše úvodní informace

    guessed = []
    num = str(random.choice(range(1000,10000)))
    guessed.append(num)
    print(num)
    pocet = 0
    pocet_c = 0
    pokusy = 1
    while True:
            cislo = str(input('Enter a number: '))

            if len(str(cislo)) < 4:
                print('Number has to have lenght of 4 digits! You have less than 4.')

            elif len(str(cislo)) > 4:
                print('Number has to have lenght of 4 digits! You have more than 4.')

            if cislo == num:
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


            else:
                print('Not right')


hra() # spusti celý kód

