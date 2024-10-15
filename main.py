def binaire_en_decimal(binaire):
    for bit in binaire:
        if bit not in ['0', '1']:
            return f"Erreur : l'élément '{bit}' n'est pas un chiffre binaire valide."
    
    decimal = 0
    for i, bit in enumerate(binaire):
        if bit == '1':
            decimal += 2 ** (len(binaire) - 1 - i)
    return decimal

def decimal_en_binaire(decimal):
    binaire = ''
    while decimal > 0:
        binaire = str(decimal % 2) + binaire
        decimal //= 2
    return binaire

def decimal_en_hexadecimal(decimal):
    if decimal is None:
        return None
    decimal = int(decimal)
    hexadecimal = ''
    while decimal > 0:
        reste = decimal % 16
        if reste < 10:
            hexadecimal = str(reste) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + reste - 10) + hexadecimal
        decimal //= 16
    return hexadecimal

def hexadecimal_en_decimal(hexadecimal):
    decimal = 0
    for i, char in enumerate(reversed(hexadecimal)):
        if char.isdigit():
            decimal += int(char) * (16 ** i)
        else:
            decimal += (ord(char) - ord('A') + 10) * (16 ** i)
    return decimal

def binaire_en_hexadecimal(binaire):
    decimal = binaire_en_decimal(binaire)
    if isinstance(decimal, str) and decimal.startswith("Erreur"):
        return decimal
    return decimal_en_hexadecimal(decimal)

def hexadecimal_en_binaire(hexadecimal):
    decimal = hexadecimal_en_decimal(hexadecimal)
    return decimal_en_binaire(decimal)

def hexa_check(s):
    """
    Checks if a string is a valid hexadecimal string with only letters from 'a' to 'f'.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a valid hexadecimal string, False otherwise.
    """
    for char in s:
        if char.isdigit() and int(char) > 9:
            return False
        elif char.lower() >= 'a' and char.lower() <= 'f':
            continue
        else:
            return False
    return True

# Example usage:
s = "1a2f"
if hexa_check(s):
    print("The string is a valid hexadecimal string.")
else:
    print("The string is not a valid hexadecimal string.")

s = "1g2f"
if hexa_check(s):
    print("The string is a valid hexadecimal string.")
else:
    print("The string is not a valid hexadecimal string.")
def convertir_base():
    valeur_entree = entree_valeur.get()
    base_depart = base_depart_var.get()
    base_arrivee = base_arrivee_var.get()

    if base_depart == "Binaire" and base_arrivee == "Décimal":
        resultat = binaire_en_decimal(valeur_entree)
    elif base_depart == "Décimal" and base_arrivee == "Binaire":
        try:
            resultat = decimal_en_binaire(int(valeur_entree))
        except ValueError:
            resultat = "Erreur : la valeur entrée n'est pas un nombre décimal valide."
    elif base_depart == "Décimal" and base_arrivee == "Hexadécimal":
        try:
            resultat = decimal_en_hexadecimal(int(valeur_entree))
        except ValueError:
            resultat = "Erreur : la valeur entrée n'est pas un nombre décimal valide."
    elif base_depart == "Hexadécimal" and base_arrivee == "Décimal":
        try:
            resultat = hexadecimal_en_decimal(valeur_entree)
        except ValueError:
            resultat = "Erreur : la valeur entrée n'est pas un nombre hexadécimal valide."
    elif base_depart == "Binaire" and base_arrivee == "Hexadécimal":
        resultat = binaire_en_hexadecimal(valeur_entree)
    elif base_depart == "Hexadécimal" and base_arrivee == "Binaire":
        try:
            resultat = hexadecimal_en_binaire(valeur_entree)
        except ValueError:
            resultat = "Erreur : la valeur entrée n'est pas un nombre hexadécimal valide."
    else:
        resultat = "Conversion de base non valide"

    etiquette_resultat.config(text="Résultat : " + str(resultat))

# Création de la fenêtre
import tkinter as tk
fenetre = tk.Tk()
fenetre.title("Convertisseur de base")

# Création des éléments de la fenêtre
etiquette_valeur = tk.Label(fenetre, text="Entrez la valeur :")
etiquette_valeur.pack()

entree_valeur = tk.Entry(fenetre)
entree_valeur.pack()

etiquette_base_depart = tk.Label(fenetre, text="De :")
etiquette_base_depart.pack()

base_depart_var = tk.StringVar()
base_depart_var.set("Binaire")
menu_base_depart = tk.OptionMenu(fenetre, base_depart_var, "Binaire", "Décimal", "Hexadécimal")
menu_base_depart.pack()

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