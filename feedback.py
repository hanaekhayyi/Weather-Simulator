from tkinter import *
from tkinter import messagebox

def run_rating_app():
    root = Toplevel()
    root.geometry("450x200+300+200")
    root.resizable(False,False)
    app = RatingApp(root)
    root.mainloop()

class RatingApp:
    def __init__(self, parent):
        self.parent = parent
        parent.title("Feedback")
        parent.configure(bg="#F0F0F0")  # Couleur de fond

        self.star_frame = Frame(parent, bg="#F0F0F0")
        self.star_frame.pack(pady=20)

        self.star_rating = 0

        self.star_buttons = []
        for i in range(5):
            star_button = Button(self.star_frame, text="★", bg="#F0F0F0", font=("Helvetica", 20),
                                    command=lambda i=i+1: self.set_rating(i), bd=0, highlightthickness=0)
            star_button.grid(row=0, column=i, padx=5)
            self.star_buttons.append(star_button)

        # Bouton avec une image pour Submit
        self.submit_image_button =Button(parent, command=self.submit_rating_and_close)
        submit_img = PhotoImage(file="submit.png")
        self.submit_image_button.config(image=submit_img, width="200", height="90", bg="#F0F0F0", bd=0, highlightthickness=0)
        self.submit_image_button.image = submit_img  # Gardez une référence à l'image pour éviter la suppression par le garbage collector
        self.submit_image_button.pack(side="left", padx=(30, 10), pady=10)  # Augmenter la marge à gauche de 30 pixels
        #################

        # Bouton avec une image pour Clear
        self.clear_image_button = Button(parent, command=self.image_button_click)
        clear_img = PhotoImage(file="cancel.png")
        self.clear_image_button.config(image=clear_img, width="150", height="70", bg="#F0F0F0", bd=0, highlightthickness=0)
        self.clear_image_button.image = clear_img  # Gardez une référence à l'image pour éviter la suppression par le garbage collector
        self.clear_image_button.pack(side="left", padx=(10, 30), pady=10)  # Augmenter la marge à droite de 30 pixels

    def set_rating(self, rating):
        self.star_rating = rating
        for i in range(rating):
            self.star_buttons[i].config(fg="#FFD700")  # Couleur jaune pour les étoiles sélectionnées
        for i in range(rating, 5):
            self.star_buttons[i].config(fg="#D3D3D3")  # Couleur grise pour les étoiles non sélectionnées

    def submit_rating_and_close(self):
        messagebox.showinfo("Thank you !", f"You have rated {self.star_rating} stars!")
        self.parent.destroy()

    def image_button_click(self):
        # Réinitialiser la note donnée et réinitialiser l'apparence des étoiles
        self.star_rating = 0
        for button in self.star_buttons:
            button.config(fg="#D3D3D3")  # Réinitialiser la couleur de toutes les étoiles à grise



