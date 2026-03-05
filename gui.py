import tkinter as tk
from shunting_yard import infix_to_postfix, evaluate_postfix, tokenize
from gestion_erreurs import gestion_denominateur_zero, gestion_parantheses, gestion_nombre, gestion_opérateur, gestion_expression_invalide, ParanthesesError, NombreError, OpérateurError 

fenetre = tk.Tk()
fenetre.title("Calculatrice")
titre_champ_de_saisie = tk.Label(fenetre, text="Entrez une expression :")
titre_champ_de_saisie.pack()
champ_de_saisie = tk.Entry(fenetre)
champ_de_saisie.pack()

def valeur_terme():
    gestion_erreur.delete('1.0', tk.END)
    resultats_notation_postifixée.delete('1.0', tk.END)
    resultat_évaluation.delete('1.0', tk.END)
    try:
        gestion_parantheses(champ_de_saisie.get())
        gestion_nombre(champ_de_saisie.get())
        gestion_opérateur(champ_de_saisie.get())
        gestion_denominateur_zero(champ_de_saisie.get())
        gestion_expression_invalide(champ_de_saisie.get())
    except IndexError as e:
        gestion_erreur.insert(tk.END, f"Expression Invalide: {e}")
    except ZeroDivisionError as e:
        gestion_erreur.insert(tk.END, f"Division par zéro : {e}")
    except ParanthesesError as e:
        gestion_erreur.insert(tk.END, f"Paranthèses non appariées : {e}")
    except OpérateurError as e:
        gestion_erreur.insert(tk.END, f"Opérateur inconnu : {e}")
    except NombreError as e:
        gestion_erreur.insert(tk.END, f"Nombre mal formé : {e}")
    else:
        expression = infix_to_postfix(tokenize(champ_de_saisie.get()))
        evaluation = evaluate_postfix(expression)
        resultats_notation_postifixée.insert(tk.END, expression)
        resultat_évaluation.insert(tk.END, evaluation)
        gestion_erreur.insert(tk.END, "Aucune erreur détectée.")
        
bouton_calculer = tk.Button(fenetre, text="Calculer", command = valeur_terme)
bouton_calculer.pack()
titre_notation_postifixée = tk.Label(fenetre, text="Notation postifixée :")
titre_notation_postifixée.pack()
resultats_notation_postifixée = tk.Text(fenetre, height=5, width=50)
resultats_notation_postifixée.pack()
titre_évaluation = tk.Label(fenetre, text="Évaluation :")
titre_évaluation.pack()
resultat_évaluation = tk.Text(fenetre, height=5, width=50)
resultat_évaluation.pack()
titre_gestion_erreur = tk.Label(fenetre, text="Gestion d'erreur :")
titre_gestion_erreur.pack()
gestion_erreur = tk.Text(fenetre, height=5, width=50)
gestion_erreur.pack()

fenetre.mainloop()
