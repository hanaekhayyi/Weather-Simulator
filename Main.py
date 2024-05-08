from tkinter import *
import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image,ImageTk
from tkintermapview import TkinterMapView
import geocoder
from datetime import timezone

def ouvrir_Accueil():
    f=Toplevel()
    f.title("Accueil") # Titre de la fenettre
    f.geometry("890x479+300+200") #la geometrie de la fenettre 
    f.configure(bg="#E6E6FA") #determiner la couleur du fond ecran
    f.resizable(False,False) # la fenettre n'est definie fixe

    def obtenir_temperature_jour_actuel(donnees_meteo):
        # Obtenir la date actuelle
        date_actuelle = datetime.now().date()

        # Parcourir les prévisions météorologiques pour trouver le jour actuel
        for prevision in donnees_meteo['list']:
            # Convertir la date de la prévision en objet datetime
            date_prevision = datetime.fromtimestamp(prevision['dt']).date()
            
            # Vérifier si la prévision est pour le jour actuel
            if date_prevision == date_actuelle:
                return prevision['main']['temp']
        
        # Si aucune prévision n'a été trouvée pour le jour actuel, retourner None
        return None


    def obtenir_humidite_jour_actuel(donnees_meteo):
        # Obtenir la date actuelle
        date_actuelle = datetime.now().date()

        # Parcourir les prévisions météorologiques pour trouver le jour actuel
        for prevision in donnees_meteo['list']:
            # Convertir la date de la prévision en objet datetime
            date_prevision = datetime.fromtimestamp(prevision['dt']).date()
            
            # Vérifier si la prévision est pour le jour actuel
            if date_prevision == date_actuelle:
                return prevision['main']['humidity']
        
        # Si aucune prévision n'a été trouvée pour le jour actuel, retourner None
        return None

    def obtenir_pression_jour_actuel(donnees_meteo):
        # Obtenir la date actuelle
        date_actuelle = datetime.now().date()

        # Parcourir les prévisions météorologiques pour trouver le jour actuel
        for prevision in donnees_meteo['list']:
            # Convertir la date de la prévision en objet datetime
            date_prevision = datetime.fromtimestamp(prevision['dt']).date()
            
            # Vérifier si la prévision est pour le jour actuel
            if date_prevision == date_actuelle:
                return prevision['main']['pressure']
        
        # Si aucune prévision n'a été trouvée pour le jour actuel, retourner None
        return None
    def obtenir_vitesse_vent_jour_actuel(donnees_meteo):
        # Obtenir la date actuelle
        date_actuelle = datetime.now().date()

        # Parcourir les prévisions météorologiques pour trouver le jour actuel
        for prevision in donnees_meteo['list']:
            # Convertir la date de la prévision en objet datetime
            date_prevision = datetime.fromtimestamp(prevision['dt']).date()
            
            # Vérifier si la prévision est pour le jour actuel
            if date_prevision == date_actuelle:
                return prevision['wind']['speed']
        
        # Si aucune prévision n'a été trouvée pour le jour actuel, retourner None
        return None
        
    def obtenir_description_jour_actuel(donnees_meteo):
        # Obtenir la date actuelle
        date_actuelle = datetime.now().date()

        # Parcourir les prévisions météorologiques pour trouver le jour actuel
        for prevision in donnees_meteo['list']:
            # Convertir la date de la prévision en objet datetime
            date_prevision = datetime.fromtimestamp(prevision['dt']).date()
            
            # Vérifier si la prévision est pour le jour actuel
            if date_prevision == date_actuelle:
                return prevision['weather'][0]['description']
        
        # Si aucune prévision n'a été trouvée pour le jour actuel, retourner None
        return None

    def obtenir_donnees_meteo(ville, api_key):
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={ville}&appid={api_key}&units=metric"
        reponse = requests.get(url)
        donnees = reponse.json()
        return donnees
    def get_sunrise_sunset(api_key, ville):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
            sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')
            return sunrise, sunset
        else:
            return "N/A", "N/A"
    # Obtenir la temperature de la nuit
    def obtenir_temperature_nuit(donnees_meteo):
        for prevision in donnees_meteo.get('list', []):
            # Vérifiez si le moment de la journée est la nuit (généralement de 18h à 6h)
            if 'dt_txt' in prevision and 'main' in prevision and 'temp' in prevision['main']:
                date_heure = datetime.strptime(prevision['dt_txt'], '%Y-%m-%d %H:%M:%S')
                # Correction de la condition
                # Si c'est entre 18h et 23h OU entre 0h et 6h (nuit)
                if 18 <= date_heure.hour <= 23 or 0 <= date_heure.hour < 6:
                    return prevision['main']['temp']
        return None

    def obtenir_temperature_nuit_jour_suivant(donnees_meteo):
        # Récupérer la date et l'heure actuelle
        maintenant = datetime.now()
        # Calculer la date du jour suivant
        jour_suivant = maintenant + timedelta(days=1)

        for prevision in donnees_meteo.get('list', []):
            # Vérifier si la prévision correspond au jour suivant
            if 'dt_txt' in prevision:
                date_prevision = datetime.strptime(prevision['dt_txt'], '%Y-%m-%d %H:%M:%S')
                # Vérifier si la prévision est pour le jour suivant
                if date_prevision.date() == jour_suivant.date():
                    # Vérifier si le moment de la journée est la nuit (généralement de 18h à 6h)
                    if 18 <= date_prevision.hour <= 23 or 0 <= date_prevision.hour < 6:
                        return prevision['main']['temp']
        return None

    def obtenir_temperature_nuit_jour_3(donnees_meteo):
        # Récupérer la date et l'heure actuelle
        maintenant = datetime.now()
        # Calculer la date du jour suivant
        jour_suivant = maintenant + timedelta(days=2)

        for prevision in donnees_meteo.get('list', []):
            # Vérifier si la prévision correspond au jour suivant
            if 'dt_txt' in prevision:
                date_prevision = datetime.strptime(prevision['dt_txt'], '%Y-%m-%d %H:%M:%S')
                # Vérifier si la prévision est pour le jour suivant
                if date_prevision.date() == jour_suivant.date():
                    # Vérifier si le moment de la journée est la nuit (généralement de 18h à 6h)
                    if 18 <= date_prevision.hour <= 23 or 0 <= date_prevision.hour < 6:
                        return prevision['main']['temp']
        return None

    def obtenir_temperature_nuit_jour_4(donnees_meteo):
        # Récupérer la date et l'heure actuelle
        maintenant = datetime.now()
        # Calculer la date du jour suivant
        jour_suivant = maintenant + timedelta(days=3)

        for prevision in donnees_meteo.get('list', []):
            # Vérifier si la prévision correspond au jour suivant
            if 'dt_txt' in prevision:
                date_prevision = datetime.strptime(prevision['dt_txt'], '%Y-%m-%d %H:%M:%S')
                # Vérifier si la prévision est pour le jour suivant
                if date_prevision.date() == jour_suivant.date():
                    # Vérifier si le moment de la journée est la nuit (généralement de 18h à 6h)
                    if 18 <= date_prevision.hour <= 23 or 0 <= date_prevision.hour < 6:
                        return prevision['main']['temp']
        return None

    def obtenir_temperature_nuit_jour_5(donnees_meteo):
        # Récupérer la date et l'heure actuelle
        maintenant = datetime.now()
        # Calculer la date du jour suivant
        jour_suivant = maintenant + timedelta(days=4)

        for prevision in donnees_meteo.get('list', []):
            # Vérifier si la prévision correspond au jour suivant
            if 'dt_txt' in prevision:
                date_prevision = datetime.strptime(prevision['dt_txt'], '%Y-%m-%d %H:%M:%S')
                # Vérifier si la prévision est pour le jour suivant
                if date_prevision.date() == jour_suivant.date():
                    # Vérifier si le moment de la journée est la nuit (généralement de 18h à 6h)
                    if 18 <= date_prevision.hour <= 23 or 0 <= date_prevision.hour < 6:
                        return prevision['main']['temp']
        return None


    def obtenir_temperature_nuit_jour_6(donnees_meteo):
        # Récupérer la date et l'heure actuelle
        maintenant = datetime.now()
        # Calculer la date dans 5 jours
        jour_apres_5_jours = maintenant + timedelta(days=5)

        for prevision in donnees_meteo.get('list', []):
            # Vérifier si la prévision correspond à la date dans 5 jours
            if 'dt_txt' in prevision:
                date_prevision = datetime.strptime(prevision['dt_txt'], '%Y-%m-%d %H:%M:%S')
                # Vérifier si la prévision est pour la date dans 5 jours
                if date_prevision.date() == jour_apres_5_jours.date():
                    # Vérifier si le moment de la journée est la nuit (généralement de 18h à 6h)
                    if 18 <= date_prevision.hour <= 23 or 0 <= date_prevision.hour < 6:
                        return prevision['main']['temp']
        return None

    def obtenir_temperature_matin(donnees_meteo):
        for prevision in donnees_meteo.get('list', []):
            # Vérifiez si le moment de la journée est le matin (généralement de 6h à 18h)
            if 'dt_txt' in prevision and 'main' in prevision and 'temp' in prevision['main']:
                date_heure = datetime.strptime(prevision['dt_txt'], '%Y-%m-%d %H:%M:%S')
                if 6 <= date_heure.hour < 18:  # Si c'est entre 6h et 18h (matin)
                    return prevision['main']['temp']
        return None

    def obtenir_temperature_matin_jour_suivant(donnees_meteo):
        # Récupérer la date et l'heure actuelle
        maintenant = datetime.now()
        # Calculer la date du jour suivant
        jour_suivant = maintenant + timedelta(days=1)

        for prevision in donnees_meteo.get('list', []):
            # Vérifier si la prévision correspond au jour suivant
            if 'dt_txt' in prevision:
                date_prevision = datetime.strptime(prevision['dt_txt'], '%Y-%m-%d %H:%M:%S')
                # Vérifier si la prévision est pour le jour suivant
                if date_prevision.date() == jour_suivant.date():
                    # Vérifier si le moment de la journée est le matin (généralement de 6h à 12h)
                    if 6 <= date_prevision.hour < 18:
                        return prevision['main']['temp']
        return None

    def obtenir_temperature_matin_jour_3(donnees_meteo):
        # Récupérer la date et l'heure actuelle
        maintenant = datetime.now()
        # Calculer la date du jour suivant
        jour_suivant = maintenant + timedelta(days=2)

        for prevision in donnees_meteo.get('list', []):
            # Vérifier si la prévision correspond au jour suivant
            if 'dt_txt' in prevision:
                date_prevision = datetime.strptime(prevision['dt_txt'], '%Y-%m-%d %H:%M:%S')
                # Vérifier si la prévision est pour le jour suivant
                if date_prevision.date() == jour_suivant.date():
                    # Vérifier si le moment de la journée est le matin (généralement de 6h à 12h)
                    if 6 <= date_prevision.hour < 18:
                        return prevision['main']['temp']
        return None

    def obtenir_temperature_matin_jour_4(donnees_meteo):
        # Récupérer la date et l'heure actuelle
        maintenant = datetime.now()
        # Calculer la date du jour suivant
        jour_suivant = maintenant + timedelta(days=3)

        for prevision in donnees_meteo.get('list', []):
            # Vérifier si la prévision correspond au jour suivant
            if 'dt_txt' in prevision:
                date_prevision = datetime.strptime(prevision['dt_txt'], '%Y-%m-%d %H:%M:%S')
                # Vérifier si la prévision est pour le jour suivant
                if date_prevision.date() == jour_suivant.date():
                    # Vérifier si le moment de la journée est le matin (généralement de 6h à 12h)
                    if 6 <= date_prevision.hour < 18:
                        return prevision['main']['temp']
        return None

    def obtenir_temperature_matin_jour_5(donnees_meteo):
        # Récupérer la date et l'heure actuelle
        maintenant = datetime.now()
        # Calculer la date du jour suivant
        jour_suivant = maintenant + timedelta(days=4)

        for prevision in donnees_meteo.get('list', []):
            # Vérifier si la prévision correspond au jour suivant
            if 'dt_txt' in prevision:
                date_prevision = datetime.strptime(prevision['dt_txt'], '%Y-%m-%d %H:%M:%S')
                # Vérifier si la prévision est pour le jour suivant
                if date_prevision.date() == jour_suivant.date():
                    # Vérifier si le moment de la journée est le matin (généralement de 6h à 12h)
                    if 6 <= date_prevision.hour < 18:
                        return prevision['main']['temp']
        return None

    def obtenir_temperature_matin_jour_6(donnees_meteo):
        # Récupérer la date et l'heure actuelle
        maintenant = datetime.now()
        # Calculer la date dans 5 jours
        jour_apres_5_jours = maintenant + timedelta(days=5)

        for prevision in donnees_meteo.get('list', []):
            # Vérifier si la prévision correspond à la date dans 5 jours
            if 'dt_txt' in prevision:
                date_prevision = datetime.strptime(prevision['dt_txt'], '%Y-%m-%d %H:%M:%S')
                # Vérifier si la prévision est pour la date dans 5 jours
                if date_prevision.date() == jour_apres_5_jours.date():
                    # Vérifier si le moment de la journée est le matin (généralement de 6h à 12h)
                    if 6 <= date_prevision.hour < 12:
                        return prevision['main']['temp']
        return None


    # Cette fonction affiche toutes les informatios presentes dans le fichier en ce qui concerne la meteo
    def afficher_informations_meteo(informations):
        for cle, valeur in informations.items():
            if isinstance(valeur, dict):
                print(f"{cle}:")
                afficher_informations_meteo(valeur)
            else:
                print(f"{cle}: {valeur}")


    # Les icones de chaque etat du weather
    #le jours actuel
    def obtenir_code_icone(donnees_meteo):
        if 'list' in donnees_meteo and len(donnees_meteo['list']) > 0:
            code_icone = donnees_meteo['list'][0]['weather'][0]['icon']
            return code_icone
        else:
            return None

    # jours suivant
    def obtenir_code_icone_1(donnees_meteo):
        if 'list' in donnees_meteo and len(donnees_meteo['list']) > 1:
            code_icone = donnees_meteo['list'][1]['weather'][0]['icon']
            return code_icone
        else:
            return None
        
    def obtenir_code_icone_2(donnees_meteo):
        if 'list' in donnees_meteo and len(donnees_meteo['list']) > 2:
            code_icone = donnees_meteo['list'][2]['weather'][0]['icon']
            return code_icone
        else:
            return None

    def obtenir_code_icone_3(donnees_meteo):
        if 'list' in donnees_meteo and len(donnees_meteo['list']) > 3:
            code_icone = donnees_meteo['list'][3]['weather'][0]['icon']
            return code_icone
        else:
            return None
        
    def obtenir_code_icone_4(donnees_meteo):
        if 'list' in donnees_meteo and len(donnees_meteo['list']) > 4:
            code_icone = donnees_meteo['list'][4]['weather'][0]['icon']
            return code_icone
        else:
            return None
        
    def obtenir_code_icone_5(donnees_meteo):
        if 'list' in donnees_meteo and len(donnees_meteo['list']) > 5 :
            code_icone = donnees_meteo['list'][5]['weather'][0]['icon']
            return code_icone
        else:
            return None

    def getweather():
        city = textf.get()

        geolocator = Nominatim(user_agent="geoapiApplication")
        location = geolocator.geocode(city)
        
        if location:
            obj = TimezoneFinder()
            result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
            # Assurez-vous que timezone est un Label dans votre interface graphique
            # timezone.config(text=result)
            # long_lat.config(text=f"{round(location.latitude,4)}°N--{round(location.longitude,4)}°E")
            home=pytz.timezone(result)
            local_time=datetime.now(home)
            current_time=local_time.strftime("%I:%M-%p")
            clock.config(text=current_time)

            #weather
            api_key="e2382302378f3a9df7e550c3e8633623"
            donnee=obtenir_donnees_meteo(city,api_key)
            temperature = obtenir_temperature_nuit(donnee)
            temp.config(text=str(temperature) + "°C")

            humidite = obtenir_humidite_jour_actuel(donnee)
            hum.config(text=str(humidite) + "%")

            pression = obtenir_pression_jour_actuel(donnee)
            pres.config(text=str(pression) + "hPa")

            wind = obtenir_vitesse_vent_jour_actuel(donnee)
            vent.config(text=str(wind) + "m/s")

            desc=obtenir_description_jour_actuel(donnee)

            firstdayimage=obtenir_code_icone(donnee)
            photo1=ImageTk.PhotoImage(file=f"{firstdayimage}@2x.png")
            firstimage.config(image=photo1)
            firstimage.image=photo1

            tempday1=obtenir_temperature_matin(donnee)
            tempnuit1=obtenir_temperature_nuit(donnee)

            day1temp.config(text=f"Day:{tempnuit1}°\nNight:{tempday1}°")

            seconddayimage=obtenir_code_icone_1(donnee)
            img=(Image.open(f"{seconddayimage}@2x.png"))
            resized_image=img.resize((50,50))
            photo2 = ImageTk.PhotoImage(resized_image)
            secondimage.config(image=photo2)
            secondimage.image=photo2

            tempday2=obtenir_temperature_matin_jour_suivant(donnee)
            tempnuit2=obtenir_temperature_nuit_jour_suivant(donnee)

            day2temp.config(text=f"Day:{tempnuit2}°\nNight:{tempday2}°")

            thirddayimage=obtenir_code_icone_2(donnee)
            img=(Image.open(f"{thirddayimage}@2x.png"))
            resized_image=img.resize((50,50))
            photo3 = ImageTk.PhotoImage(resized_image)
            thirdimage.config(image=photo3)
            thirdimage.image=photo3

            tempday3=obtenir_temperature_matin_jour_3(donnee)
            tempnuit3=obtenir_temperature_nuit_jour_3(donnee)

            day3temp.config(text=f"Day:{tempnuit3}°\nNight:{tempday3}°")

            quatredayimage=obtenir_code_icone_3(donnee)
            img=(Image.open(f"{quatredayimage}@2x.png"))
            resized_image=img.resize((50,50))
            photo4 = ImageTk.PhotoImage(resized_image)
            quatreimage.config(image=photo4)
            quatreimage.image=photo4

            tempday4=obtenir_temperature_matin_jour_4(donnee)
            tempnuit4=obtenir_temperature_nuit_jour_4(donnee)

            day4temp.config(text=f"Day:{tempnuit4}°\nNight:{tempday4}°")

            cinqdayimage=obtenir_code_icone_4(donnee)
            img=(Image.open(f"{cinqdayimage}@2x.png"))
            resized_image=img.resize((50,50))
            photo5 = ImageTk.PhotoImage(resized_image)
            cinqimage.config(image=photo5)
            cinqimage.image=photo5

            tempday5=obtenir_temperature_matin_jour_5(donnee)
            tempnuit5=obtenir_temperature_nuit_jour_5(donnee)

            day5temp.config(text=f"Day:{tempnuit5}°\nNight:{tempday5}°")

            sixdayimage=obtenir_code_icone_5(donnee)
            img=(Image.open(f"{sixdayimage}@2x.png"))
            resized_image=img.resize((50,50))
            photo6 = ImageTk.PhotoImage(resized_image)
            siximage.config(image=photo6)
            siximage.image=photo6

            tempday6=obtenir_temperature_matin_jour_6(donnee)
            tempnuit6=obtenir_temperature_nuit_jour_6(donnee)

            day6temp.config(text=f"Day:{tempnuit6}°\nNight:{tempday6}°")
            # days

            first =datetime.now()
            day1.config(text=first.strftime("%A"))

            second =first+timedelta(days=1)
            day2.config(text=second.strftime("%A"))

            third =first+timedelta(days=2)
            day3.config(text=third.strftime("%A"))

            quatre =first+timedelta(days=3)
            day4.config(text=quatre.strftime("%A"))

            cinq =first+timedelta(days=4)
            day5.config(text=cinq.strftime("%A"))

            six =first+timedelta(days=5)
            day6.config(text=six.strftime("%A"))

        else:
            # Gérer le cas où la ville n'est pas trouvée
            not_found_label.config(text="City not found ! Enter City")
    # Icone for our application 

    icone=PhotoImage(file=r"weather.png")  # L'image a faire comme icone doit etre obligatoirement sous format png ou gif
    f.iconphoto(False,icone)

    # Chargement de l'image avec PIL
    image_pil = Image.open("carreBleu.jpg")

    # Redimensionnement de l'image
    nouvelle_largeur = 200  # Nouvelle largeur de l'image
    nouvelle_hauteur = 150  # Nouvelle hauteur de l'image
    image_pil_redimensionnee = image_pil.resize((nouvelle_largeur, nouvelle_hauteur)) 

    # Conversion de l'image PIL redimensionnée en format PhotoImage pour tkinter
    image_tk = ImageTk.PhotoImage(image_pil_redimensionnee)

    # Création d'une étiquette pour afficher l'image
    label = Label(f, image=image_tk,bg="#E6E6FA")
    #label.place(x=30,y=130) #le carre bleu qui encadre les fonctionnalites

    # Les titres dispo
    def affichermap():
        pays = textf.get()  # Récupérer le nom du pays depuis le champ de saisie
        if pays:
            # Créer une fenêtre pour afficher la carte
            fenetre_carte = Toplevel()
            fenetre_carte.title("Carte de " + pays)
            fenetre_carte.geometry("500x500")

            # Créer un widget de carte
            map_widget = TkinterMapView(fenetre_carte, width=600, height=400, corner_radius=0)
            map_widget.pack(fill="both", expand=True)
            map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=0)
            map_widget.set_address(pays, marker=True)  # Afficher le marqueur sur le pays spécifié

    icon_map = Image.open(r"map2.png")

    # Redimensionnement de l'image
    nouvelle_largeur = 45
    nouvelle_hauteur = 45
    image_redimensionnee1 = icon_map.resize((nouvelle_largeur, nouvelle_hauteur))

    # Conversion de l'image PIL redimensionnée en format PhotoImage pour tkinter
    image_map = ImageTk.PhotoImage(image_redimensionnee1)

    # Création d'une étiquette pour afficher l'image
    label_map = Label(f, image=image_map, bg= "#E6E6FA")
    # Création d'un bouton avec l'image
    bouton_map = Button(f, image=image_map, borderwidth=0, cursor="hand2", bg="#E6E6FA",command=affichermap)
    bouton_map.place(x=40, y=70)
    label_map.place(x=40, y=70)
    Label0=Label(f, text="Useful Information", font=("Times New Roman", 20), fg="#1E90FF",bg="#E6E6FA")
    Label0.place(x=40,y=110)

    Label1=Label(f,text="Temperature",font=('Roboto',15),fg="black",bg="#E6E6FA")
    Label1.place(x=70,y=150)
    Label2=Label(f,text="Humidity",font=('Roboto',15),fg="black",bg="#E6E6FA")
    Label2.place(x=70,y=180)
    Label3=Label(f,text="Pressure",font=('Roboto',15),fg="black",bg="#E6E6FA")
    Label3.place(x=70,y=209)
    Label4=Label(f,text="Wind speed",font=('Roboto',15),fg="black",bg="#E6E6FA")
    Label4.place(x=70,y=237)



    # Chargement de la barre de recherche
    image = Image.open(r"search bar.png")

    # Redimensionnement de l'image
    nouvelle_largeur = 500  # Nouvelle largeur de l'image
    nouvelle_hauteur = 200  # Nouvelle hauteur de l'image
    image_redimensionnee = image.resize((nouvelle_largeur, nouvelle_hauteur)) 

    # Conversion de l'image PIL redimensionnée en format PhotoImage pour tkinter
    image_tk1 = ImageTk.PhotoImage(image_redimensionnee)

    # Création d'une étiquette pour afficher l'image
    labele = Label(f, image=image_tk1,bg="#E6E6FA")
    labele.place(x=270,y=120)

    # Création d'une étiquette pour afficher le titre au-dessus de l'image
    titre_label = Label(f, text="Enter city : ", font=("Helvetica", 16), bg="#E6E6FA", fg="#1E90FF")
    titre_label.place(x=350, y=150)
    # Assurez-vous de garder une référence à l'image pour éviter qu'elle ne soit supprimée par le garbage collector
    labele.image = image_tk1

    # Chargement de l'image avec PIL
    weat_ima = Image.open(r"wh.jpg")

    # Redimensionnement de l'image
    nouvelle_largeur = 45  # Nouvelle largeur de l'image
    nouvelle_hauteur = 45  # Nouvelle hauteur de l'image
    image_redimensionnee = weat_ima.resize((nouvelle_largeur, nouvelle_hauteur))

    # Conversion de l'image PIL redimensionnée en format PhotoImage pour tkinter
    image_tk2 = ImageTk.PhotoImage(image_redimensionnee)

    # Création d'une étiquette pour afficher l'image redimensionnée
    weatherim = Label(f, image=image_tk2, bg="white")
    weatherim.place(x=335, y=195)

    # Le texte qu'on saisi dans la bar de recherche
    def obtenir_ville_actuelle():
        # Utilisation du module geocoder pour obtenir les informations de localisation actuelles
        g = geocoder.ip('me')
        # Récupérer le nom de la ville à partir des informations de localisation
        ville = g.city
        return ville
        # Obtention de la ville actuelle
    ville_actuelle = obtenir_ville_actuelle()

    # Création de l'entrée de texte avec la ville actuelle pré-remplie
    textf = Entry(f, justify="center", width=15, font=('Arial', 25, 'bold'), bg='white', border=0, fg="black")
    textf.insert(0, ville_actuelle)  # Pré-remplir avec la ville actuelle
    textf.place(x=380, y=200)
    textf.focus()
    

    # Chargement de l'image
    image1 = Image.open(r"search_ico.png")

    # Redimensionnement de l'image
    nouvelle_largeur = 45
    nouvelle_hauteur = 45
    image_redimensionnee1 = image1.resize((nouvelle_largeur, nouvelle_hauteur))

    # Conversion de l'image PIL redimensionnée en format PhotoImage pour tkinter
    image_tk3 = ImageTk.PhotoImage(image_redimensionnee1)

    # Création d'une étiquette pour afficher l'image
    label = Label(f, image=image_tk3, bg="white")
    # Création d'un bouton avec l'image
    bouton = Button(f, image=image_tk3, borderwidth=0, cursor="hand2", bg="white",command=getweather)
    bouton.place(x=650, y=195)
    label.place(x=650, y=195)

    # Division de la fenetre 
    frame=Frame(f,width=900,height=180,bg="#1E90FF")
    frame.pack(side=BOTTOM)

    # les boxes qu'on aura besoin

    firstbox=PhotoImage(file=r"rounded_rec_1.png")
    secondbox=PhotoImage(file=r"rounded_rec_2.png")
    secondbox = secondbox.subsample(4,4)
    firstbox = firstbox.subsample(2,2) 
    Label(frame,image=firstbox,bg="#1E90FF").place(x=10,y=-40)
    Label(frame,image=secondbox,bg="#1E90FF").place(x=255,y=20)
    Label(frame,image=secondbox,bg="#1E90FF").place(x=385,y=20)
    Label(frame,image=secondbox,bg="#1E90FF").place(x=515,y=20)
    Label(frame,image=secondbox,bg="#1E90FF").place(x=645,y=20)
    Label(frame,image=secondbox,bg="#1E90FF").place(x=775,y=20)
    
    # programation de l'heure 
    clock=Label(f,font=("Hervetica",30,'bold'),fg="black",bg="#E6E6FA")
    clock.place(x=30,y=20)

    # zone du temps
    timezone=Label(f,font=("Helvetica",20),fg="black",bg="#E6E6FA")
    timezone.place(x=600,y=20)

    long_lat=Label(f,font=("Helvetica",15),fg="black",bg="#E6E6FA")
    long_lat.place(x=600,y=50)


    # Label pour afficher le message de ville non trouvée
    not_found_label = Label(f, font=("Helvetica",15),fg="red",bg="#E6E6FA")  # Le texte sera affiché en rouge
    not_found_label.pack()

    city = textf.get()
    api_key="e2382302378f3a9df7e550c3e8633623"
    sunrise, sunset = get_sunrise_sunset(api_key, city)
    label_sunrise = tk.Label(f, text=f"Suntime :", font=("Times New Roman", 18), fg="#1E90FF", bg="#E6E6FA")
    label_sunrise.place(x=710,y=25)
    label_sunrise = tk.Label(f, text=f"          {sunrise}", font=("Arial", 12), bg="#E6E6FA")
    label_sunrise.place(x=710,y=73)
    label_sunset = tk.Label(f, text=f"          {sunset}", font=("Arial", 12), bg="#E6E6FA")
    label_sunset.place(x=710,y=114)
    sunrise_image = Image.open(r"sunrise.png")
    sunset_image = Image.open(r"sunset.png")
    sunrise_resized = sunrise_image.resize((50, 50))
    sunset_resized = sunset_image.resize((50, 50))
    sunrise_tk = ImageTk.PhotoImage(sunrise_resized)
    sunset_tk = ImageTk.PhotoImage(sunset_resized)
    sunrise_image_label = tk.Label(f, image=sunrise_tk, bg="#E6E6FA")
    sunrise_image_label.place(x=690, y=55)
    sunset_image_label = tk.Label(f, image=sunset_tk, bg="#E6E6FA")
    sunset_image_label.place(x=690, y=96)
    # Chargement de l'image
    icon_temp = Image.open("temperature.png")


    # Redimensionnement de l'image
    nouvelle_largeur = 35
    nouvelle_hauteur = 25
    image_redimensionnee12 = icon_temp.resize((nouvelle_largeur, nouvelle_hauteur))

    # Conversion de l'image PIL redimensionnée en format PhotoImage pour tkinter
    image_tk12 = ImageTk.PhotoImage(image_redimensionnee12)
    # Créer un label pour afficher l'image
    label_image = Label(f, image=image_tk12,bg="#E6E6FA")
    label_image.place(x=30, y=150)


    # Chargement de l'image humidite
    icon_temp2 = Image.open("humidity.png")


    # Redimensionnement de l'image
    nouvelle_largeur = 35
    nouvelle_hauteur = 30
    image_redimensionnee14 = icon_temp2.resize((nouvelle_largeur, nouvelle_hauteur))

    # Conversion de l'image PIL redimensionnée en format PhotoImage pour tkinter
    image_tk14 = ImageTk.PhotoImage(image_redimensionnee14)
    # Créer un label pour afficher l'image
    label_image = Label(f, image=image_tk14,bg="#E6E6FA")
    label_image.place(x=30, y=178)


    # Chargement de l'image pression
    icon_temp5 = Image.open("pression.png")


    # Redimensionnement de l'image
    nouvelle_largeur = 25
    nouvelle_hauteur = 25
    image_redimensionnee15 = icon_temp5.resize((nouvelle_largeur, nouvelle_hauteur))

    # Conversion de l'image PIL redimensionnée en format PhotoImage pour tkinter
    image_tk15 = ImageTk.PhotoImage(image_redimensionnee15)
    # Créer un label pour afficher l'image
    label_image = Label(f, image=image_tk15,bg="#E6E6FA")
    label_image.place(x=30, y=209)

    # Chargement de l'image Pour le vent
    icon_temp1 = Image.open("vent.png")


    # Redimensionnement de l'image
    nouvelle_largeur = 35
    nouvelle_hauteur = 25
    image_redimensionnee13 = icon_temp1.resize((nouvelle_largeur, nouvelle_hauteur))

    # Conversion de l'image PIL redimensionnée en format PhotoImage pour tkinter
    image_tk13 = ImageTk.PhotoImage(image_redimensionnee13)
    # Créer un label pour afficher l'image
    label_image = Label(f, image=image_tk13,bg="#E6E6FA")
    label_image.place(x=30, y=240)

    
    # Les parametres de meteo:
    temp= Label(f,font=("Helvetica",11),fg="black",bg="#E6E6FA")
    temp.place(x=195,y=155)
    hum= Label(f,font=("Helvetica",11),fg="black",bg="#E6E6FA")
    hum.place(x=195,y=185)
    pres= Label(f,font=("Helvetica",11),fg="black",bg="#E6E6FA")
    pres.place(x=195,y=213)
    vent= Label(f,font=("Helvetica",11),fg="black",bg="#E6E6FA")
    vent.place(x=195,y=242)


    # premier appel
    firstframe=Frame(f,width=199,height=114,bg="#1E90FF")
    firstframe.place(x=36,y=336)

    day1 = Label(firstframe, font="Helvetica 20", bg="#1E90FF", fg="white")
    day1.place(x=90,y=5)

    firstimage=Label(firstframe,width=50,height=50,bg="#1E90FF")
    firstimage.place(x=1,y=15)

    day1temp=Label(firstframe,bg="#1E90FF",fg="#ADAEAF",font="arial 15 bold")
    day1temp.place(x=80,y=50)

    # deuxieme appel
    secondframe=Frame(f,width=93,height=120,bg="#1E90FF")
    secondframe.place(x=265,y=330)

    day2 = Label(secondframe, bg="#1E90FF", fg="white")
    day2.place(x=10,y=5)

    secondimage=Label(secondframe,bg="#1E90FF")
    secondimage.place(x=7,y=20)

    day2temp=Label(secondframe,bg="#1E90FF",fg="#fff")
    day2temp.place(x=10,y=70)

    # 3 eme appel 
    thirdframe=Frame(f,width=93,height=120,bg="#1E90FF")
    thirdframe.place(x=397,y=330)

    day3 = Label(thirdframe, bg="#1E90FF", fg="white")
    day3.place(x=10,y=5)


    thirdimage=Label(thirdframe,bg="#1E90FF")
    thirdimage.place(x=7,y=20)

    day3temp=Label(thirdframe,bg="#1E90FF",fg="#fff")
    day3temp.place(x=10,y=70)

    # 4eme appel
    quatreframe=Frame(f,width=93,height=120,bg="#1E90FF")
    quatreframe.place(x=527,y=330)

    day4 = Label(quatreframe, bg="#1E90FF", fg="white")
    day4.place(x=10,y=5)

    quatreimage=Label(quatreframe,bg="#1E90FF")
    quatreimage.place(x=7,y=20)

    day4temp=Label(quatreframe,bg="#1E90FF",fg="#fff")
    day4temp.place(x=10,y=70)

    # 5eme appel
    cinqframe=Frame(f,width=93,height=120,bg="#1E90FF")
    cinqframe.place(x=658,y=330)

    day5 = Label(cinqframe, bg="#1E90FF", fg="white")
    day5.place(x=10,y=5)

    cinqimage=Label(cinqframe,bg="#1E90FF")
    cinqimage.place(x=7,y=20)

    day5temp=Label(cinqframe,bg="#1E90FF",fg="#fff")
    day5temp.place(x=10,y=70)

    # 6eme appel
    sixframe=Frame(f,width=93,height=120,bg="#1E90FF")
    sixframe.place(x=788,y=330)

    day6 = Label(sixframe, bg="#1E90FF", fg="white")
    day6.place(x=10,y=5)

    siximage=Label(sixframe,bg="#1E90FF")
    siximage.place(x=7,y=20)

    day6temp=Label(sixframe,bg="#1E90FF",fg="#fff")
    day6temp.place(x=10,y=70)
    getweather()
    f.mainloop()

