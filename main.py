


import random

max_try = 10
nombre_myster = random.randint(1, 100) # Permet de choisir un nombre au hazard

for i in range(max_try): # Boucle for pour parcourir
    print("Entrer le nombre de 1 a 100 :")

    number = int(input())

    if nombre_myster == number:
        print("Gagné en", i + 1, "essai(s)") # Si le le nombre est trouver
        break
    elif number > nombre_myster:
        print("Trop grand") # Si le nombre est trop grand
    elif number < nombre_myster:
        print("Trop petit") # Si le nombre est trop petit

    if i == max_try - 1:
        print("Perdu le nombre secret est :", nombre_myster) # Si le nombre est pas trouver on annonce le nombre mystere