# Créé par henzo, le 26/04/2024 avec Python 3.7 en UTF-8
# Créé par henzo, le 25/04/2024 en Python 3.7
# Créé par henzo, le 24/11/2023 en Python 3.7
# Créé par henzo, le 12/10/2023 en Python 3.7

import os # syteme
import ctypes # syteme
import math # mathematique
import pickle as pk # syteme
import tkinter as tk # affichage
from PIL import Image, ImageTk # affichage
from tkinter import filedialog # affichage
from tkinter import Y, X, RIGHT, LEFT, BOTH, BOTTOM, VERTICAL, HORIZONTAL # affichage
from tkinter import messagebox # affichage
import tkinter.font as tk_font # affichage

fenetre =  tk.Tk() # initialisation de la fenetre principal

def global_image(liste):
    global liste_img_c
    liste_img_c = liste
    return

def fichier_dossier(path:str)->tuple:
    """ entree : str ; sortie : tuple"""
    tab = []
    tab_type = []
    liste = []
    for root, directories, files in os.walk(path):
        for file in files:
            if '.png'in file:
                tab.append(path + '/' + file) ; tab_type.append('.png')
            elif '.jpeg' in file:
                tab.append(path + '/' + file) ; tab_type.append('.jpeg')
            elif '.jpg' in file:
                tab.append(path + '/' + file) ; tab_type.append('.jpg')
            liste.append(path + '/' + file)
    global_image(liste)
    return tab, tab_type

def creation_bouton(tab:list)->list:
    """ entree :  list ; sortie :  list """
    liste = []
    for i in range(len(tab)):
        liste.append(tk.Button(fenetre, image = photo, command=lambda i=i: image_choisi(i) ))
        plus(liste[i], tab[i])
    return liste

def plus(b,p):
    photo = ImageTk.PhotoImage(p)
    b.photo = photo
    b.configure(image = photo)
    return

def creation_image(tab_image)->list:
    """ entree :  tuple ; sortie : list """
    liste = []
    tab_type = tab_image[1]
    tab_image = tab_image[0]
    for i in range(len(tab_image)):
        image = Image.open(f"{tab_image[i]}")
        MAX_SIZE = (100, 100)
        image.thumbnail(MAX_SIZE)
        # creating thumbnail
        liste.append(image)
    return liste

def image_mere(chemin):
    """ entree : str  """
    global photo
    image = Image.open(f"{chemin}")
    MAX_SIZE = (100, 100)
    image.thumbnail(MAX_SIZE)
    # creating thumbnail
    photo = ImageTk.PhotoImage(image)
    return

def appliquer_fond(chemin):
    """ entree : str """
    ctypes.windll.user32.SystemParametersInfoW(20, 0, chemin , 0)
    image_unicode = os.path.abspath(chemin) # on transforme l'image en unicode # il faut le chemin absolu
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_unicode, 0x02)
    return

def choisir_dossier():
    dossier = filedialog.askdirectory()
    return dossier

def choisir_fichier(label_dossier = '/'):
    """ entree : str (pas obligatoire ; sortie : str """
    fichier = filedialog.askopenfilename(initialdir=label_dossier, title="selectionde d'iamge", filetypes=(("all files", "*.*"), ("all files", "*.*")))
    return fichier

def dossier_defaut(label_text, label_image,Fpara): # label_text->label_dossier
    """ entree : str, str, <class 'tkinter.Tk' """
    Fpara.wm_attributes("-topmost", 0)
    dossier = choisir_dossier()
    Fpara.wm_attributes("-topmost", 1)
    if dossier != "":
        label_text.config(text = str(dossier))
    ##Etext(label_text,label_image)
    donnees_E(label_text,label_image)
    return

def img_defaut(label_text, label_dossier, Fpara): # label_text->label_image
    """ entree : str, str, <class 'tkinter.Tk' """
    Fpara.wm_attributes("-topmost", 0)
    if label_dossier['text'][0] != " ":
        dossier = choisir_fichier(label_dossier["text"])
    else:
        dossier = choisir_fichier()
    Fpara.wm_attributes("-topmost", 1)
    if dossier != "":
        label_text.config(text = str(dossier))
    ##Etext(label_dossier,label_text)
    donnees_E(label_dossier, label_text)
    return

