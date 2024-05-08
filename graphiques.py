from tkinter import *
from tkinter import messagebox
import requests
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import datetime
import numpy as np
import seaborn as sns
# Déclaration globale de la variable ville_entry
ville_entry = None
ville_selec = None  # Variable globale pour stocker la ville sélectionnée

def obtenir_donnees_meteo(ville, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={ville}&appid={api_key}&units=metric"
    reponse = requests.get(url)
    donnees = reponse.json()
    return donnees
def creer_graphique_vent_matrice(ville, api_key):
    donnees_meteo = obtenir_donnees_meteo(ville, api_key)
    
    # Extraction des données sur le vent
    heures = []
    vitesses_vent = []
    for prevision in donnees_meteo['list']:
        heure = prevision['dt_txt']
        vitesse_vent = prevision['wind']['speed']  # Utilisez le champ correspondant à la vitesse du vent
        heures.append(heure)
        vitesses_vent.append(vitesse_vent)

    # Création du graphique de matrice pour le vent
    plt.figure(figsize=(8, 4))
    plt.matshow([vitesses_vent], fignum=1, cmap='Greens')
    plt.xlabel('Heure')
    plt.ylabel('Vitesse du vent (m/s)')
    plt.title('Vitesse du vent à ' + ville)
    plt.colorbar(label='Vitesse du vent (m/s)')
    plt.xticks(range(len(heures)), heures, rotation=45)
    plt.tight_layout()
    plt.show()

def creer_graphique_vent_barres(ville, api_key):
    donnees_meteo = obtenir_donnees_meteo(ville, api_key)
    
    # Extraction des données sur le vent
    heures = []
    vitesses_vent = []
    for prevision in donnees_meteo['list']:
        heure = prevision['dt_txt']
        vitesse_vent = prevision['wind']['speed']  # Utilisez le champ correspondant à la vitesse du vent
        heures.append(heure)
        vitesses_vent.append(vitesse_vent)

    # Création du graphique à barres pour le vent
    plt.figure(figsize=(8, 4))
    plt.bar(heures, vitesses_vent, color='green')
    plt.xlabel('Heure')
    plt.ylabel('Vitesse du vent (m/s)')
    plt.title('Vitesse du vent à ' + ville)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def creer_graphique_vent_ligne(ville, api_key):
    donnees_meteo = obtenir_donnees_meteo(ville, api_key)
    
    # Extraction des données sur le vent
    heures = []
    vitesses_vent = []
    for prevision in donnees_meteo['list']:
        heure = prevision['dt_txt']
        vitesse_vent = prevision['wind']['speed']  # Utilisez le champ correspondant à la vitesse du vent
        heures.append(heure)
        vitesses_vent.append(vitesse_vent)

    # Création du graphique en ligne pour le vent
    plt.figure(figsize=(8, 4))
    plt.plot(heures, vitesses_vent, color='green', marker='o', linestyle='-')
    plt.xlabel('Heure')
    plt.ylabel('Vitesse du vent (m/s)')
    plt.title('Vitesse du vent à ' + ville)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def creer_graphique_pression_matrice(ville, api_key):
    donnees_meteo = obtenir_donnees_meteo(ville, api_key)
    
    # Extraction des données sur la pression atmosphérique
    heures = []
    pressions = []
    for prevision in donnees_meteo['list']:
        heure = prevision['dt_txt']
        pression = prevision['main']['pressure']  # Utilisez le champ correspondant à la pression atmosphérique
        heures.append(heure)
        pressions.append(pression)

    # Création du graphique de matrice pour la pression atmosphérique
    plt.figure(figsize=(8, 4))
    plt.matshow([pressions], fignum=1, cmap='Purples')
    plt.xlabel('Heure')
    plt.ylabel('Pression (hPa)')
    plt.title('Pression atmosphérique à ' + ville)
    plt.colorbar(label='Pression (hPa)')
    plt.xticks(range(len(heures)), heures, rotation=45)
    plt.tight_layout()
    plt.show()

def creer_graphique_pression_barres(ville, api_key):
    donnees_meteo = obtenir_donnees_meteo(ville, api_key)
    
    # Extraction des données sur la pression atmosphérique
    heures = []
    pressions = []
    for prevision in donnees_meteo['list']:
        heure = prevision['dt_txt']
        pression = prevision['main']['pressure']  # Utilisez le champ correspondant à la pression atmosphérique
        heures.append(heure)
        pressions.append(pression)

    # Création du graphique à barres pour la pression atmosphérique
    plt.figure(figsize=(8, 4))
    plt.bar(heures, pressions, color='purple')
    plt.xlabel('Heure')
    plt.ylabel('Pression (hPa)')
    plt.title('Pression atmosphérique à ' + ville)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def creer_graphique_pression_ligne(ville, api_key):
    donnees_meteo = obtenir_donnees_meteo(ville, api_key)
    
    # Extraction des données sur la pression atmosphérique
    heures = []
    pressions = []
    for prevision in donnees_meteo['list']:
        heure = prevision['dt_txt']
        pression = prevision['main']['pressure']  # Utilisez le champ correspondant à la pression atmosphérique
        heures.append(heure)
        pressions.append(pression)

    # Création du graphique en ligne pour la pression atmosphérique
    plt.figure(figsize=(8, 4))
    plt.plot(heures, pressions, color='purple', marker='o', linestyle='-')
    plt.xlabel('Heure')
    plt.ylabel('Pression (hPa)')
    plt.title('Pression atmosphérique à ' + ville)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def creer_graphique_precipitations_matrice(ville, api_key):
    donnees_meteo = obtenir_donnees_meteo(ville, api_key)
    
    # Extraction des données sur les précipitations
    heures = []
    precipitations = []
    for prevision in donnees_meteo['list']:
        heure = prevision['dt_txt']
        precipitation = prevision['main']['humidity']  # Utilisez le champ correspondant aux précipitations
        heures.append(heure)
        precipitations.append(precipitation)

    # Création du graphique de matrice pour les précipitations
    plt.figure(figsize=(8, 4))
    plt.matshow([precipitations], fignum=1, cmap='Blues')
    plt.xlabel('Heure')
    plt.ylabel('Précipitations (%)')
    plt.title('Précipitations à ' + ville)
    plt.colorbar(label='Précipitations (%)')
    plt.xticks(range(len(heures)), heures, rotation=45)
    plt.tight_layout()
    plt.show()

def creer_graphique_precipitations_barres(ville, api_key):
    donnees_meteo = obtenir_donnees_meteo(ville, api_key)
    
    # Extraction des données sur les précipitations
    heures = []
    precipitations = []
    for prevision in donnees_meteo['list']:
        heure = prevision['dt_txt']
        precipitation = prevision['main']['humidity']  # Utilisez le champ correspondant aux précipitations
        heures.append(heure)
        precipitations.append(precipitation)

    # Création du graphique à barres pour les précipitations
    plt.figure(figsize=(8, 4))
    plt.bar(heures, precipitations, color='blue')
    plt.xlabel('Heure')
    plt.ylabel('Précipitations (%)')
    plt.title('Précipitations à ' + ville)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def creer_graphique_precipitations_ligne(ville, api_key):
    donnees_meteo = obtenir_donnees_meteo(ville, api_key)
    
    # Extraction des données sur les précipitations
    heures = []
    precipitations = []
    for prevision in donnees_meteo['list']:
        heure = prevision['dt_txt']
        precipitation = prevision['main']['humidity']  # Utilisez le champ correspondant aux précipitations
        heures.append(heure)
        precipitations.append(precipitation)

    # Création du graphique en ligne pour les précipitations
    plt.figure(figsize=(8, 4))
    plt.plot(heures, precipitations, color='blue', marker='o', linestyle='-')
    plt.xlabel('Heure')
    plt.ylabel('Précipitations (%)')
    plt.title('Précipitations à ' + ville)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def creer_graphique_temperature_matrice(ville, api_key):
    donnees_meteo = obtenir_donnees_meteo(ville, api_key)
    
    # Extraction des données sur la température
    heures = []
    temperatures = []
    for prevision in donnees_meteo['list']:
        heure = prevision['dt_txt']
        temperature = prevision['main']['temp']  # Utilisez le champ correspondant à la température
        heures.append(heure)
        temperatures.append(temperature)

    # Création du graphique de matrice pour la température
    plt.figure(figsize=(8, 4))
    plt.matshow([temperatures], fignum=1, cmap='Reds')
    plt.xlabel('Heure')
    plt.ylabel('Température (°C)')
    plt.title('Température à ' + ville)
    plt.colorbar(label='Température (°C)')
    plt.xticks(range(len(heures)), heures, rotation=45)
    plt.tight_layout()
    plt.show()

def creer_graphique_temperature_barres(ville, api_key):
    donnees_meteo = obtenir_donnees_meteo(ville, api_key)
    
    # Extraction des données sur la température
    heures = []
    temperatures = []
    for prevision in donnees_meteo['list']:
        heure = prevision['dt_txt']
        temperature = prevision['main']['temp']  # Utilisez le champ correspondant à la température
        heures.append(heure)
        temperatures.append(temperature)

    # Création du graphique à barres pour la température
    plt.figure(figsize=(8, 4))
    plt.bar(heures, temperatures, color='red')
    plt.xlabel('Heure')
    plt.ylabel('Température (°C)')
    plt.title('Température à ' + ville)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def creer_graphique_temperature_ligne(ville, api_key):
    donnees_meteo = obtenir_donnees_meteo(ville, api_key)
    
    # Extraction des données sur la température
    heures = []
    temperatures = []
    for prevision in donnees_meteo['list']:
        heure = prevision['dt_txt']
        temperature = prevision['main']['temp']  # Utilisez le champ correspondant à la température
        heures.append(heure)
        temperatures.append(temperature)

    # Création du graphique en ligne pour la température
    plt.figure(figsize=(8, 4))
    plt.plot(heures, temperatures, color='red', marker='o', linestyle='-')
    plt.xlabel('Heure')
    plt.ylabel('Température (°C)')
    plt.title('Température à ' + ville)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def creer_graphe_matrice_temperature(ville, api_key):
    donnees_meteo = obtenir_donnees_meteo(ville, api_key)
    matrice_temperature = creer_matrice_temperature(donnees_meteo)
    
    jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    heures = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
    
    plt.figure(figsize=(8, 4))
    sns.heatmap(matrice_temperature, annot=True, cmap='coolwarm', xticklabels=heures, yticklabels=jours)
    plt.title(f'Heatmap de température pour {ville}')
    plt.xlabel('Heure')
    plt.ylabel('Jour de la semaine')
    plt.show()

def creer_matrice_temperature(donnees_meteo):
    jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    heures = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
    temperatures = np.zeros((len(jours), len(heures)))
    
    for prevision in donnees_meteo['list']:
        date = datetime.datetime.strptime(prevision['dt_txt'].split()[0], '%Y-%m-%d')
        jour = jours[date.weekday()]
        heure = prevision['dt_txt'].split()[1][:5]
        temperature = prevision['main']['temp']
        jour_index = jours.index(jour)
        heure_index = heures.index(heure)
        temperatures[jour_index][heure_index] = temperature
    
    return temperatures

def creer_graphe_matrice_pression(ville, api_key):
    donnees_meteo = obtenir_donnees_meteo(ville, api_key)
    matrice_pression = creer_matrice_pression(donnees_meteo)
    
    jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    heures = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
    
    plt.figure(figsize=(8, 4))
    sns.heatmap(matrice_pression, annot=True, cmap='coolwarm', xticklabels=heures, yticklabels=jours)
    plt.title(f'Heatmap de pression atmosphérique pour {ville}')
    plt.xlabel('Heure')
    plt.ylabel('Jour de la semaine')
    plt.show()

def creer_matrice_pression(donnees_meteo):
    jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    heures = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
    pressions = np.zeros((len(jours), len(heures)))
    
    for prevision in donnees_meteo['list']:
        date = datetime.datetime.strptime(prevision['dt_txt'].split()[0], '%Y-%m-%d')
        jour = jours[date.weekday()]
        heure = prevision['dt_txt'].split()[1][:5]
        pression = prevision['main']['pressure']
        jour_index = jours.index(jour)
        heure_index = heures.index(heure)
        pressions[jour_index][heure_index] = pression
    
    return pressions


def creer_graphe_matrice_vent(ville, api_key):
    donnees_meteo = obtenir_donnees_meteo(ville, api_key)
    matrice_vent = creer_matrice_vent(donnees_meteo)
    
    jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    heures = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
    
    plt.figure(figsize=(8, 4))
    sns.heatmap(matrice_vent, annot=True, cmap='coolwarm', xticklabels=heures, yticklabels=jours)
    plt.title(f'Heatmap de vitesse du vent pour {ville}')
    plt.xlabel('Heure')
    plt.ylabel('Jour de la semaine')
    plt.show()

def creer_matrice_vent(donnees_meteo):
    jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    heures = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
    vitesses_vent = np.zeros((len(jours), len(heures)))
    
    for prevision in donnees_meteo['list']:
        date = datetime.datetime.strptime(prevision['dt_txt'].split()[0], '%Y-%m-%d')
        jour = jours[date.weekday()]
        heure = prevision['dt_txt'].split()[1][:5]
        vitesse_vent = prevision['wind']['speed']
        jour_index = jours.index(jour)
        heure_index = heures.index(heure)
        vitesses_vent[jour_index][heure_index] = vitesse_vent
    
    return vitesses_vent

def creer_graphe_matrice_precipitations(ville, api_key):
    donnees_meteo = obtenir_donnees_meteo(ville, api_key)
    matrice_precipitations = creer_matrice_precipitations(donnees_meteo)
    
    jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    heures = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
    
    plt.figure(figsize=(8, 4))
    sns.heatmap(matrice_precipitations, annot=True, cmap='coolwarm', xticklabels=heures, yticklabels=jours)
    plt.title(f'Heatmap de précipitations pour {ville}')
    plt.xlabel('Heure')
    plt.ylabel('Jour de la semaine')
    plt.show()

def creer_matrice_precipitations(donnees_meteo):
    jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    heures = ['00:00', '03:00', '06:00', '09:00', '12:00', '15:00', '18:00', '21:00']
    precipitations = np.zeros((len(jours), len(heures)))
    
    for prevision in donnees_meteo['list']:
        date = datetime.datetime.strptime(prevision['dt_txt'].split()[0], '%Y-%m-%d')
        jour = jours[date.weekday()]
        heure = prevision['dt_txt'].split()[1][:5]
        precipitation = prevision['main']['humidity']
        jour_index = jours.index(jour)
        heure_index = heures.index(heure)
        precipitations[jour_index][heure_index] = precipitation
    
    return precipitations


def rechercher_ville():
    global ville_selec
    ville_selec = ville_entry.get()
    print("Ville sélectionnée :", ville_selec)

def afficher_graphique(option):
    global ville_selec  # Accès à la variable ville_selec déclarée globalement
    if ville_selec:
        api_key = "e2382302378f3a9df7e550c3e8633623"
        try:
            if option == "Precipitation":
                type_graph = type_graphique.get()
                if type_graph == "Barres":
                    creer_graphique_precipitations_barres(ville_selec, api_key)
                elif type_graph == "Ligne":
                    creer_graphique_precipitations_ligne(ville_selec, api_key)
                elif type_graph == "Matrice":
                    creer_graphique_precipitations_matrice(ville_selec, api_key)
                elif type_graph == "heatmap":
                    creer_graphe_matrice_precipitations(ville_selec, api_key)
            elif option == "Temperature":
                type_graph = type_graphique.get()
                if type_graph == "Barres":
                    creer_graphique_temperature_barres(ville_selec, api_key)
                elif type_graph == "Ligne":
                    creer_graphique_temperature_ligne(ville_selec, api_key)
                elif type_graph == "Matrice":
                    creer_graphique_temperature_matrice(ville_selec, api_key)
                elif type_graph == "heatmap":
                    creer_graphe_matrice_temperature(ville_selec, api_key)
            elif option == "vent":
                type_graph = type_graphique.get()
                if type_graph == "Barres":
                    creer_graphique_vent_barres(ville_selec, api_key)
                elif type_graph == "Ligne":
                    creer_graphique_vent_ligne(ville_selec, api_key)
                elif type_graph == "Matrice":
                    creer_graphique_vent_matrice(ville_selec, api_key)
                elif type_graph == "heatmap":
                    creer_graphe_matrice_vent(ville_selec, api_key)
            elif option == "pression":
                type_graph = type_graphique.get()
                if type_graph == "Barres":
                    creer_graphique_pression_barres(ville_selec, api_key)
                elif type_graph == "Ligne":
                    creer_graphique_pression_ligne(ville_selec, api_key)
                elif type_graph == "Matrice":
                    creer_graphique_pression_matrice(ville_selec, api_key)
                elif type_graph == "heatmap":
                    creer_graphe_matrice_pression(ville_selec, api_key)
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")
    else:
        messagebox.showerror("Erreur", "Enter city first !")

def on_enter_pressed(event):
    rechercher_ville()

def graphique():
    global ville_entry  # Accès à la variable ville_entry déclarée globalement
    root = Toplevel()
    root.title("Graphiques") # Titre de la fenettre
    root.geometry("890x479+300+200") #la geometrie de la fenettre 
    root.configure(bg="#E6E6FA") #determiner la couleur du fond ecran
    root.resizable(False,False) # la fenettre n'est definie fixe
    icone=PhotoImage(file=r"C:\Users\hp\Desktop\Projet PythonFinal\Projet Python\weather.png")  # L'image a faire comme icone doit etre obligatoirement sous format png ou gif
    root.iconphoto(False,icone)

    # Création d'un cadre pour placer les widgets
    frame = Frame(root, padx=10, pady=10,bg="#E6E6FA")
    frame.pack()
    image = Image.open("search bar.png")

    # Redimensionnement de l'image
    nouvelle_largeur = 500  # Nouvelle largeur de l'image
    nouvelle_hauteur = 200  # Nouvelle hauteur de l'image
    image_redimensionnee = image.resize((nouvelle_largeur, nouvelle_hauteur)) 

    # Conversion de l'image PIL redimensionnée en format PhotoImage pour tkinter
    image_tk1 = ImageTk.PhotoImage(image_redimensionnee)

    # Création d'une étiquette pour afficher l'image
    labele = Label(root, image=image_tk1,bg="#E6E6FA")
    labele.place(x=200,y=50)
    # Création d'une étiquette et d'une zone de saisie pour la ville
        # Chargement de la barre de recherche
    imagefe = Image.open("simulation2.png")

    # Redimensionnement de l'image
    nouvelle_largeur = 190  # Nouvelle largeur de l'image
    nouvelle_hauteur = 160  # Nouvelle hauteur de l'image
    image_redimensionneefe = imagefe.resize((nouvelle_largeur, nouvelle_hauteur)) 

    # Conversion de l'image PIL redimensionnée en format PhotoImage pour tkinter
    image_tkfe = ImageTk.PhotoImage(image_redimensionneefe)

    # Création d'une étiquette pour afficher l'image
    labelefe = Label(root, image=image_tkfe,bg="#E6E6FA")
    labelefe.place(x=710,y=300)
                # Chargement de la barre de recherche
    imagef = Image.open("simulation.png")

    # Redimensionnement de l'image
    nouvelle_largeur = 230  # Nouvelle largeur de l'image
    nouvelle_hauteur = 230  # Nouvelle hauteur de l'image
    image_redimensionneef = imagef.resize((nouvelle_largeur, nouvelle_hauteur)) 

    # Conversion de l'image PIL redimensionnée en format PhotoImage pour tkinter
    image_tkf = ImageTk.PhotoImage(image_redimensionneef)

    # Création d'une étiquette pour afficher l'image
    labelef = Label(root, image=image_tkf,bg="#E6E6FA")
    labelef.place(x=0,y=30)
    # Chargement de la barre de recherche
    image = Image.open(r"search bar.png")

    # Redimensionnement de l'image
    nouvelle_largeur = 500  # Nouvelle largeur de l'image
    nouvelle_hauteur = 200  # Nouvelle hauteur de l'image
    image_redimensionnee = image.resize((nouvelle_largeur, nouvelle_hauteur)) 

    # Conversion de l'image PIL redimensionnée en format PhotoImage pour tkinter
    image_tk1 = ImageTk.PhotoImage(image_redimensionnee)

    # Création d'une étiquette pour afficher l'image
    labele = Label(root, image=image_tk1,bg="#E6E6FA")
    labele.place(x=200,y=50)
    # Création d'une étiquette pour afficher le titre au-dessus de l'image
    titre_label = Label(root, text="Enter City : ", font=("Helvetica", 16), bg="#E6E6FA", fg="#1E90FF")
    titre_label.place(x=250, y=60)
    
    # Chargement de l'image avec PIL
    weat_ima = Image.open(r"wh.jpg")

    # Redimensionnement de l'image
    nouvelle_largeur = 45  # Nouvelle largeur de l'image
    nouvelle_hauteur = 45  # Nouvelle hauteur de l'image
    image_redimensionnee = weat_ima.resize((nouvelle_largeur, nouvelle_hauteur))

    # Conversion de l'image PIL redimensionnée en format PhotoImage pour tkinter
    image_tk2 = ImageTk.PhotoImage(image_redimensionnee)

    # Création d'une étiquette pour afficher l'image redimensionnée
    weatherim = Label(root, image=image_tk2, bg="white")
    weatherim.place(x=267, y=125)

    # Le texte qu'on saisi dans la bar de recherche

    textf=Entry(root,justify="center",width=15,font=('Arial',25,'bold'),bg='white',border=0,fg="black")
    textf.place(x=310,y=130)
    textf.focus()
    textf.bind('<Return>', on_enter_pressed)  # Lier la fonction on_enter_pressed à l'événement "Entrée"
    ville_entry = textf  # Assigner le widget Entry à ville_entry
    
    # Chargement de l'image
    image1 = Image.open(r"search_ico.png")

    # Redimensionnement de l'image
    nouvelle_largeur = 45
    nouvelle_hauteur = 45
    image_redimensionnee1 = image1.resize((nouvelle_largeur, nouvelle_hauteur))

    # Conversion de l'image PIL redimensionnée en format PhotoImage pour tkinter
    image_tk3 = ImageTk.PhotoImage(image_redimensionnee1)

    # Création d'une étiquette pour afficher l'image
    label = Label(root, image=image_tk3, bg="white")
    # Création d'un bouton avec l'image
    bouton = Button(root, image=image_tk3, borderwidth=0, cursor="hand2", bg="white", command=rechercher_ville)
    bouton.place(x=583, y=127)
    label.place(x=578, y=126)

    #click bouton
        # Chargement de la barre de recherche
    imageg = Image.open(r"click.png")

    # Redimensionnement de l'image
    nouvelle_largeur = 50  # Nouvelle largeur de l'image
    nouvelle_hauteur = 50  # Nouvelle hauteur de l'image
    image_redimensionneeg = imageg.resize((nouvelle_largeur, nouvelle_hauteur)) 

    # Conversion de l'image PIL redimensionnée en format PhotoImage pour tkinter
    image_tkg = ImageTk.PhotoImage(image_redimensionneeg)

    # Création d'une étiquette pour afficher l'image
    labelei = Label(root, image=image_tkg,bg="#E6E6FA")
    labelei.place(x=180,y=230)

    # Création d'une zone de texte pour afficher le texte souligné
    texte = Text(root, font=("Helvetica", 16), bg="#E6E6FA", fg="black", bd=0, relief="flat", highlightthickness=0, width=50, height=1)
    texte.insert(END, "Click Option :")

    # Ajout du soulignement au texte
    texte.tag_configure("underline", underline=True)
    texte.tag_add("underline", "1.0", "end")

    texte.place(x=250, y=245)
    def on_enter(event):
        event.widget.config(bg="#B4C8DD")  # Changer la couleur de fond lorsque la souris entre

    def on_leave(event):
        event.widget.config(bg="#E6E6FA")  

    option_menu = StringVar(root)
    option_menu.set("")  # Option par défaut
    options = ["Precipitation", "Temperature", "vent", "pression"]
    x = 160  # Coordonnée x initiale
    y = 300  # Coordonnée y
    #########################################################
    select_bar = Image.open(r"select_bar.png")

    # Redimensionnement de l'image
    nouvelle_largeur1 = 160  # Nouvelle largeur de l'image
    nouvelle_hauteur1 = 160  # Nouvelle hauteur de l'image
    image_redimensionnee1 = select_bar.resize((nouvelle_largeur1, nouvelle_hauteur1)) 

    # Conversion de l'image PIL redimensionnée en format PhotoImage pour tkinter
    image_tk1_select_bar = ImageTk.PhotoImage(image_redimensionnee1)

    # Création d'une étiquette pour afficher l'image
    labele_bar = Label(root, image=image_tk1_select_bar,bg="#E6E6FA")
    labele_bar.place(x=480,y=185)
    #########################################################
    # Ajouter un menu déroulant pour choisir le type de graphique
    global type_graphique
    type_graphique = StringVar(root)
    type_graphique.set("Barres")  # Type de graphique par défaut

    option_menu_graphique = OptionMenu(root, type_graphique, "Barres", "Ligne","Matrice","heatmap")
    option_menu_graphique.config(bg="#E6E6FA",bd=0,highlightbackground="#E6E6FA",height=0)  # Changer la couleur du texte
    option_menu_graphique.place(x=530, y=254)


    # Positionnement des options dans la Navbar
    for option in options:
        button = Button(root, text=option, font="ExtraCondensed 15", bg="#E6E6FA", fg="#4C7DAF",
                        activebackground="#B4C8DD", bd=0, command=lambda opt=option: afficher_graphique(opt),
                        highlightthickness=2, highlightbackground="black")
        button.place(x=x, y=y)
        button.bind("<Enter>", on_enter)  # Lier l'événement de survol de la souris à la fonction on_enter
        button.bind("<Leave>", on_leave)  # Lier l'événement de sortie de la souris à la fonction on_leave

        # Obtenir la largeur réelle du bouton
        width = button.winfo_reqwidth()

        # Ajuster la coordonnée x pour le prochain bouton
        x += width + 40  # Ajoutez un espacement de 20 pixels entre les boutons
    root.mainloop()

