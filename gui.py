import tkinter as tk
from shunting_yard import infix_to_postfix, tokenize, evaluate_postfix

fenetre = tk.Tk()
champ_de_saisie = tk.Entry(fenetre)
champ_de_saisie.pack()

def valeur_terme():
    #try:
        expression = infix_to_postfix(tokenize(champ_de_saisie.get()))
        evaluation = evaluate_postfix(expression)
        resultats_notation_postifixée.config(text=expression)
        resultat_évaluation.config(text=evaluation)
    


bouton_calculer = tk.Button(fenetre, text="Calculer", command = valeur_terme)
bouton_calculer.pack()
resultats_notation_postifixée = tk.Label(fenetre, text="")
resultats_notation_postifixée.pack()
resultat_évaluation = tk.Label(fenetre, text="")
resultat_évaluation.pack()



fenetre.mainloop()


# def cliquer():
#     etiquette.config(text="Vous avez cliqué !")

# fenetre = tk.Tk()

# etiquette = tk.Label(fenetre, text="")
# etiquette.pack()

# bouton = tk.Button(fenetre, text="Cliquez ici", command=cliquer)
# bouton.pack()

# fenetre.mainloop()