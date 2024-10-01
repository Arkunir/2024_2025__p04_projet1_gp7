import tkinter as tk

def convertir_base():
    valeur_entree = entree_valeur.get()
    base_depart = base_depart_var.get()
    base_arrivee = base_arrivee_var.get()

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