def place_img_fp():
    initialisation = init_D()
    if initialisation == None:
        return
    elif len(initialisation) >= 2:
        fichier, theme = initialisation
    else:
        fichier = initialisation[0]

    if fichier != None and fichier[1] != " ":
        image_mere(fichier[1])
        boutton_img_df(fichier[1])
    return

def init_D(): # initialisation des données
    donnees = donnees_L()
    ##print(donnees)
    if donnees == None:
        return None
    # je dois verifier si tout les elements sont là (key : defaut->str ; dossier->str ; theme->tuple "valeur hexa")
    if 'theme' in donnees:
        return [donnees['dossier'], donnees['defaut']], donnees['theme']
    return [donnees['dossier'], donnees['defaut']], # faire une modif sur la parie execution

def donnees_L(): # lecture des données
    if not os.path.exists('parametre.af'): # verification que le fichier de parametre existe
        return None
    if os.path.getsize('parametre.af') == 0: # verification qu'il contient qqc
        return None
    with open("parametre.af","rb") as fichier:
        fichier = pk.load(fichier) # traduction du fichier
    if len(fichier) >= 2 and 'defaut' in fichier and 'dossier' in fichier and os.path.exists(fichier['defaut']) and os.path.exists(fichier['dossier']): # si tout les elements sont bon (existe) et si fichier a plus de deux elements
        return fichier # dictionnaire
    ##print('cic', fichier)
    return None

def donnees_E(label_dossier:tk.Label = None, label_image:tk.Label = None, mode = None): # ecriture des données

    erreur = False # si True, cela signifie qu'il y a un pb en fin d'execution au niv de la lecture du fichier de parametres ou dans l'appel de la fonction

    theme_color = (canvas['bg'], frame_b['bg'], liste_b[0]['bg'], liste_b[0]['fg']) # couleur de l'app (couleur centre ; couleur gauche ; couleur bouton ; couleur ecriture bouton)
    if mode == None and (label_dossier == None or label_image == None): # si la fonction est executée mais qu'elle n'est pas appelée pour l'arret du pgrm
        erreur = True # erreur d'appel de fonction
        raise AttributeError("mode == None but it's not end prgm") # erreur d'appel de fonction
    elif mode == None: # si le mode != None => fin d'execution du pgrm
        image_defaut = label_image['text'] # image par defaut
        dossier_defaut = label_dossier['text'] # dossier par defaut
        parametre_ = {'defaut':image_defaut, 'dossier':dossier_defaut, 'theme':theme_color} # dict qui regroupe les 3 infos (dossier et image par defaut, theme(couleur) choisi par l'utilisateur)
    else:
        donnees = donnees_L() # on prend les valeurs dans le fichier de parametres
        if donnees != None: # on verifie que tout est en ordre
            donnees['theme'] = theme_color # on modifie / ajoute le nouvelle element theme_color
            parametre_ = donnees # le dict 'donnees' replace le dict 'parametre_'
        else:
            erreur = True # car donnees == True dans erreur dans la lecture du fichier de parametres

    if erreur == False: # si il n'y a pas d'erreur dans le code pecedent (de la fonction)
        with open("parametre.af", 'wb') as fichier:
            pk.dump(parametre_, fichier)

# implementation d'un nouveau mode d
##def donnees_E_(**kw)->None:
##    """
##    prend les arguments et les places dans le fichier parametre.af
##    toutes les options de personnalisations du theme son automatiquement prise en compte
##    il faut au moins mettre en argument le dossier et l'image par defaut
##    """
##    # parametre_ = {'defaut':image_defaut, 'dossier':dossier_defaut, 'theme':theme_color}
##    theme_color = (canvas['bg'], frame_b['bg'], liste_b[0]['bg']) # couleur de l'app
##    if 'defaut' in kw and 'dossier' in kw:
##        kw['theme'] = theme_color

