import pyautogui
import time
import random
import keyboard
import win32api, win32con

#TODO : bouclier auto, reset quetes guild fest, combat monstre auto, recherche chateaux, detecte attaque


#Toutes les fonctions:

def EnterCo(x:str):
    if x=='1':
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('1.png', confidence=0.8))#met le curseur sur 1
        pyautogui.click()#clique sur 1
    elif x=='2':
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('2.png', confidence=0.8))#met le curseur sur 2
        pyautogui.click()#clique sur 2 
    elif x=='3':
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('3.png', confidence=0.8))#met le curseur sur 3
        pyautogui.click()#clique sur 3
    elif x=='4':
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('4.png', confidence=0.8))#met le curseur sur 4
        pyautogui.click()#clique sur 4
    elif x=='5':
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('5.png', confidence=0.8))#met le curseur sur 5
        pyautogui.click()#clique sur 5
    elif x=='6':
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('6.png', confidence=0.8))#met le curseur sur 6
        pyautogui.click()#clique sur 6
    elif x=='7':
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('7.png', confidence=0.8))#met le curseur sur 7
        pyautogui.click()#clique sur 7
    elif x=='8':
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('8.png', confidence=0.8))#met le curseur sur 8
        pyautogui.click()#clique sur 8
    elif x=='9':
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('9.png', confidence=0.8))#met le curseur sur 9
        pyautogui.click()#clique sur 9
    elif x=='0':
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('0.png', confidence=0.8))#met le curseur sur 0
        pyautogui.click()#clique sur 0

def move(letter:str,x:int):
    tab=[chiffre for chiffre in str(x)]
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('Loupe.png', confidence=0.8))#met le curseur sur la loupe
    pyautogui.click() #clique sur la loupe pour rechercher un territoire
    time.sleep(0.1)
    if letter == 'x':
        pyautogui.moveTo(937,400)#place le curseur sur la valeur de X
        pyautogui.click() #clique sur la valeur de X
        time.sleep(0.1)
        for i in tab:
            EnterCo(i)# Saisi les coordonnées de X
            time.sleep(0.1)
    elif letter == 'y':
        pyautogui.moveTo(1100,400)  #place le curseur sur la valeur de Y
        pyautogui.click()   #clique sur la valeur de Y
        time.sleep(0.1)
        for i in tab:
            EnterCo(i)  #Saisi les coordonnées de Y
            time.sleep(0.1)
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('Valid.png', confidence=0.8))#met le curseur sur "Valider"
    pyautogui.click()   #clique sur "Valider"
    time.sleep(0.1)
    pyautogui.moveTo(937,550)#met le curseur sur "OK"
    pyautogui.click()   #clique sur "OK"
    time.sleep(0.1)

def collecte():
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('Coll.png', confidence=0.6))#met le curseur sur collecter
    pyautogui.click()#clique sur collecter
    time.sleep(0.5)
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('Groupe_Auto.png', confidence=0.5))#met le curseur sur groupe auto
    pyautogui.click()#clique sur groupe auto
    time.sleep(0.5)
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('Deployer.png', confidence=0.6))#met le curseur sur deployer
    pyautogui.click()#clique sur deployer
    time.sleep(0.5)

def OreOnScreen():
    try:
        if pyautogui.locateOnScreen('Ore_Dirt.png', confidence=0.4) is not None :   #detecte les filons de minerais sur les pistes de magma
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('Ore_Dirt.png', confidence=0.6))    #met le curseur sur le filon
            pyautogui.click()   #Clique sur le filon
            time.sleep(0.5)
            collecte()
        elif pyautogui.locateOnScreen('Ore_Grass.png', confidence=0.4) is not None :    #detecte les filons de minerais sur les prairies
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('Ore_Grass.png', confidence=0.6))   #met le curseur sur le filon
            pyautogui.click()   #Clique sur le filon
            time.sleep(0.5)
            collecte()
        elif pyautogui.locateOnScreen('Ore_Snow.png', confidence=0.4) is not None:  #detecte les filons de minerais sur la neige
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('Ore_Snow.png', confidence=0.6))   #met le curseur sur le filon
            pyautogui.click()   #Clique sur le filon
            time.sleep(0.5)
            collecte()
    except pyautogui.ImageNotFoundException:    #Pour ne pas renvoyer de msg d'erreur
        time.sleep(0.5)

def GoldOnScreen():
    try:
        if pyautogui.locateOnScreen('Gold_Dirt.png', confidence=0.4) is not None :   #detecte les filons d'or sur les pistes de magma
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('Gold_Dirt.png', confidence=0.6))    #met le curseur sur le filon
            pyautogui.click()   #Clique sur le filon
            time.sleep(0.5)
            collecte()
        elif pyautogui.locateOnScreen('Gold_Grass.png', confidence=0.4) is not None :    #detecte les filons d'or sur les prairies
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('Gold_Grass.png', confidence=0.6))   #met le curseur sur le filon
            pyautogui.click()   #Clique sur le filon
            time.sleep(0.5)
            collecte()
        elif pyautogui.locateOnScreen('Gold_Snow.png', confidence=0.4) is not None:  #detecte les filons d'or sur la neige
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('Gold_Snow.png', confidence=0.6))   #met le curseur sur le filon
            pyautogui.click()   #Clique sur le filon
            time.sleep(0.5)
            collecte()
    except pyautogui.ImageNotFoundException:    #Pour ne pas renvoyer de msg d'erreur
        time.sleep(0.5)

