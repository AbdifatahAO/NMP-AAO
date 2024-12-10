
from Terrain import Terrain, Case
from StrategieReseau import StrategieReseau, StrategieReseauAuto

class Reseau:
    def __init__(self):
        self.strat = StrategieReseauAuto()
        self.noeuds = {}
        self.arcs = []

        self.noeud_entree = -1

    def definir_entree(self, n: int) -> None:
        if n in self.noeuds.keys():
            self.noeud_entree = n
        else:
            self.noeud_entree = -1

    def ajouter_noeud(self, n: int, coords: tuple[int, int]):
        if n >= 0:
            self.noeuds[n] = coords

    def ajouter_arc(self, n1: int, n2: int) -> None:
        if n1 > n2:
            tmp = n2
            n2 = n1
            n1 = tmp
        if n1 not in self.noeuds.keys() or n2 not in self.noeuds.keys():
            return
        if (n1, n2) not in self.arcs:
            self.arcs.append((n1, n2))

    def set_strategie(self, strat: StrategieReseau):
        self.strat = strat

    def valider_reseau(self) -> bool:
    
    if not hasattr(self, 'noeud_entree') or self.noeud_entree == -1:
        return False
   
    #La fonction hasattr en Python est utilisée pour vérifier si un objet possède un attribut spécifique. Elle renvoie True si l'attribut existe, et False sinon.
    visitzs = set()
    a_visiter = [self.noeud_entree]

    while a_visiter:
        n = a_visiter.pop()
        if n not in visites:
            visites.add(n)
            voisins = [n2 for n1, n2 in self.arcs if n1 == n] + [n1 for n1, n2 in self.arcs if n2 == n]
            a_visiter.extend(voisins)

    for n in self.noeuds:
        if n not in visites:
            return False

    return True
====================
    from Terrain import Terrain, Case
from StrategieReseau import StrategieReseau, StrategieReseauAuto

class Reseau:
    def __init__(self):
        self.strat = StrategieReseauAuto()
        self.noeuds = {}
        self.arcs = []
        self.noeud_entree = -1

    def definir_entree(self, n: int) -> None:
        if n in self.noeuds.keys():
            self.noeud_entree = n
        else:
            self.noeud_entree = -1

    def ajouter_noeud(self, n: int, coords: tuple[int, int]):
        if n >= 0:
            self.noeuds[n] = coords

    def ajouter_arc(self, n1: int, n2: int) -> None:
        if n1 > n2:
            tmp = n2
            n2 = n1
            n1 = tmp
        if n1 not in self.noeuds.keys() or n2 not in self.noeuds.keys():
            return
        if (n1, n2) not in self.arcs:
            self.arcs.append((n1, n2))

    def set_strategie(self, strat: StrategieReseau):
        self.strat = strat

    def valider_reseau(self) -> bool:
        if not hasattr(self, 'noeud_entree') or self.noeud_entree == -1:
            return False

        visites = set()
        a_visiter = [self.noeud_entree]

        while a_visiter:
            n = a_visiter.pop()
            if n not in visites:
                visites.add(n)
                voisins = [n2 for n1, n2 in self.arcs if n1 == n] + [n1 for n1, n2 in self.arcs if n2 == n]
                a_visiter.extend(voisins)

        for n in self.noeuds:
            if n not in visites:
                return False

        return True


    def valider_distribution(self, t: Terrain) -> bool:
        #pas sur de ce code
        if not self.valider_reseau():
            return False

        clients_coords = t.get_clients()
        for client in clients_coords:
            client_noeud = None
            for noeud, coords in self.noeuds.items():
                if coords == client:
                    client_noeud = noeud
                    break

            if client_noeud is None:
                return False
            
            visites = set()
            a_visiter = [client_noeud]

            while a_visiter:
                n = a_visiter.pop()
                if n == self.noeud_entree:
                    break
                if n not in visites:
                    visites.add(n)
                    voisins = [n2 for n1, n2 in self.arcs if n1 == n] + [n1 for n1, n2 in self.arcs if n2 == n]
                    a_visiter.extend(voisins)
            else:
                return False

        return True
    # reseau = Reseau()
    # entree_coords = terrain.get_entree()
    # reseau.ajouter_noeud(1, entree_coords)
    # for i, client in enumerate([(1,0), (2,0), (2,5), (5,1), (5,4), (4,5)], start=2):
    # reseau.ajouter_noeud(i, client)
    # reseau.definir_entree(1)
    # for i in range(2, len(reseau.noeuds) + 1):
    # reseau.ajouter_arc(1, i)
    # reseau.afficher()
    
    
    def configurer(self, t: Terrain):
        self.noeud_entree, self.noeuds, self.arcs  = self.strat.configurer(t)

  def afficher(self) -> None:
    print("Configuration du Réseau :")
    print("Nœuds :")
    for noeud, coords in self.noeuds.items():
        print(f"  Nœud {noeud} : {coords}")
    print("Arcs :")
    for arc in self.arcs:
        print(f"  Arc entre {arc[0]} et {arc[1]}")
    
    print("Nœud d'entrée :")
    if self.noeud_entree != -1:
        print(f"  Nœud {self.noeud_entree} : {self.noeuds[self.noeud_entree]}")
    else:
        print("  Aucune entrée définie")


    def afficher_avec_terrain(self, t: Terrain) -> None:
        for ligne, l in enumerate(t.cases):
            for colonne, c in enumerate(l):
                if (ligne, colonne) not in self.noeuds.values():
                    if c == Case.OBSTACLE:
                        print("X", end="")
                    if c == Case.CLIENT:
                        print("C", end="")
                    if c == Case.VIDE:
                        print("~", end="")
                    if c == Case.ENTREE:
                        print("E", end="")
                    else:
                        print(" ", end="")
                else:
                    if c == Case.OBSTACLE:
                        print("T", end="")
                    if c == Case.CLIENT:
                        print("C", end="")
                    if c == Case.VIDE:
                        print("+", end="")
                    if c == Case.ENTREE:
                        print("E", end="")
                    else:
                        print(" ", end="")
            print()

    def calculer_cout(self, t: Terrain) -> float:
        cout = 0
        for _ in self.arcs:
            cout += 1.5
        for n in self.noeuds.values():
            if t[n[0]][n[1]] == Case.OBSTACLE:
                cout += 2
            else:
                cout += 1
        return cout