def boutton_img_df(label_image, win = None):
    """ entree : str """
    global b_imgD
    def e(bouton):
        type = label_image[-1]
        for i in range(len(label_image)-2,0,-1):
            if type[0] != '.':
                type = label_image[i] + type

        image = Image.open(f"{label_image}")
        MAX_SIZE = (100, 100)
        image.thumbnail(MAX_SIZE)
        # creating thumbnail
        photo = ImageTk.PhotoImage(image)

        bouton.photo = photo
        bouton.configure(image = photo)
        return
    try:
        b_imgD.destroy()
    except:
        pass

    if not os.path.exists(label_image):
        messagebox.showerror("Erreur de parametre", "Le chemin renseigné est invalide")
        print(etat_parametre.get())
        if etat_parametre.get() == False and win != None:
            win.focus_force()
            print('hellp')
        return

    image_mere(label_image)
    b_imgD = tk.Button(fenetre, image = photo, command = lambda : appliquer_fond(label_image)) # definition de l'image par def
    b_imgD.place(x=20,y=50)
    e(b_imgD)
    return

def affichage_image(liste_bouton):
    """ entree : list """
    temp = 0
    x = 100 ; y = 40
    for i in range(len(liste_bouton)):
        bouton_c = canvas.create_window(x, y, window = liste_bouton[i])
        temp += 1
        x += 120
        if temp == 6:
            temp = 0
            x = 100
            y += 80

    return

def image_choisi(n_image):
    """ entree : int """
    global numero_image
    numero_image = n_image
    return

def execution():
    global boutons_r
    initialisation = init_D() # tuple
    ##print(initialisation)
    if initialisation != None:
        if len(initialisation) == 2:
            dossier, theme_color = initialisation # dossier -> list : theme_color -> tuple
        else:
            dossier = initialisation[0]
        ##print(dossier)

        image_mere(dossier[1])
        var_image_defaut.set(dossier[1]) # chemin d'acces de l'image pas defaut
        dossier = dossier[0]
        images = fichier_dossier(dossier)
        image_boutons = creation_image(images)
        boutons = boutons_r = creation_bouton(image_boutons)
        affichage_image(boutons)
        if len(initialisation) == 2:
            if len(theme_color) == 4:
                canvas['bg'], frame_b['bg'], couleur_bouton, couleur_ecriture_b = theme_color
                for ele in liste_b:
                    ele['bg'] = couleur_bouton
                    ele['fg'] = couleur_ecriture_b
        return len(boutons)
    else:
        # cree variable si pas de chemin pour afficher image
        erreur_execution_d()
        return

def erreur_execution_d():
   messagebox.showerror("Erreur de parametre", "Veuillez renseigner le\nchemin d'acces du dossier\noù sont stokées les images")
   b_parametre.flash()

def exe_appliquer():
    if numero_image == None:
        return
    try:
        image = Image.open(f"{liste_img_c[numero_image]}")
        appliquer_fond(liste_img_c[numero_image])
    except:
        pass
    return

def actualiser():
    global numero_image
    if 'boutons_r' in globals(): # True si 'boutons_r' existe sinon Fasle
        for bouton in boutons_r: #
            bouton.destroy()
    execution()
    boutton_img_df(var_image_defaut.get()) # re-instalation du bouton de l'image par defaut
    numero_image = None

def destroy_window(win,Var):
    Var.set(True) # reaset variable d'etat
    win.destroy() # destruction de la fenetre 'win' => fin 'win'

def end_fenetre():
    """ fonction de fin de pgrm """
    donnees_E(mode = True) # enregistrement du theme choisi par l'utilisateur
    fenetre.destroy() # destruction de la fenetre principal => fin

def open_parametre():
    """ ouverture des parametre ssi pas encore ouvert """
    if etat_parametre.get() == True:
        parametre()
    elif para.state() == 'iconic':
        para.deiconify()
        para.focus_force()
    else:
        para.focus_force()

