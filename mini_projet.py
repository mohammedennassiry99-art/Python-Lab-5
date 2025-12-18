classe = [
    ["simo", 20, 15.5],
    ["yousra", 19, 14.0],
    ["nizar", 21, 16.5],
    ["mohammed", 21, 20]
]

def afficher_classe(classe):
    if not classe:
        print("La classe est vide.")
        return
    for index, (nom, age, note) in enumerate(classe, start=1):
        print(f"{index}. {nom} — {age} ans — note {note}")

def ajouter_etudiant(classe):
    nom = input("Nom : ").strip()
    try:
        age = int(input("Âge : "))
        note = float(input("Note : "))
    except ValueError:
        print("Saisie invalide.")
        return
    classe.append([nom, age, note])
    print(f"{nom} ajouté.")

def supprimer_etudiant(classe):
    if not classe:
        print("Rien à supprimer.")
        return
    try:
        index = int(input("Numéro de l’étudiant à supprimer : ")) - 1
        etudiant = classe.pop(index)
        print(f"{etudiant[0]} supprimé.")
    except (ValueError, IndexError):
        print("Index invalide.")

def mettre_a_jour_etudiant(classe):
    if not classe:
        print("Classe vide.")
        return
    try:
        index = int(input("Numéro de l’étudiant à modifier : ")) - 1
        etudiant = classe[index]
    except (ValueError, IndexError):
        print("Index invalide.")
        return

    print(f"Modification de {etudiant[0]} (laisser vide pour ne pas changer).")
    nouveau_nom = input("Nouveau nom : ").strip()
    if nouveau_nom:
        etudiant[0] = nouveau_nom

    entree_age = input("Nouvel âge : ").strip()
    if entree_age:
        try:
            etudiant[1] = int(entree_age)
        except ValueError:
            print("Âge ignoré (saisie invalide).")

    entree_note = input("Nouvelle note : ").strip()
    if entree_note:
        try:
            etudiant[2] = float(entree_note)
        except ValueError:
            print("Note ignorée (saisie invalide).")

def afficher_statistiques(classe):
    if not classe:
        print("Pas de données.")
        return
    notes = [etudiant[2] for etudiant in classe]
    moyenne = sum(notes) / len(notes)
    meilleure = max(classe, key=lambda e: e[2])
    pire = min(classe, key=lambda e: e[2])
    print(f"Moyenne des notes : {moyenne:.2f}")
    print(f"Meilleure note : {meilleure[2]} ( {meilleure[0]} )")
    print(f"Moins bonne note : {pire[2]} ( {pire[0]} )")

while True:
    print("\nGestion de la classe")
    print("1. Afficher tous les étudiants")
    print("2. Ajouter un étudiant")
    print("3. Supprimer un étudiant")
    print("4. Modifier un étudiant")
    print("5. Statistiques")
    print("q. Quitter")

    choix = input("Choix : ").strip().lower()

    if choix == "1":
        afficher_classe(classe)
    elif choix == "2":
        ajouter_etudiant(classe)
    elif choix == "3":
        supprimer_etudiant(classe)
    elif choix == "4":
        mettre_a_jour_etudiant(classe)
    elif choix == "5":
        afficher_statistiques(classe)
    elif choix == "q":
        print("Au revoir.")
        break
    else:
        print("Option inconnue.")