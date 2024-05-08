import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime  # Import datetime from the datetime module
import requests
from tkinter import messagebox

global ville_entry
global sunrise_label
global sunset_label

def rechercher_ville(event=None):
    city_name = ville_entry.get()
    sunrise, sunset = fetch_weather_data(city_name)
    if sunrise and sunset:
        sunrise_label.config(text=f"Sunrise : {convert_timestamp_to_time(sunrise)} AM", fg="green", font=("Arial", 12, "italic"))
        sunset_label.config(text=f"Sunset : {convert_timestamp_to_time(sunset)} PM", fg="green", font=("Arial", 12, "italic"))

    else:
        sunrise_label.config(text="Failed to fetch data")
        sunset_label.config(text="Failed to fetch data")

def fetch_weather_data(city_name):
    api_key = 'e2382302378f3a9df7e550c3e8633623'  # Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    
    try:
        response = requests.get(url)
        data = response.json()
        sunrise = data['sys']['sunrise']
        sunset = data['sys']['sunset']
        return sunrise, sunset
    except Exception as e:
        print("Error fetching weather data:", e)
        return None, None

def convert_timestamp_to_time(timestamp):
    return datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')

def write_to_search_bar(character):
    current_text = ville_entry.get()
    ville_entry.delete(0, tk.END)
    ville_entry.insert(tk.END, current_text + character)

def open_virtual_keyboard():
    virtual_keyboard_window = tk.Toplevel()
    virtual_keyboard_window.title("Clavier Visuel")
    
    # Création des boutons pour chaque touche du clavier
    buttons = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'
    ]
    
    row, col = 0, 0
    for button in buttons:
        button_label = tk.Button(virtual_keyboard_window, text=button, width=3, command=lambda b=button: write_to_search_bar(b))
        button_label.grid(row=row, column=col, padx=5, pady=5)
        col += 1
        if col > 10:
            col = 0
            row += 1
        button_label = tk.Button(virtual_keyboard_window, text='Backspace', command=lambda b=button: ville_entry.delete(len(ville_entry.get()) - 1))
        button_label.place(x=128,y=114)
        button_label = tk.Button(virtual_keyboard_window, text='Space', command=lambda b=button: write_to_search_bar(' '))
        button_label.place(x=205,y=114)
        button_label = tk.Button(virtual_keyboard_window, text='Enter', command=rechercher_ville)
        button_label.place(x=258,y=114)

def affiche_sunrise_sunset():
    root = tk.Toplevel()
    root.title("Sunrise and Sunset") # Titre de la fenettre
    root.geometry("890x479+300+200") #la geometrie de la fenettre 
    root.configure(bg="#E6E6FA") #determiner la couleur du fond ecran
    root.resizable(False,False) # la fenettre n'est definie fixe

    global ville_entry
    global sunrise_label
    global sunset_label

    # Chargement des images de lever et coucher de soleil
    sunrise_image = Image.open(r"sunrise.png")
    sunset_image = Image.open(r"sunset.png")
    bow=Image.open(r"bow.png")
    bow_resized = bow.resize((750, 160))
    bow_tk=ImageTk.PhotoImage(bow_resized)
    bow_label=tk.Label(root, image=bow_tk,bg="#E6E6FA")
    bow_label.place(x=80, y=133)
    # Redimensionnement des images
    sunrise_resized = sunrise_image.resize((100, 100))
    sunset_resized = sunset_image.resize((100, 100))

    # Conversion des images PIL en format PhotoImage pour tkinter
    sunrise_tk = ImageTk.PhotoImage(sunrise_resized)
    sunset_tk = ImageTk.PhotoImage(sunset_resized)

    # Création d'une étiquette pour afficher l'image de lever de soleil
    sunrise_image_label = tk.Label(root, image=sunrise_tk, bg="#E6E6FA")
    sunrise_image_label.place(x=100, y=280)

    # Création d'une étiquette pour afficher l'image de coucher de soleil
    sunset_image_label = tk.Label(root, image=sunset_tk, bg="#E6E6FA")
    sunset_image_label.place(x=700, y=280)

    # Création d'une étiquette pour afficher l'heure de lever du soleil
    sunrise_label = tk.Label(root, text="Sunrise Time:", font=("Arial", 12), bg="#E6E6FA")
    sunrise_label.place(x=100, y=380)

    # Création d'une étiquette pour afficher l'heure de coucher du soleil
    sunset_label = tk.Label(root, text="Sunset Time:", font=("Arial", 12), bg="#E6E6FA")
    sunset_label.place(x=710, y=380)

    # Chargement de l'image de la barre de recherche
    search_bar_image = Image.open(r"search bar.png")
    search_bar_resized = search_bar_image.resize((500, 200))
    search_bar_tk = ImageTk.PhotoImage(search_bar_resized)

    # Création d'une étiquette pour afficher l'image de la barre de recherche
    search_bar_label = tk.Label(root, image=search_bar_tk, bg="#E6E6FA")
    search_bar_label.place(x=210, y=-4)

    # Création d'une étiquette pour afficher le titre au-dessus de l'image
    titre_label = tk.Label(root, text="Enter ville : ", font=("Helvetica", 16), bg="#E6E6FA", fg="#1E90FF")
    titre_label.place(x=360, y=20)

    # Widget Entry pour saisir le nom de la ville
    ville_entry = tk.Entry(root, justify="center", width=15, font=('Arial', 25, 'bold'), bg='white', border=0, fg="black")
    ville_entry.place(x=280, y=75)
    ville_entry.focus()
    ville_entry.bind('<Return>', rechercher_ville)  # Lier la fonction rechercher_ville à l'événement "Entrée"

    # Chargement de l'image de la loupe
    search_ico_image = Image.open(r"search_ico.png")
    search_ico_resized = search_ico_image.resize((45, 45))
    search_ico_tk = ImageTk.PhotoImage(search_ico_resized)
    # Création d'une cloud sur la  loupe (pour une meilleure visibilité)
    cloud = Image.open(r"wh.jpg")
    cloud_resized = cloud.resize((45, 45))
    cloud_tk = ImageTk.PhotoImage(cloud_resized)
    cloud_lab = tk.Label(root, image=cloud_tk, bg="white")
    cloud_lab.place(x=280, y=73)
    # Création d'un bouton avec l'image de la loupe
    bouton = tk.Button(root, image=search_ico_tk, borderwidth=0, cursor="hand2", bg="white", command=rechercher_ville)
    bouton.place(x=590, y=75)



    keyboard_image = Image.open("keyboard.png")
    keyboard_resized = keyboard_image.resize((45, 45))
    keyboard_tk = ImageTk.PhotoImage(keyboard_resized)

    clavier_button = tk.Button(root, image=keyboard_tk, command=open_virtual_keyboard, bd=0,bg='#E6E6FA')
    clavier_button.place(x=810, y=75)
    # Bouton pour ouvrir le clavier visuel
   

    root.mainloop()