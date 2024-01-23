import tkinter as tk
from readScreen import getText

# Fonction à appeler lors du clic sur le bouton
def on_button_click():
    label_result.config(text="Bonjour, " + getText(entry_name.get()))

# Création de la fenêtre principale
root = tk.Tk()
root.title("Ma Première Interface")

# Ajout d'une étiquette
label_name = tk.Label(root, text="Entrez votre nom:")
label_name.pack(pady=10)


# Ajout d'une zone de saisie
entry_name = tk.Entry(root)
entry_name.pack(pady=10)

# Ajout d'un bouton
button_submit = tk.Button(root, text="Valider", command=on_button_click)
button_submit.pack(pady=10)

# Ajout d'une étiquette pour afficher le résultat
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Boucle principale de l'application
root.mainloop()
