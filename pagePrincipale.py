import tkinter as tk
from Main import ouvrir_Accueil
from graphiques import *
from meteoGlobal import *
from sunrise_sunset import *
from feedback import *
import time
import math
from PIL import Image,ImageTk

def ouvrir_accueil_fenetre():
    ouvrir_Accueil()

def ouvrir_pages():
    graphique()

def ouvrir_meteo_global():
    afficher_carte_html()

def autre_informations():
    affiche_sunrise_sunset()

def feedback():
    run_rating_app()

def ouvrir_parametres():
    nouvelle_fenetre = tk.Toplevel(fe)
    nouvelle_fenetre.title("settings")
    nouvelle_fenetre.geometry("400x300")
    nouvelle_fenetre.configure(bg="white")
    tk.Label(nouvelle_fenetre, text="C'est la fenêtre des paramètres !").pack()

def ouvrir_aide():
    nouvelle_fenetre = tk.Toplevel(fe)
    nouvelle_fenetre.title("Aide")
    nouvelle_fenetre.geometry("400x300")
    nouvelle_fenetre.configure(bg="white")
    tk.Label(nouvelle_fenetre, text="C'est la fenêtre d'aide !").pack()

def switch():
    global btnEtat
    if btnEtat is True:
        # Creer une fermeture animee Navbar:
        for x in range(285):
            navbarLateral.place(x=-x, y=0)
            topFrame.update()

        # Reset couleur widgets
        bannerText.config(fg="#FFFFFF",bg="#87B1DC")  # Change text color to white
        acceuilText.config(fg="#FFFFFF")  # Change text color to white
        # topFrame.config(bg="#87B1DC")
        fe.config(bg="gray30")
        btnEtat = False

    else:
        for x in range(-285, 0):
            navbarLateral.place(x=x, y=0)
            topFrame.update()
            btnEtat = True
def switch_theme():
    global dark_mode
    if dark_mode:
        fe.config(bg="gray30")
        
        mode_button.config(bg="gray30", activebackground="gray30")  # Change background color to gray30
        bannerText.config(fg="#FFFFFF", bg="gray30")  # Change text color to white
        acceuilText.config(bg="#87B1DC", fg="#E6E6FA")  # Change text color to white in dark mode
        navbarLateral.config(bg="#E6E6FA")
        canvas.config(bg="gray30")  # Changer la couleur de fond du canevas


        for widget in navbarLateral.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(bg="#E6E6FA", fg="#000000")
        
        # Modifier la couleur des aiguilles de l'horloge
        canvas.itemconfig(seconds_hand, fill="red")
        canvas.itemconfig(minutes_hand, fill="white")
        canvas.itemconfig(hours_hand, fill="white")
        dark_mode = False

    else:
        fe.config(bg="#E6E6FA")

        mode_button.config(bg="#E6E6FA", activebackground="#E6E6FA")  # Change background color to light blue
        bannerText.config(fg="#87B1DC", bg="#E6E6FA")  # Change text color to black
        acceuilText.config(bg="#87B1DC", fg="#E6E6FA")  # Change text color to white in dark mode
        navbarLateral.config(bg="gray30")
        canvas.config(bg="#E6E6FA")  # Changer la couleur de fond du canevas

        for widget in navbarLateral.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(bg="gray30", fg="white")
        mode_button.config(bg="#E6E6FA")
        # Restore date label colors to default
        # Rétablir la couleur par défaut des aiguilles de l'horloge
        canvas.itemconfig(seconds_hand, fill="red")
        canvas.itemconfig(minutes_hand, fill="black")
        canvas.itemconfig(hours_hand, fill="black")
        dark_mode = True

    
    
def switch_mode():
    switch_theme()
    if dark_mode:
        mode_button.config(image=light_image, bg="#E6E6FA")
    else:
        mode_button.config(image=dark_image, bg="gray30")

# Création de la fenêtre tkinter
fe = tk.Tk()
fe.title("weather simulation")
fe.geometry("890x479+300+200")
fe.configure(bg="#E6E6FA")
fe.resizable(False, False)

# Chargement de l'icône de fenêtre
icone = tk.PhotoImage(file='weather.png')
fe.iconphoto(False, icone)

# Parametrage switch
btnEtat = False

# Parametrage dark mode
dark_mode = True

# top navigation
topFrame = tk.Frame(fe, bg="#87B1DC", width=150, height=90)
topFrame.pack(side="top", fill=tk.X)

# texte de top bar
acceuilText = tk.Label(topFrame, text="WELCOME", font=("ExtraCondenced ", 15, " bold italic"), bg="#87B1DC",
                       fg="#E6E6FA", height=2, padx=20)
acceuilText.pack(side="right")

# Ajout d'un texte de bannière avec une ombre portée et une bordure arrondie
bannerText = tk.Label(fe, text="Weather \nApplication", font="ExtraCondensed 35 bold", fg="#87B1DC", bg="#E6E6FA")
bannerText.place(x=320, y=330)

