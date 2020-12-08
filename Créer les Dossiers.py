from collections import deque
import random
import os
import numpy as np
os.chdir(r"C:\Users\NSI-SNT\Desktop\NSI-TP-master\Exercice Parcours en Largeur")
root = os.getcwd() #Naviguer avant de lancer le programme sinon ça va envahir votre dossier utilisateur

File = []
Compteur = 0
Alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
Liste = []

def MkDos(p,v,path): #path chemin dossier, p proba de créer un dossier
    global File,Compteur,Liste
    os.chdir(path)
    u = random.random()
    v = random.random()
    while u<p:
        print("Création")
        os.mkdir(str(Compteur))
        os.chdir(str(Compteur))
        # Ajouter ouvrir document avec proba v et écrire Alphabet[compteur%26]
        if random.random()<p:
            with open("text.txt","w+") as file:
                file.write(Alphabet[Compteur%26])
                Liste.append(Alphabet[Compteur%26])
        temp_path = os.getcwd()
        File.append(temp_path)
        os.chdir("..")
        u = random.random()
        Compteur +=1
    os.chdir(root)


def Boucle(v,p,t): #p proba initiale, t taux de décroissance
    global File,Compteur,Liste
    MkDos(v,p,root)
    while len(File)>0:
        pathDos = File.pop(0)
        p = max(0, p*np.exp(-t*Compteur))
        print(len(File))
        MkDos(p,v,pathDos)


#Enlever le commentaire de la ligne suivante et lancer la Fonction Boucle.

# Boucle(0.5,0.9,0.000001)




def Largeur(start):
    os.chdir(r"C:\Users\NSI-SNT\Desktop\NSI-TP-master\Exercice Parcours en Largeur")
    visited = []
    queue = deque()
    queue.append(root+'\\'+start)
    L_Lettres=[]
    while queue:
        node = queue.popleft()
        if node not in visited:
            tmp=node
            visited.append(node)
            with open(node+"\\text.txt","r") as file:
                L_Lettres.append(file.read())
            unvisited=[]
            for n in os.listdir():
                try:
                    int(n)
                    path=tmp+'\\'+str(n)
                    if path not in unvisited:
                        unvisited.append(path)
                except:
                    pass

            queue.extend(unvisited)

    return visited,L