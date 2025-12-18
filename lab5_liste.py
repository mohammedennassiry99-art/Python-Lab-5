classe = [
    ["simo", 20, 15.5],
    ["yousra", 19, 14.0],
    ["nizar", 21, 16.5],
    ["mohammed", 21, 20]
]

etudiants = ["Alice", "Bob", "Charlie"]
print(etudiants)
#Ajoute un élément à la fin avec append()
etudiants.append("Diana")
print(etudiants)
#Insère à une position précise avec insert() 
etudiants.insert(1, "Eve") 
print(etudiants)
#Supprime par valeur avec remove()
etudiants.remove("Bob")
print(etudiants) 
#Retire et récupère le dernier élément avec pop() 
dernier = etudiants.pop()
print(dernier) 
print(etudiants)

etudiants = ["Alice", "Bob", "Charlie"]
print(etudiants[0])  
print(etudiants[2]) 
print(etudiants[-1])  
print(etudiants[-2])  

notes = [12, 15, 9, 18, 14, 16]

print(notes[1:4])   
print(notes[:3])    
print(notes[3:])    
print(notes[::-1]) 

#Tri et statistiques;
classe.sort(key=lambda ligne: ligne[2], reverse=True)
print(classe)
#Recherche
somme = 0
for nom, age, note in classe:
    somme += note

moyenne_classe = somme / len(classe)
print("Moyenne de la classe est: ", moyenne_classe)

name_search = input("Entrez le nom : ")

for nom, age, note in classe:
    if nom == name_search:
        print(nom, age, note)
        break
else:
    print("Etudiant n'exsit pad dans la liste")

#copie superficielle vs profonde
classe_copie = classe[:]
classe_copie[0][1] = 99

print("Classe originale :", classe)
print("Classe copiée :", classe_copie)

import copy

classe_profonde = copy.deepcopy(classe)
classe_profonde[0][1] = 18

print("Classe originale :", classe)
print("Classe profonde :", classe_profonde)

#Conversion en dictionnaires
classe_dict = [
    {"nom": nom, "age": age, "note": note}
    for nom, age, note in classe
]