# Button to switch between dark and light mode
dark_image = tk.PhotoImage(file='dark.png')
light_image = tk.PhotoImage(file='light.png')
close_image = tk.PhotoImage(file='close.png')
mode_button = tk.Button(fe, image=light_image, bd=0, bg="#E6E6FA", activebackground="#E6E6FA", command=switch_mode)
mode_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# navbar Icone
navbarIcon = tk.PhotoImage(file='menu.png')
navbarBtn = tk.Button(topFrame, image=navbarIcon, bg="#87B1DC",
                      bd=0, padx=20, activebackground="#87B1DC", command=switch)
navbarBtn.place(x=20, y=10)

# parametre navbar laterale
navbarLateral = tk.Frame(fe, bg="gray30", width=285, height=400)
navbarLateral.place(x=0, y=0)
tk.Label(navbarLateral, font="ExtraCondensed 15", bg="#87B1DC", fg="black", width=300, height=2, padx=20).place(x=0,
                                                                                                                   y=0)

y = 80
# Liste des fonctions correspondantes à chaque option
fonctions_options = [ouvrir_accueil_fenetre, ouvrir_pages, ouvrir_meteo_global,feedback]
# Les options dans la navbar Laterale avec les chemins d'accès aux fichiers image
option = [("    WEATHER\n", "Acceuillicon.png"),
          (" GRAPHICS\n", "graph.png"),
          ("    WEATHER MAP", "carteM.png"),
          #("    OTHER INFORMATIONS\n", "+.png"),
          ("    FEEDBACK\n", "feedback.png")
          ]


# Positionnement des options dans la Navbar avec texte et image
for i in range(len(option)):
    # Chargement de l'image
    icon = tk.PhotoImage(file=option[i][1])
    # Création du bouton avec texte et image
    btn = tk.Button(navbarLateral, text=option[i][0], font="ExtraCondensed 13", bg="gray30", fg="white",
                    activebackground="gray30", bd=0, command=fonctions_options[i], compound="left", image=icon)
    btn.image = icon  # Garde une référence à l'image pour éviter la suppression par le garbage collector
    # Placement du bouton
    btn.config(text=option[i][0] + "\t  ")
    icon_height = icon.height()
    # Placement du bouton avec un espacement horizontal de 10 pixels entre l'image et le texte
    btn.place(x=5, y=y + (65 - icon_height) // 2)
    y += 65
    

# Parametrage bouton fermeture menu
# Définition de la fonction pour fermer la barre de navigation latérale
def ferme_barre():
    navbarLateral.place_forget()


# Création du bouton de fermeture avec la commande associée
fermeBtn = tk.Button(navbarLateral, image=close_image, bg="#87B1DC", activebackground="#87B1DC", bd=0,
                     command=ferme_barre)
fermeBtn.place(x=250, y=10)

# Fermeture de la barre de navigation latérale au démarrage de l'application
ferme_barre()

# creation de l'horloge
def update_clock():
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

    # updating seconds hand
    seconds_x = seconds_hand_len * math.sin(math.radians(seconds * 6)) + center_x
    seconds_y = -1 * seconds_hand_len * math.cos(math.radians(seconds * 6)) + center_y
    canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)

    # updating minutes hand
    minutes_x = minutes_hand_len * math.sin(math.radians(minutes * 6)) + center_x
    minutes_y = -1 * minutes_hand_len * math.cos(math.radians(minutes * 6)) + center_y
    canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

    # updating hours hand
    hours_x = hours_hand_len * math.sin(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + center_x
    hours_y = -1 * hours_hand_len * math.cos(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + center_y
    canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)

    fe.after(1000, update_clock)


canvas = tk.Canvas(fe, width=200, height=200, bg="#E6E6FA", highlightthickness=0)
canvas.place(x=600,y=100) 

# create background
image_pil = Image.open("a1.png")

            # Redimensionnement de l'image
nouvelle_largeur = 190  # Nouvelle largeur de l'image
nouvelle_hauteur = 190  # Nouvelle hauteur de l'image
image_pil_redimensionnee = image_pil.resize((nouvelle_largeur, nouvelle_hauteur)) 

            # Conversion de l'image PIL redimensionnée en format PhotoImage pour tkinter
image_tk = ImageTk.PhotoImage(image_pil_redimensionnee)

canvas.create_image(100,100, image=image_tk)


# create clock hands
# seconds hand
center_x = 100
center_y = 100

seconds_hand_len = 95
minutes_hand_len = 80
hours_hand_len = 60

seconds_hand = canvas.create_line(200, 200, 200 + seconds_hand_len, 200 + seconds_hand_len, width=1.5, fill='red')
# minutes hand
minutes_hand = canvas.create_line(200, 200, 200 + minutes_hand_len, 200 + minutes_hand_len, width=2, fill='black')
# hours hand
hours_hand = canvas.create_line(200, 200, 200 + hours_hand_len, 200 + hours_hand_len, width=4, fill='black')

update_clock()


# Démarrage de la boucle principale tkinter
fe.mainloop()