def FoodOnScreen():
    try:
        if pyautogui.locateOnScreen('Food_Dirt.png', confidence=0.4) is not None :   #detecte les champs sur les pistes de magma
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('Food_Dirt.png', confidence=0.6))    #met le curseur sur le champs
            pyautogui.click()   #Clique sur le filon
            time.sleep(0.5)
            collecte()
        elif pyautogui.locateOnScreen('Food_Grass.png', confidence=0.4) is not None :    #detecte les champs sur les prairies
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('Food_Grass.png', confidence=0.6))   #met le curseur sur le champs
            pyautogui.click()   #Clique sur le filon
            time.sleep(0.5)
            collecte()
        elif pyautogui.locateOnScreen('Food_Snow.png', confidence=0.4) is not None:  #detecte les champs sur la neige
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('Food_Snow.png', confidence=0.6))   #met le curseur sur le champs
            pyautogui.click()   #Clique sur le filon
            time.sleep(0.5)
            collecte()
    except pyautogui.ImageNotFoundException:    #Pour ne pas renvoyer de msg d'erreur
        time.sleep(0.5)

def WoodOnScreen():
    try:
        if pyautogui.locateOnScreen('Wood_Dirt.png', confidence=0.4) is not None :   #detecte les forets sur les pistes de magma
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('Wood_Dirt.png', confidence=0.6))    #met le curseur sur la foret
            pyautogui.click()   #Clique sur le filon
            time.sleep(0.5)
            collecte()
        elif pyautogui.locateOnScreen('Wood_Grass.png', confidence=0.4) is not None :    #detecte les forets sur les prairies
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('Wood_Grass.png', confidence=0.6))   #met le curseur sur la foret
            pyautogui.click()   #Clique sur le filon
            time.sleep(0.5)
            collecte()
        elif pyautogui.locateOnScreen('Wood_Snow.png', confidence=0.4) is not None:  #detecte les forets sur la neige
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('Wood_Snow.png', confidence=0.6))   #met le curseur sur la foret
            pyautogui.click()   #Clique sur le filon
            time.sleep(0.5)
            collecte()
    except pyautogui.ImageNotFoundException:    #Pour ne pas renvoyer de msg d'erreur
        time.sleep(0.5)

def StoneOnScreen():
    try:
        if pyautogui.locateOnScreen('Stone_Dirt.png', confidence=0.4) is not None :   #detecte les carrieres sur les pistes de magma
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('Stone_Dirt.png', confidence=0.6))    #met le curseur sur la carriere
            pyautogui.click()   #Clique sur le filon
            time.sleep(0.5)
            collecte()
        elif pyautogui.locateOnScreen('Stone_Grass.png', confidence=0.4) is not None :    #detecte les carrieres sur les prairies
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('Stone_Grass.png', confidence=0.6))   #met le curseur sur la carriere
            pyautogui.click()   #Clique sur le filon
            time.sleep(0.5)
            collecte()
        elif pyautogui.locateOnScreen('Stone_Snow.png', confidence=0.4) is not None:  #detecte les carrieres sur la neige
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('Stone_Snow.png', confidence=0.6))   #met le curseur sur la carriere
            pyautogui.click()   #Clique sur le filon
            time.sleep(0.5)
            collecte()
    except pyautogui.ImageNotFoundException:    #Pour ne pas renvoyer de msg d'erreur
        time.sleep(0.5)

def helpGuild():
    try:
        if pyautogui.locateOnScreen('Help.png', confidence=0.8) is not None:    #verifie si il y a des demandes d'aide
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('Help.png', confidence=0.8))    #met le curseur sur les aides
            pyautogui.click()   #clique sur les aides
            time.sleep(0.1)
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('Help_All.png', confidence=0.8))   #met le curseur sur aider tout le monde
            pyautogui.click()   #clique sur aider tout le monde
            time.sleep(0.1)
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('Cross.png', confidence=0.8))   #met le curseur sur la croix
            pyautogui.click()   #clique sur la croix
            time.sleep(0.1)
    except pyautogui.ImageNotFoundException:
        time.sleep(0.1)

