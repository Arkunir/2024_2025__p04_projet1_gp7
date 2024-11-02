import tkinter as tk

def convertir_binaire_decimal(binaire):
    decimal = 0
    for i, bit in enumerate(reversed(binaire)):
        if bit == '1':
            decimal += 2 ** i
    return decimal

def convertir_decimal_binaire(decimal):
    if decimal == 0:
        return "0"
    binaire = ""
    n = abs(decimal)
    while n > 0:
        binaire = str(n % 2) + binaire
        n //= 2
    return binaire

def convertir_decimal_hexadecimal(decimal):
    if decimal == 0:
        return "0"
    hexadecimal = ""
    n = abs(decimal)
    while n > 0:
        reste = n % 16
        if reste < 10:
            hexadecimal = str(reste) + hexadecimal
        else:
            hexadecimal = chr(reste - 10 + ord('A')) + hexadecimal
        n //= 16
    return hexadecimal

def convertir_hexadecimal_decimal(hexadecimal):
    decimal = 0
    for i, chiffre in enumerate(reversed(hexadecimal)):
        if '0' <= chiffre <= '9':
            valeur = int(chiffre)
        else:
            valeur = ord(chiffre.upper()) - ord('A') + 10
        decimal += valeur * (16 ** i)
    return decimal

def convertir_binaire_hexadecimal(binaire):
    decimal = convertir_binaire_decimal(binaire)
    return convertir_decimal_hexadecimal(decimal)

def convertir_hexadecimal_binaire(hexadecimal):
    decimal = convertir_hexadecimal_decimal(hexadecimal)
    return convertir_decimal_binaire(decimal)

def convertir_base():
    valeur_entree = entree_valeur.get()
    base_depart = base_depart_var.get()
    base_arrivee = base_arrivee_var.get()

    if valeur_entree[0] == "-":
        signe = "-"
        valeur_entree = valeur_entree[1:]
    else:
        signe = ""

    if base_depart == "Binaire":
        if not set(valeur_entree).issubset({"0", "1"}):
            etiquette_resultat.config(text="Erreur : entrée binaire invalide")
            return
    elif base_depart == "Décimal":
        if not valeur_entree.isdigit():
            etiquette_resultat.config(text="Erreur : entrée décimale invalide")
            return
    elif base_depart == "Hexadécimal":
        if not set(valeur_entree).issubset({"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"}):
            etiquette_resultat.config(text="Erreur : entrée hexadécimale invalide")
            return

    if base_depart == "Binaire" and base_arrivee == "Décimal":
        resultat = signe + str(convertir_binaire_decimal(valeur_entree))
    elif base_depart == "Binaire" and base_arrivee == "Hexadécimal":
        resultat = signe + convertir_binaire_hexadecimal(valeur_entree)
    elif base_depart == "Décimal" and base_arrivee == "Binaire":
        resultat = signe + convertir_decimal_binaire(int(valeur_entree))
    elif base_depart == "Décimal" and base_arrivee == "Hexadécimal":
        resultat = signe + convertir_decimal_hexadecimal(int(valeur_entree))
    elif base_depart == "Hexadécimal" and base_arrivee == "Binaire":
        resultat = signe + convertir_hexadecimal_binaire(valeur_entree)
    elif base_depart == "Hexadécimal" and base_arrivee == "Décimal":
        resultat = signe + str(convertir_hexadecimal_decimal(valeur_entree))
    else:
        resultat = "Erreur : conversion non prise en charge"

    etiquette_resultat.config(text="Résultat : " + resultat)

fenetre = tk.Tk()
fenetre.title("Convertisseur de base")

base_depart_var = tk.StringVar(fenetre)
base_arrivee_var = tk.StringVar(fenetre)

label_valeur = tk.Label(fenetre, text="Valeur à convertir:")
label_valeur.pack()

entree_valeur = tk.Entry(fenetre)
entree_valeur.pack()

label_base_depart = tk.Label(fenetre, text="Base de départ:")
label_base_depart.pack()

options_base = ["Binaire", "Décimal", "Hexadécimal"]
menu_base_depart = tk.OptionMenu(fenetre, base_depart_var, *options_base)
base_depart_var.set(options_base[1])  # Valeur par défaut
menu_base_depart.pack()

label_base_arrivee = tk.Label(fenetre, text="Base d'arrivée:")
label_base_arrivee.pack()

menu_base_arrivee = tk.OptionMenu(fenetre, base_arrivee_var, *options_base)
base_arrivee_var.set(options_base[0])  # Valeur par défaut
menu_base_arrivee.pack()

button_convertir = tk.Button(fenetre, text="Convertir", command=convertir_base)
button_convertir.pack()

etiquette_resultat = tk.Label(fenetre, text="Résultat : ")
etiquette_resultat.pack()

fenetre.mainloop()