import statistics
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter.messagebox import *
from turtle import bgcolor
import matplotlib
matplotlib.use('Agg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)


fichier = "test.csv"
Tableau = pd.read_csv(fichier, delimiter=",")

# #Appel des  Colonnes___________________________________________________________________________________
_n_dose1_0 = Tableau.n_dose1_0
_n_dose1_2 = Tableau.n_dose1_1
_n_dose1_1 = Tableau.n_dose1_2

#Colonne contenant le numéro des départements de France allant de 1 à 94
regions = Tableau.reg

# # Calcul des Moyennes____Médianes____Modes_____des Enfants______________________________________________________________________

Moyenne_n_dose1_0 = statistics.mean(_n_dose1_0)
Mediane_n_dose1_0 = statistics.median(_n_dose1_0)
Mode_n_dose1_0 = statistics.mode(_n_dose1_0)

# # Calcul des Moyennes____Médianes____Modes_____des Hommes______________________________________________________________________

Moyenne_n_dose1_1 = statistics.mean(_n_dose1_1)
Mediane_n_dose1_1 = statistics.median(_n_dose1_1)
Mode_n_dose1_1 = statistics.mode(_n_dose1_1)

# # Calcul des Moyennes____Médianes____Modes_____des Femmes______________________________________________________________________

Moyenne_n_dose1_2 = statistics.mean(_n_dose1_2)
Mediane_n_dose1_2 = statistics.median(_n_dose1_2)
Mode_n_dose1_2 = statistics.mode(_n_dose1_2)


#IHM Tkinter_______________________________________________________ 


Projet = Tk()

Projet.title('Espace graphique')
Projet.geometry('600x400')
Projet.minsize(450, 360)
Projet.config(background='#C3D6D3')


frame = Frame(Projet, bg='#87CEEB' )
frame.pack(side=TOP, expand=Y, fill=BOTH, pady=5, padx=5)

# label_titre_0 = Label(frame,  text = "VARIABLES STATISTIQUES DES ENFANTS", font=('time 22 bold', 10), bg='#87CEEB')
# label_titre_0.pack(expand=YES, padx=5, pady=5)

Frame1 = Frame(frame, bg='#1E4589', borderwidth='1' )
Frame1.pack(expand=YES, padx=0, pady=0)
label_titre0_0 = Label(Frame1,  text = "Moyenne", font=('time 22 bold', 10), bg='#87CEEB')
label_titre0_0.grid(row=1, column=1)

Data_Entry0_0=Entry(Frame1, font=("Arial", 10), fg='#070D32')
Data_Entry0_0.grid(row=2, column=1)

label_titre1_0 = Label(Frame1,  text = "Médiane", font=('time 22 bold', 10), bg='#87CEEB')
label_titre1_0.grid(row=1, column=2)

Data_Entry1_0=Entry(Frame1, font=("Arial", 10), fg='#070D32')
Data_Entry1_0.grid(row=2, column=2)

label_titre2_0 = Label(Frame1,  text = "Mode", font=('time 22 bold', 10), bg='#87CEEB')
label_titre2_0.grid(row=1, column=3)

Data_Entry2_0=Entry(Frame1, font=("Arial", 10), fg='#070D32')
Data_Entry2_0.grid(row=2, column=3)

#Deuxieme rangées

Frame2 = Frame(frame, bg='#BE155F', borderwidth='1' )
Frame2.pack(expand=YES, padx=0, pady=0)
label_titre0_0 = Label(Frame2,  text = "Moyenne", font=('time 22 bold', 10), bg='#FF5F4C')
label_titre0_0.grid(row=3, column=1)

Data_Entry0_0=Entry(Frame2, font=("Arial", 10), fg='#070D32')
Data_Entry0_0.grid(row=4, column=1)

label_titre1_0 = Label(Frame2,  text = "Médiane", font=('time 22 bold', 10), bg='#FF5F4C')
label_titre1_0.grid(row=3, column=2)

Data_Entry1_0=Entry(Frame2, font=("Arial", 10), fg='#070D32')
Data_Entry1_0.grid(row=4, column=2)

label_titre2_0 = Label(Frame2,  text = "Mode", font=('time 22 bold', 10), bg='#FF5F4C')
label_titre2_0.grid(row=3, column=3)

Data_Entry2_0=Entry(Frame2, font=("Arial", 10), fg='#070D32')
Data_Entry2_0.grid(row=4, column=3)

#Troisieme rangées

Frame3 = Frame(frame, bg='#418109', borderwidth='1' )
Frame3.pack(expand=YES, padx=0, pady=0)
label_titre0_0 = Label(Frame3,  text = "Moyenne", font=('time 22 bold', 10), bg='#A0FF4C')
label_titre0_0.grid(row=3, column=1)

Data_Entry0_2=Entry(Frame3, font=("Arial", 10), fg='#070D32')
Data_Entry0_2.grid(row=4, column=1)

label_titre1_2 = Label(Frame3,  text = "Médiane", font=('time 22 bold', 10), bg='#A0FF4C')
label_titre1_2.grid(row=3, column=2)

Data_Entry1_2=Entry(Frame3, font=("Arial", 10), fg='#070D32')
Data_Entry1_2.grid(row=4, column=2)

label_titre2_2 = Label(Frame3,  text = "Mode", font=('time 22 bold', 10), bg='#A0FF4C')
label_titre2_2.grid(row=3, column=3)

Data_Entry2_2=Entry(Frame3, font=("Arial", 10), fg='#070D32')
Data_Entry2_2.grid(row=4, column=3)





# frame 2


Projet.mainloop()