def open_options():
    """ ouverture des parametre ssi pas encore ouvert """

    if etat_options.get() == True:
        options()
    elif opti.state() == 'iconic':
        opti.deiconify()
        opti.focus_force()
    else:
        print(opti.state())
        opti.focus_force()

def parametre():
    global para

    para = tk.Toplevel(fenetre) # tk.Tk()
    para.title('Parametre')
    para.geometry('800x220')
    para.resizable(width=False, height=False)
    para.protocol("WM_DELETE_WINDOW", lambda : destroy_window(para,etat_parametre))
    #para.wm_attributes("-topmost", 1)

    etat_parametre.set(False)

    label_dossier_titre = tk.Label(para, text = 'Nom dossier', font = ('Times Roman',15))
    label_dossier = tk.Label(para, text = " Nom du dossier (qui contient les images)", font = ('Times Roman',10))
    bouton_dossier = tk.Button(para, text = 'Modifier', command = lambda : dossier_defaut(label_dossier,  label_image, para), font = ('Sens Serif',10))

    label_image_titre = tk.Label(para, text = 'Image par defaut', font = ('Times Roman',15))
    label_image = tk.Label(para, text = " Image par defaut (raccourci sur l'ecran d'accueil)", font = ('Times Roman',10))
    bouton_image = tk.Button(para, text = 'Modifier', command = lambda : img_defaut(label_image, label_dossier, para), font = ('Sens Serif',10))

    b_para_appliquer = tk.Button(para, text = 'Appliquer', command = lambda : boutton_img_df(label_image['text'],win=para), font = ('Sens Serif',10))

    try: # a modifer
        initialisation = init_D()
        if len(initialisation) >= 2:
            info, theme = initialisation
        else:
            info = initialisation[0]
        if info != None:
            if info[0] == "":
                label_dossier.config(text = " Une erreur est survenue :/")
            else:
                label_dossier.config(text = str(info[0]))
            label_image.config(text = str(info[1]))
    except:
        label_dossier.config(text = " Une erreur est survenue :/")
        label_image.config(text = " Une erreur est survenue :/")
        pass

    label_dossier_titre.place(x=120,y=20)
    label_dossier.place(x=50,y=50)
    bouton_dossier.place(x=250,y=80)

    label_image_titre.place(x=120,y=120)
    label_image.place(x=50,y=150)
    bouton_image.place(x=250,y=180)

    b_para_appliquer.place(x=500,y=180)

    para.mainloop()
    return

