from datetime import date

nom = input("Nom : ")
prenom = input("Prenom : ")
date_naissance = input("Date de naissance (jj/mm/aaaa) : ")

jour, mois, annee = (int(x) for x in date_naissance.split("/"))
naissance = date(annee, mois, jour)
aujourd_hui = date.today()
age = aujourd_hui.year - naissance.year - (
    (aujourd_hui.month, aujourd_hui.day) < (naissance.month, naissance.day)
)

print("\n--- Profil ---")
print(f"Nom : {nom}")
print(f"Prenom : {prenom}")
print(f"Age : {age} ans")
