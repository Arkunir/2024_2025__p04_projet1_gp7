import tkinter as tk

def binaire_vers_decimal(binaire):
    decimal = 0
    for i, chiffre in enumerate(reversed(binaire)):
        decimal += int(chiffre) * (2 ** i)
    return decimal

<<<<<<< HEAD
def decimal_vers_binaire(decimal):
    if decimal == 0:
        return "0"
    binaire = ""
    while decimal > 0:
=======
def decimal_en_binaire(decimal):
    if decimal < 0:
        negatif = True
        decimal = -decimal
    else:
        negatif = False
    while decimal != 0:

>>>>>>> cff0dae7f8b0fca3e83dc5d02122b552866c3541
        binaire = str(decimal % 2) + binaire
        decimal //= 2
    return binaire

def hexadécimal_vers_decimal(hexadécimal):
    decimal = 0
    for i, chiffre in enumerate(reversed(hexadécimal)):
        if '0' <= chiffre <= '9':
            valeur = int(chiffre)
        else:
            valeur = ord(chiffre.upper()) - ord('A') + 10  # Convertit A-F en 10-15
        decimal += valeur * (16 ** i)
    return decimal

def decimal_vers_hexadécimal(decimal):
    if decimal == 0:
        return "0"
    hexadécimal = ""
    while decimal > 0:
        reste = decimal % 16
        if reste < 10:
            hexadécimal = str(reste) + hexadécimal
        else:
            hexadécimal = chr(reste - 10 + ord('A')) + hexadécimal
        decimal //= 16
    return hexadécimal

def convertir_base():
    valeur_entree = entree_valeur.get()
    base_depart = base_depart_var.get()
    base_arrivee = base_arrivee_var.get()
    
    try:
        # Conversion de la valeur d'entrée selon la base de départ
        if base_depart == "Binaire":
            decimal_value = binaire_vers_decimal(valeur_entree)
        elif base_depart == "Décimal":
            decimal_value = int(valeur_entree)
        elif base_depart == "Hexadécimal":
            decimal_value = hexadécimal_vers_decimal(valeur_entree)
        else:
            raise ValueError("Base de départ non reconnue.")
        
        # Conversion vers la base d'arrivée
        if base_arrivee == "Binaire":
            resultat = decimal_vers_binaire(decimal_value)
        elif base_arrivee == "Décimal":
            resultat = str(decimal_value)
        elif base_arrivee == "Hexadécimal":
            resultat = decimal_vers_hexadécimal(decimal_value)
        else:
            raise ValueError("Base d'arrivée non reconnue.")
        
        # Afficher le résultat
        etiquette_resultat.config(text=f"Résultat : {resultat}")
    
    except ValueError as e:
        etiquette_resultat.config(text=f"Erreur : {str(e)}")

fenetre = tk.Tk()
fenetre.title("Convertisseur de base")

etiquette_valeur = tk.Label(fenetre, text="Entrez la valeur :")
etiquette_valeur.pack()

entree_valeur = tk.Entry(fenetre)
entree_valeur.pack()

etiquette_base_depart = tk.Label(fenetre, text="De :")
etiquette_base_depart.pack()

base_depart_var = tk.StringVar()
base_depart_var.set("Binaire")
menu_base_depart = tk.OptionMenu(fenetre, base_depart_var, "Binaire", "Décimal", "Hexadécimal")menu_base_depart.pack()

etiquette_base_arrivee = tk.Label(fenetre, text="Vers :")
etiquette_base_arrivee.pack()

base_arrivee_var = tk.StringVar()
base_arrivee_var.set("Décimal")
menu_base_arrivee = tk.OptionMenu(fenetre, base_arrivee_var, "Binaire", "Décimal", "Hexadécimal")
menu_base_arrivee.pack()

bouton_convertir = tk.Button(fenetre, text="Convertir", command=convertir_base)
bouton_convertir.pack()

etiquette_resultat = tk.Label(fenetre, text="Résultat : ")
etiquette_resultat.pack()

fenetre.mainloop()