def options():
    global opti

    opti = tk.Toplevel(fenetre) # tk.Tk()
    opti.title('Option')
    opti.geometry('800x220')
    opti.resizable(width=False, height=False)
    opti.protocol("WM_DELETE_WINDOW", lambda : destroy_window(opti,etat_options))
    opti['bg'] = 'light gray'

    etat_options.set(False)

    color_ = [ canvas['bg'], frame_b['bg'], liste_b[0]['bg'] ] # couleur de l'app

    def chang_color(color,element:int = None):
        if element == None: # si il n'y pas d element deffinit -> choix par defaut
            canvas['bg'] = color[0] # couleur centre
            frame_b['bg'] = color[1] # couleur gauche
            for ele in liste_b: #  pour tout les boutons (parametre, option, appliquer, actualiser)
                ele['bg'] = color[2] # couleur bouton
            if hexa_est_claire(color[2]): # si couleur bouton est clair
                for ele in liste_b: #  pour tout les boutons (parametre, option, appliquer, actualiser)
                    ele['fg'] = 'black' # couleur d ecriture en noir
            else: # sinon -> couleur bonton est sombre
                for ele in liste_b: #  pour tout les boutons (parametre, option, appliquer, actualiser)
                    ele['fg'] = 'white' # couleur d ecriture en blanc
        elif element == 1: # element 1 -> couleur centre
            canvas['bg'] = color
        elif element == 2: # element 2 -> couleur gauche
            frame_b['bg'] = color
        else: # element 3 -> couleur bouton
            for ele in liste_b: #  pour tout les boutons (parametre, option, appliquer, actualiser)
                ele['bg'] = color # couleur bonton
            if hexa_est_claire(color): # si couleur bouton est clair
                for ele in liste_b: #  pour tout les boutons (parametre, option, appliquer, actualiser)
                    ele['fg'] = 'black' # couleur d ecriture en noir
            else: # sinon -> couleur bonton est sombre
                for ele in liste_b: #  pour tout les boutons (parametre, option, appliquer, actualiser)
                    ele['fg'] = 'white' # couleur d ecriture en blanc

    class Palette:
        # argument : c1 ; c2 ; c3 ; emplacement (x,y) -> tuple

        def __init__(self,c1:str,c2:str,c3:str,emplacement:tuple,w=10,h=50):

            self.c1 = c1
            self.c2 = c2
            self.c3 = c3
            if type(emplacement) != tuple and len(emplacement) != 2:
                raise TypeError('missing 1 required positional argument: (x,y)')
            self.x, self.y = emplacement[0], emplacement[-1]

            frame_c = tk.Frame(opti, bg = 'black') # contour en noir
            frame_c.place(x=self.x, y=self.y, width=w+30,height=h+10)

            frame_c1 = tk.Frame(opti, bg = self.c1) # 1er couleur (g)
            frame_c1.place(x=self.x+5, y=self.y+5, width=w,height=h)

            frame_c2 = tk.Frame(opti, bg = self.c2) # 2e couleur (c)
            frame_c2.place(x=self.x+15, y=self.y+5, width=w,height=h)

            frame_c3 = tk.Frame(opti, bg = self.c3) # 3e couleur (d)
            frame_c3.place(x=self.x+25, y=self.y+5, width=w,height=h)

        def get_color(self):
            return [self.c1,self.c2,self.c3]

    def radio_button(pallette,i):
        bouton = tk.Radiobutton(opti, value=i, variable = Ivar, bg = 'light gray', command=exe_color, padx = 9)
        x, y = pallette.x, pallette.y
        bouton.place(x = x, y = y+65)
        return bouton

    def exe_color():
        chang_color(choix_palette[Ivar.get()])
        return

    def rgb_to_hex():
        # on récupère les valeurs rgb en hexadecimal
        R = hex(var_R.get()).lstrip('0x').upper()
        G = hex(var_G.get()).lstrip('0x').upper()
        B = hex(var_B.get()).lstrip('0x').upper()
        RGB = [R,G,B]

        # on met des 0 dans les données de l'rgb pour avoir un bon résultat
        for i in range(len(RGB)):
            if len(RGB[i]) < 2:
                while len(RGB[i]) != 2:
                    RGB[i] = '0' + RGB[i]

        color = '#' + RGB[0] + RGB[1] + RGB[2]
        label_hexa.config(text = 'Couleur hexadecimal : ' + color)
        label_hexa_cadre.config(bg = color)

    def hexa_est_claire(hexa:str)->bool: # erreur ici
        ''' prend un valeur hexadecimal est le rentourne si True si claire, sinon False '''
        hexa = hexa.strip('#') # on enleve le '#' de l'hexadecimal
        r, g, b = hexa[:2], hexa[2:4], hexa[4:] # on deffinit le 'r', le 'g' et le 'b'
        r, g, b = int(r,16), int(g, 16), int(b, 16) # on met le 'r', 'g' et 'b' en base 10
        return 0.3*r + 0.59*g + 0.11*b >= 120 # si la condition est bonne alors la couleur est claire

    def appliquer_perso():
        hexa = label_hexa['text'].lstrip('Couleur hexadecimal : ')
        chang_color(hexa, var_radio.get())
        return

    def mise_avant():
        var = var_radio.get()
        if var == 1:
            label_explication_c1['fg'] = 'magenta'
            label_explication_c2['fg'] = 'black'
            label_explication_c3['fg'] = 'black'

            label_explication1['fg'] = 'magenta'
            label_explication2['fg'] = 'black'
            label_explication3['fg'] = 'black'

        elif var == 2:
            label_explication_c2['fg'] = 'magenta'
            label_explication_c1['fg'] = 'black'
            label_explication_c3['fg'] = 'black'

            label_explication2['fg'] = 'magenta'
            label_explication1['fg'] = 'black'
            label_explication3['fg'] = 'black'

        else:
            label_explication_c3['fg'] = 'magenta'
            label_explication_c2['fg'] = 'black'
            label_explication_c1['fg'] = 'black'

            label_explication3['fg'] = 'magenta'
            label_explication2['fg'] = 'black'
            label_explication1['fg'] = 'black'
        pass

    # explication
    bar_separationG = tk.Frame(opti, bg = 'black')

    label_explication_c1 = tk.Label(opti,text = '1', bg = 'light gray', font = ('Arial',10)) # placement du 1 dans l'explication
    label_explication_c2 = tk.Label(opti,text = '2', bg = 'light gray', font = ('Arial',10)) # placement du 2 dans l'explication
    label_explication_c3 = tk.Label(opti,text = '3', bg = 'light gray', font = ('Arial',10)) # placement du 3 dans l'explication

    label_explication = tk.Label(opti,text = '1: zone centrale\n2: zone gauche\n3: boutons', bg = 'light gray')
    label_explication1 = tk.Label(opti,text = '1: zone centrale', bg = 'light gray') # placement du 1 dans l'explication bis
    label_explication2 = tk.Label(opti,text = '2: zone gauche', bg = 'light gray') # placement du 2 dans l'explication bis
    label_explication3 = tk.Label(opti,text = '3: boutons', bg = 'light gray') # placement du 3 dans l'explication bis

    label_explication_c1['fg'] = 'magenta'
    label_explication_c2['fg'] = 'black'
    label_explication_c3['fg'] = 'black'

    label_explication1['fg'] = 'magenta'
    label_explication2['fg'] = 'black'
    label_explication3['fg'] = 'black'

    # quadrillage d'explication
    frame_expli_g = tk.Frame(opti, bg = 'black')
    frame_expli_cg = tk.Frame(opti, bg = 'black')
    frame_expli_cd = tk.Frame(opti, bg = 'black')
    frame_expli_d = tk.Frame(opti, bg = 'black')
    frame_expli_h = tk.Frame(opti, bg = 'black')
    frame_expli_b = tk.Frame(opti, bg = 'black')

    # Spinbox # '#%02x%02x%02x' % (15, 126, 23)
    bar_separationD = tk.Frame(opti, bg = 'black')
    label_perso = tk.Label(opti,text = 'Personnalisation du thème :', bg = 'light gray', font = ('Arial',12,'bold'))

    var_R = tk.IntVar() # variable d'entier qui gere les valeurs R (RGB)
    var_R.set(0)
    var_G = tk.IntVar(value = 0) # variable d'entier qui gere les valeurs G (RGB)
    var_B = tk.IntVar(value = 0) # variable d'entier qui gere les valeurs B (RGB)
    var_radio = tk.IntVar(value = 1)
    label_hexa = tk.Label(opti, text = 'Couleur hexadecimal : #000000' , bg = 'light gray')
    label_hexa_cadre = tk.Label(opti, text = '        ' , bg = 'black')

    scale_R = tk.Scale(opti, from_ = 0, to = 255, orient = VERTICAL, length = 100, width = 10, variable = var_R, command = lambda _ : rgb_to_hex(), showvalue = 0, bg = 'red', bd = 0, highlightcolor = 'red') # r : barre de deffiliment
    scale_G = tk.Scale(opti, from_ = 0, to = 255, orient = VERTICAL, length = 100, width = 10, variable = var_G, command = lambda _ : rgb_to_hex(), showvalue = 0, bg = 'green', bd = 0, highlightcolor = 'green') # g : barre de deffiliment
    scale_B = tk.Scale(opti, from_ = 0, to = 255, orient = VERTICAL, length = 100, width = 10, variable = var_B, command = lambda _ : rgb_to_hex(), showvalue = 0, bg = 'blue', bd = 0, highlightcolor = 'blue') # b : barre de deffiliment

    label_R = tk.Label(opti, textvariable = var_R, bg = 'light gray') # label qui affiche la valeur du R (RGB)
    label_G = tk.Label(opti, textvariable = var_G, bg = 'light gray') # label qui affiche la valeur du G (RGB)
    label_B = tk.Label(opti, textvariable = var_B, bg = 'light gray') # label qui affiche la valeur du B (RGB)

    label_r = tk.Label(opti, text = 'R', bg = 'light gray', font = ('Arial',10,'bold')) # affichage R
    label_g = tk.Label(opti, text = 'G', bg = 'light gray', font = ('Arial',10,'bold')) # affichage G
    label_b = tk.Label(opti, text = 'B', bg = 'light gray', font = ('Arial',10,'bold')) # affichage B

    radio_p1 = tk.Radiobutton(opti, text = 'zone 1', value = 1, variable = var_radio, bg = 'light gray', font = ('Arial',9,'bold'), command = mise_avant) # radion boutton pour modifier la couleur de l'element 1
    radio_p2 = tk.Radiobutton(opti, text = 'zone 2', value = 2, variable = var_radio, bg = 'light gray', font = ('Arial',9,'bold'), command = mise_avant) # radion boutton pour modifier la couleur de l'element 2
    radio_p3 = tk.Radiobutton(opti, text = 'zone 3', value = 3, variable = var_radio, bg = 'light gray', font = ('Arial',9,'bold'), command = mise_avant) # radion boutton pour modifier la couleur de l'element 3

    # bouton appliquer
    boutton_appliquer_perso = tk.Button(opti, text = 'Appliquer', command = appliquer_perso) # creation dubouton d'application
    boutton_appliquer_perso.place(x = 727, y = 150)

    # placement explication
    bar_separationD.place(x = 549, y = 0, width = 2,height = 700)

    label_explication_c1.place(x = 22, y = 20)
    label_explication_c2.place(x = 35, y = 20)
    label_explication_c3.place(x = 50, y = 20)

    label_explication1.place(x = 1, y = 70)
    label_explication2.place(x = 1, y = 90)
    label_explication3.place(x = 1, y = 110)

    frame_expli_g.place(x = 19, y = 10, width = 5, height = 50)
    frame_expli_cg.place(x = 34 , y = 10, width = 2, height = 50)
    frame_expli_cd.place(x = 48, y = 10, width = 2, height = 50)
    frame_expli_d.place(x = 62, y = 10, width = 5, height = 50)
    frame_expli_h.place(x = 22, y = 10, width = 45, height = 5)
    frame_expli_b.place(x = 22, y = 55, width = 45, height = 5)

    # placement Spinbox
    bar_separationG.place(x = 90, y = 0, width = 2,height = 700)
    label_perso.place(x = 560, y = 2)

    # personnalisation perso

    label_r.place(x = 578, y = 29)
    label_g.place(x = 628, y = 29)
    label_b.place(x = 678, y = 29)

    scale_R.place(x = 580, y = 50)
    scale_G.place(x = 630, y = 50)
    scale_B.place(x = 680, y = 50)

    radio_p1.place(x = 727, y = 50)
    radio_p2.place(x = 727, y = 80)
    radio_p3.place(x = 727, y = 110)

    label_R.place(x = 578, y = 155)
    label_G.place(x = 628, y = 155)
    label_B.place(x = 678, y = 155)

    label_hexa.place(x = 577, y = 185)
    label_hexa_cadre.place(x = 750, y = 185)

    liste_pallette = []
    x = 98
    y = 5
    etage = 1
    for ligne in id_couleur:
        liste_pallette.append(Palette(ligne[0],ligne[1],ligne[2],(x,y)))
        x += 45
        if len(liste_pallette)//10 == etage:
            y += 95 ; x = 98 ; etage += 1
    choix_palette = []
    for element in liste_pallette:
        choix_palette.append(element.get_color())

    liste_radio = []
    Ivar = tk.IntVar(opti)

    if color_ in id_couleur:
        Ivar.set(id_couleur.index(color_))
    else:
        Ivar.set(0)

    for i in range(len(liste_pallette)):
        liste_radio.append(radio_button(liste_pallette[i],i))

    opti.mainloop()
    return

