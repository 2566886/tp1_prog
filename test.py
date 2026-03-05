import tkinter as tk

root = tk.Tk()
root.title("Exemple avec Frame")

# Créer deux cadres
top_frame = tk.Frame(root, bg="lightblue")
bottom_frame = tk.Frame(root, bg="lightgreen")

# Placer les cadres
top_frame.pack(fill="both", expand=True)
bottom_frame.pack(fill="both", expand=True)

# Ajouter des widgets dans chaque cadre
tk.Label(top_frame, text="Haut de la fenêtre").pack(pady=10)
tk.Button(bottom_frame, text="Bouton en bas").pack(pady=10)

root.mainloop()