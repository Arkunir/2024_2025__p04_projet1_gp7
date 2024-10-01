import tkinter as tk

# Définition des fonctions de conversion
def binaire_en_decimal(binaire):
    # Vérification des chiffres non valides
    for bit in binaire:
        if bit not in ['0', '1']:
            return f"Erreur : l'élément '{bit}' n'est pas un chiffre binaire valide."
    
    # Conversion binaire-décimale
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

binaire = "1110" #binaire ou decimal ou hexadecimal = "nombre"
decimal = binaire_en_decimal(binaire) #un autre parmi les trois = baseinitiale_en_basefinale(baseinitiale)
print(f"Le nombre en base initiale {binaire} est égal au nombre en base finale {decimal}") #print(f"Le nombre en base initiale {baseinitiale} est égal au nombre en base finale {basefinale}")