class Piece:
    def __init__(self, couleur, x, y):
        self.couleur = couleur
        self.x = x
        self.y = y

    def deplacer(self, x, y):
        # Méthode pour déplacer la pièce
        pass

class Roi(Piece):
    def __init__(self, couleur, x, y):
        super().__init__(couleur, x, y)

    def deplacer(self, x, y):
        # Méthode pour déplacer le roi
        if abs(x - self.x) <= 1 and abs(y - self.y) <= 1:
            self.x = x
            self.y = y
        else:
            print("Le roi ne peut pas se déplacer à cette case")

class Dame(Piece):
    def __init__(self, couleur, x, y):
        super().__init__(couleur, x, y)

    def deplacer(self, x, y):
        # Méthode pour déplacer la dame
        if abs(x - self.x) == abs(y - self.y):
            self.x = x
            self.y = y
        else:
            print("La dame ne peut pas se déplacer à cette case")

class Tour(Piece):
    def __init__(self, couleur, x, y):
        super().__init__(couleur, x, y)

    def deplacer(self, x, y):
        # Méthode pour déplacer la tour
        if x == self.x or y == self.y:
            self.x = x
            self.y = y
        else:
            print("La tour ne peut pas se déplacer à cette case")

class Cavalier(Piece):
    def __init__(self, couleur, x, y):
        super().__init__(couleur, x, y)

    def deplacer(self, x, y):
        # Méthode pour déplacer le cavalier
        if abs(x - self.x) == 2 and abs(y - self.y) == 1 or abs(x - self.x) == 1 and abs(y - self.y) == 2:
            self.x = x
            self.y = y
        else:
            print("Le cavalier ne peut pas se déplacer à cette case")

class Fou(Piece):
    def __init__(self, couleur, x, y):
        super().__init__(couleur, x, y)

    def deplacer(self, x, y):
        # Méthode pour déplacer le fou
        if abs(x - self.x) == abs(y - self.y):
            self.x = x
            self.y = y
        else:
            print("Le fou ne peut pas se déplacer à cette case")

class Pion(Piece):
    def __init__(self, couleur, x, y):
        super().__init__(couleur, x, y)

    def deplacer(self, x, y):
        # Méthode pour déplacer le pion
        if self.couleur == "blanc" and x == self.x and y == self.y + 1:
            self.x = x
            self.y = y
        elif self.couleur == "noir" and x == self.x and y == self.y - 1:
            self.x = x
            self.y = y
        else:
            print("Le pion ne peut pas se déplacer à cette case")

class Echiquier:
    def __init__(self):
        self.cases = []

    def initialiser(self):
        # Méthode pour initialiser l'échiquier
        for i in range(8):
            ligne = []
            for j in range(8):
                ligne.append(None)
            self.cases.append(ligne)

    def afficher(self):
        # Méthode pour afficher l'échiquier
        for ligne in self.cases:
            for case in ligne:
                if case is None:
                    print("-", end=" ")
                else:
                    print(case.couleur[0] + case.__class__.__name__[0], end=" ")
            print()

class Jeu:
    def __init__(self):
        self.echiquier = Echiquier()
        self.joueur1 = None
        self.joueur2 = None
        self.tour = "blanc"

    def initialiser(self):
        # Méthode pour initialiser le jeu
        self.echiquier.initialiser()
        self.joueur1 = "blanc"
        self.joueur2 = "noir"
        self.placer_pieces()

    def placer_pieces(self):
        # Méthode pour placer les pièces sur l'échiquier
                for i in range(8):
            self.echiquier.cases[1][i] = Pion("blanc", i,  1)
            self.echiquier.cases[6][i] = Pion("noir", i, 6)

        self.echiquier.cases[0][0] = Tour("blanc", 0, 0)
        self.echiquier.cases[0][7] = Tour("blanc", 7, 0)
        self.echiquier.cases[7][0] = Tour("noir", 0, 7)
        self.echiquier.cases[7][7] = Tour("noir", 7, 7)

        self.echiquier.cases[0][1] = Cavalier("blanc", 1, 0)
        self.echiquier.cases[0][6] = Cavalier("blanc", 6, 0)
        self.echiquier.cases[7][1] = Cavalier("noir", 1, 7)
        self.echiquier.cases[7][6] = Cavalier("noir", 6, 7)

        self.echiquier.cases[0][2] = Fou("blanc", 2, 0)
        self.echiquier.cases[0][5] = Fou("blanc", 5, 0)
        self.echiquier.cases[7][2] = Fou("noir", 2, 7)
        self.echiquier.cases[7][5] = Fou("noir", 5, 7)

        self.echiquier.cases[0][3] = Dame("blanc", 3, 0)
        self.echiquier.cases[7][3] = Dame("noir", 3, 7)

        self.echiquier.cases[0][4] = Roi("blanc", 4, 0)
        self.echiquier.cases[7][4] = Roi("noir", 4, 7)

    def jouer(self):
        # Méthode pour jouer le jeu
        while True:
            self.echiquier.afficher()
            if self.tour == "blanc":
                print("Tour du joueur blanc")
            else:
                print("Tour du joueur noir")
            x = int(input("Entrez la colonne de la pièce à déplacer (0-7) : "))
            y = int(input("Entrez la ligne de la pièce à déplacer (0-7) : "))
            piece = self.echiquier.cases[y][x]
            if piece is not None and piece.couleur == self.tour:
                dx = int(input("Entrez la colonne de la case de destination (0-7) : "))
                dy = int(input("Entrez la ligne de la case de destination (0-7) : "))
                piece.deplacer(dx, dy)
                if self.tour == "blanc":
                    self.tour = "noir"
                else:
                    self.tour = "blanc"
            else:
                print("Impossible de déplacer cette pièce")

jeu = Jeu()
jeu.initialiser()
jeu.jouer()