def boucli():
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('Ligne_Bas.png', confidence=0.8))
    pyautogui.click()   #deploie la ligne du bas
    time.sleep(0.1)
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('Bag.png', confidence=0.8))
    pyautogui.click()   #va dans le sac
    time.sleep(0.1)
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('Combat.png', confidence=0.8))
    pyautogui.click()   #vas dans la partie "Combat" du sac
    time.sleep(0.1)
    try:
        if pyautogui.locateOnScreen('Shield_4.png', confidence=0.7) is not None: #regarde si il y a des boucliers 4h dans le sac
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('Util_Shield_4h.png', confidence=0.7))
            pyautogui.click()   #clique sur "Utiliser"
            time.sleep(0.1)
        elif pyautogui.locateOnScreen('Shield_8.png', confidence=0.7) is not None: #regarde si il y a des boucliers 8h dans le sac
            pyautogui.moveTo(pyautogui.locateCenterOnScreen('Util_Shield_8h.png', confidence=0.7))
            pyautogui.click()   #clique sur "Utiliser"
            time.sleep(0.1)
    except pyautogui.ImageNotFoundException:
        time.sleep(0.1)
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('Cross.png', confidence=0.8))
    pyautogui.click()   #clique sur la croix
    time.sleep(0.1)
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('Ligne_Bas.png', confidence=0.8))
    pyautogui.click()   #retire la ligne du bas
    time.sleep(0.1)
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('Ligne_Bas.png', confidence=0.8))
    pyautogui.click()   #retire la ligne du bas
    time.sleep(0.1)

def hunt(lvl:int,x:int,y:int):
    pyautogui.moveTo(pyautogui.locateCenterOnScreen('See_All.png', confidence=0.7))
    pyautogui.click()
    time.sleep(0.1)
    try:
        if pyautogui.locateOnScreen('Hunt_Full.png', confidence=0.8) is not None: #regarde si la jauge d'energie est remplie
            move('x',x)
            move('y',y)
            if lvl == 1:
                try:
                    if pyautogui.locateOnScreen('Monster_1.png', confidence=0.7) is not None:
                        pyautogui.moveTo(pyautogui.locateCenterOnScreen('Monster_1.png', confidence=0.7))
                        pyautogui.click()
                        time.sleep(0.2)
                        pyautogui.moveTo(pyautogui.locateCenterOnScreen('Attaque_Monstre_Groupe.png', confidence=0.7))
                        pyautogui.click()
                        time.sleep(0.5)
                        pyautogui.moveTo(pyautogui.locateCenterOnScreen('Deployer_Monstres.png', confidence=0.7))
                        pyautogui.click()
                        time.sleep(2.5)
                except pyautogui.ImageNotFoundException:
                    time.sleep(0.1)
            if lvl == 2:
                try:
                    if pyautogui.locateOnScreen('Monster_2.png', confidence=0.7) is not None:
                        pyautogui.moveTo(pyautogui.locateCenterOnScreen('Monster_2.png', confidence=0.7))
                        pyautogui.click()
                        time.sleep(0.2)
                        pyautogui.moveTo(pyautogui.locateCenterOnScreen('Attaque_Monstre_Groupe.png', confidence=0.7))
                        pyautogui.click()
                        time.sleep(0.5)
                        pyautogui.moveTo(pyautogui.locateCenterOnScreen('Deployer_Monstres.png', confidence=0.7))
                        pyautogui.click()
                        time.sleep(1.5)
                except pyautogui.ImageNotFoundException:
                    time.sleep(2.5)
    except pyautogui.ImageNotFoundException:
        time.sleep(0.1)

#regarde si il y a des minerais dans une zone de 7 par 7 dont le joueur (les coordonees en entree) est le centre
def Bot1(x:int,y:int):
    while keyboard.is_pressed('space') == False:
        try:
            if pyautogui.locateOnScreen('Max_Troupes.png', confidence=0.5) is not None: #verifie si le nombre max de troupes en deplacement n'est pas atteint
               time.sleep(5)
               helpGuild()  #aide la guilde toute les 5 secondes
        except pyautogui.ImageNotFoundException:    #Pour ne pas renvoyer de msg d'erreur
            for i in range(7):
                move('y', y-30+10*i)    #change de ligne
                time.sleep(1)
                OreOnScreen()   #verifie si il y a des minerais
                helpGuild() #aide la guilde toute les environ 2s
                for j in range(7):
                    move('x', x-30+10*j)    #change de colonne
                    time.sleep(1)
                    OreOnScreen()   #verifie si il y a des minerais
                    helpGuild() #aide la guilde toute les environ 2s
                    
def Bot2(x:int,y:int):
    while keyboard.is_pressed('space') == False:
        try:
            if pyautogui.locateOnScreen('Shield.png', confidence=0.5) is not None: #regarde si il y a un bouclier deploye
                time.sleep(0.1)
        except pyautogui.ImageNotFoundException:
            boucli()
            pass


        
#Code principal :
time.sleep(2)
Bot1(301,477)
"""
pyautogui.moveTo(pyautogui.locateCenterOnScreen('Monster_2.png', confidence=0.7))

hunt(1,343,479)
"""
"""
Fonction hunt :
- Deplacements de la cam
- Vérification jauge energie remplie
- Commenter

"""
