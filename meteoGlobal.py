import tkinter as tk
import webview
import requests
import folium

# Fonction pour obtenir les données météorologiques d'une ville depuis l'API OpenWeatherMap
def obtenir_donnees_meteo(ville, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ville}&appid={api_key}&units=metric"
    reponse = requests.get(url)
    donnees = reponse.json()
    return donnees

def get_icon(description):
    description_lower = description.lower()
    if "cloud" in description_lower:
        return "cloud" if "few clouds" not in description_lower else "cloud-sun"
    elif "rain" in description_lower or "shower" in description_lower:
        return "cloud-showers-heavy"
    elif "snow" in description_lower:
        return "snowflake"
    elif "sun" in description_lower or "clear" in description_lower:
        return "sun"
    elif "fog" in description_lower or "mist" in description_lower or "haze" in description_lower:
        return "smog"
    elif "wind" in description_lower:
        return "wind"
    elif "smoke" in description_lower:  # Ajout de la condition pour "smoke"
        return "smoke"
    else:
        return "question-circle"


# Fonction pour créer une carte météorologique interactive avec des marqueurs pour chaque ville
def creer_carte_meteo(villes, api_key):
    carte = folium.Map(location=[0, 0], zoom_start=2)  # Créer une carte centrée sur l'équateur avec un zoom de départ de 2

    for ville in villes:
        donnees_meteo = obtenir_donnees_meteo(ville, api_key)
        latitude = donnees_meteo['coord']['lat']
        longitude = donnees_meteo['coord']['lon']
        temperature = donnees_meteo['main']['temp']
        description = donnees_meteo['weather'][0]['description']
        
        # Obtenir l'icône correspondant à la description météorologique
        icon = get_icon(description)
        
        # Créer un marqueur avec une icône personnalisée
        marker = folium.Marker(
            location=[latitude, longitude],
            popup=f"{ville}<br>Température : {temperature}°C<br>{description}",
            icon=folium.Icon(icon=icon, prefix="fa")
        )
        marker.add_to(carte)

    return carte

villes = ['Paris', 'New York', 'Tokyo', 'Sydney', 'Rabat', 'London', 'Los Angeles', 'Beijing', 'Moscow', 'Dubai', 'Rio de Janeiro', 'Cairo', 'Berlin', 'Toronto', 'Mexico City', 'Bangkok', 'Singapore', 'Istanbul', 'Mumbai', 'Seoul', 'Rome']

# Clé API OpenWeatherMap
api_key = "e2382302378f3a9df7e550c3e8633623"

# Créer la carte météorologique interactive
carte_meteo = creer_carte_meteo(villes, api_key)

# Enregistrer la carte au format HTML
carte_meteo.save('carte_meteo.html')

# Fonction pour afficher le fichier HTML dans une fenêtre tkinter
def afficher_carte_html():
    webview.create_window("Carte Météo", "carte_meteo.html", width=890, height=479)
    webview.start()