fenetre.geometry("1000x700+50+10")
fenetre.title("Auto-Fond    Version.1.2.0")
fenetre.resizable(width=False, height=False)
fenetre.protocol("WM_DELETE_WINDOW", end_fenetre)
##icon = tk.PhotoImage(file = os.path.abspath("logo auto fond.png"))
##fenetre.tk.call('wm', 'iconphoto', fenetre._w, icon)

# id des couleurs de la personnalisation du theme

id_couleur = [['#739072','#4F6F52','#ECE3CE'],
              ['#9BBEC8','#427D9D','#DDF2FD'],
              ['#DCBFFF','#D0A2F7','#E5D4FF'],
              ['#E48F45','#994D1C','#F5CCA0'],
              ['#FFC47E','#FFE382','#FFAD84'],
              ['#7BD3EA','#A1EEBD','#F6F7C4'],
              ['#B5CB99','#B2533E','#FCE09B'],
              ['#005B41','#232D3F','#008170'],
              ['#6D5D6E','#4F4557','#F4EEE0'],
              ['#9E4784','#66347F','#E0AED0'],
              ['#B6BBC4','#31304D','#F0ECE5'],
              ['#F6F7C4','#A1EEBD','#F6D6D6']]

#

frame_b = tk.Frame(fenetre, bg = 'light gray')
frame_b.place(x=0, y=0, width=180,height=700) # frame des boutons d'options

frame_i = tk.Frame(fenetre, bg = 'gray') # frame des boutons de fond
frame_i.place(x=180, y=0, width=820,height=700)


canvas = tk.Canvas(frame_i, bg = 'gray', width=200, height=100)
canvas.place(x=0, y=0, width=820,height=700)
canvas.config(scrollregion=(0, 0, 1000, 500))

# scrollbar
scrollbar = tk.Scrollbar(frame_i, orient = VERTICAL,width = 20)
scrollbar.pack(side = RIGHT, fill = Y )
scrollbar.config(command=canvas.yview)

canvas.config(yscrollcommand=scrollbar.set)

numero_image = None

b_appliquer = tk.Button(fenetre, text = 'Appliquer', command = exe_appliquer) # , command =  c # commande de test
b_parametre = tk.Button(fenetre, text = 'Paramètre', command = open_parametre) # variable d'etat pour savoir si il y a une fenetre deja ouvert ou pas ?
b_reset = tk.Button(fenetre, text = 'Actualiser', command = actualiser)

b_options = tk.Button(fenetre, text = 'Option', command = open_options)

# taille de la police + couleur
b_appliquer['font'] = tk_font.Font(size=20)
b_parametre['font'] = tk_font.Font(size=19)
b_reset['font'] = tk_font.Font(size=15)

# action liée
fenetre.bind("<Return>", lambda x : exe_appliquer())

# mise en place de la couleur par defaut
liste_b = [b_appliquer,b_options,b_parametre,b_reset]
canvas['bg'] = '#739072'
frame_b['bg'] = '#4F6F52'
for ele in liste_b:
    ele['bg'] = '#ECE3CE'

# placement des boutons d'actions
b_appliquer.place(x=20,y=280)
b_parametre.place(x=20,y=510)
b_options['font'] = tk_font.Font(size=19)
b_reset.place(x=40,y=640)

b_options.place(x=40,y=400)

# BoolVar d etat

etat_options = tk.BooleanVar()
etat_options.set(True)
etat_parametre = tk.BooleanVar()
etat_parametre.set(True)

# StringVar pour l'image par defaut

var_image_defaut = tk.StringVar() # chemin d'acces pour l'image par défaut

# lancement

place_img_fp()
val_exe = execution()

if val_exe != None and type(val_exe) == int and val_exe > 48:
    canvas.config(scrollregion=(0, 0, 1000, 600*(math.ceil(val_exe/48) )))

fenetre.mainloop()