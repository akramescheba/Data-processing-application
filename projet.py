#Import des bibliothèques
import statistics
from tkinter.font import BOLD
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

#Import de la base des données

fichier = "vacsisreg2022062420h24_.csv"
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
Projet.config(background='#04318B')

#Insertion de frame dans la fenetre Projet
frame = Frame(Projet, bg='#B4C1BB', borderwidth=2, relief=GROOVE)
frame.pack(side=TOP, expand=Y, fill=BOTH, pady=5, padx=5)

label_titre_frame = Label(frame,  text = "ANALYSE DES DONNEES PAR DEPARTEMENT DE LA POP AYANT SUBIT LA 1ERE DOSE DE VACCINS CONTRE LE COVID", font=('courier', 12), borderwidth=3, relief="ridge", bg='#D6DBDD')
label_titre_frame.pack(side= TOP, fill=BOTH, pady=2, padx=250)

# Frame1 à gauche contenant les graph
Frame1 = Frame(frame, bg='#18CAEA', borderwidth=5, relief=GROOVE)
Frame1.pack(expand=YES,side=LEFT,padx=10, pady=10)

# Frame2 à droite contenant le calcul des variables
Frame2 = Frame(frame, borderwidth=5,  bg='#B5C4CA', relief=GROOVE)
Frame2.pack(expand=YES,side=RIGHT, padx=10, pady=10)

#Footer contenant mon adresse mail
label_Footer_frame = Label(frame,text = "meschebajordy@gmail.com", font=('courier',12), borderwidth=3, relief="ridge", bg='#B4C1BB')
label_Footer_frame.place(relx = 0.0, rely = 1.0, anchor ='sw')

#__Fonction_exécutants_le_boutons__VARIABLES__________________ 

def statistic():
    #Variables statistiques des enfants
    Moyenne0 = Moyenne_n_dose1_0, 
    Mediane0 = Mediane_n_dose1_0, 
    Mode0 = Mode_n_dose1_0
    
    Data_Entry0_0.delete(0, END)
    Data_Entry0_0.insert(0,  Moyenne0)
    
    Data_Entry1_0.delete(0, END)
    Data_Entry1_0.insert(0,  Mediane0)
    
    Data_Entry2_0.delete(0, END)
    Data_Entry2_0.insert(0,  Mode0)
    
    #Variables statistiques des hommes
    Moyenne1 = Moyenne_n_dose1_1, 
    Mediane1 = Mediane_n_dose1_1, 
    Mode1 = Mode_n_dose1_1 
    
    Data_Entry0_1.delete(0, END)
    Data_Entry0_1.insert(0,  Moyenne1)
    
    Data_Entry1_1.delete(0, END)
    Data_Entry1_1.insert(0,  Mediane1)
    
    Data_Entry2_1.delete(0, END)
    Data_Entry2_1.insert(0,  Mode1)
    #Variables statistiques des femmes
    Moyenne2 = Moyenne_n_dose1_2 
    Mediane2 = Mediane_n_dose1_2 
    Mode2 = Mode_n_dose1_2 
    
    Data_Entry0_2.delete(0, END)
    Data_Entry0_2.insert(0,  Moyenne2)
    
    Data_Entry1_2.delete(0, END)
    Data_Entry1_2.insert(0,  Mediane2)
    
    Data_Entry2_2.delete(0, END)
    Data_Entry2_2.insert(0,  Mode2)

 #__Fonction_exécutants_le_boutons__GRAPHIQUES__________________

def Histogramme():
   
    plt.rcParams['axes.facecolor'] = '#CCD6D6'
    Fig=Figure(figsize=(10, 10), dpi = 100) 
    Histo = Fig.add_subplot(121)
    
    y_0 = (_n_dose1_0)
    y_1 = (_n_dose1_1)
    y_2 = (_n_dose1_2)
    x = (regions)
    
    labels =  'Enfants', 'Hommes', 'Femmes'
    colors = ['blue', 'red', 'green']
    
    #Histogrammes
    
    Histo.hist([y_0,y_1,y_2 ],  range=(0, 100), bins=x,
                color=colors,
                edgecolor='White',label='Dose',
                rwidth=1, histtype='bar')
  
   #Diagramme de secteurs
   
    Circ = Fig.add_subplot(2,2,2)
    Circ.pie([ Moyenne_n_dose1_0, Moyenne_n_dose1_1,Moyenne_n_dose1_2], 
        labels=labels, 
        colors=colors, 
        autopct='%1.1f%%',
        shadow=True, 
        startangle=0 )

    #Boite à moustache
    
    Boite = Fig.add_subplot(2,2,4)
    Boite.boxplot([Mediane_n_dose1_0, Mediane_n_dose1_1, Mediane_n_dose1_2])
    plt.show()
   
    # Insertion des graphique dans Tkinter
    # création du Tkinter canvas contenant la figure Matplotlib 
    canvas = FigureCanvasTkAgg(Fig, Frame1)  
    
    # Insertion du canvas dans la fenetre Projet Tkinter
    canvas.get_tk_widget().pack()
  
    # Création de la barre d'outils Matplotlib
    toolbar = NavigationToolbar2Tk(canvas, Frame1)
    toolbar.update()
    
    canvas.get_tk_widget().pack()
#Tkinter_______________________________________________________ 
# Premiere rangée des Entrées contenant les variables des Enfants
label_titre_0 = Label(Frame2,  text = "VARIABLES STATISTIQUES DES ENFANTS", font=('courier', 10), bg='#B5C4CA')
label_titre_0.pack()

FrameA = Frame(Frame2, bg='#1E4589', borderwidth='1' )
FrameA.pack(expand=YES, padx=0, pady=0)

label_titre0_0 = Label(FrameA,  text = "Moyenne", font=('courier', 10), bg='#87CEEB')
label_titre0_0.grid(row=1, column=1)

Data_Entry0_0=Entry(FrameA, font=('courier', 10), fg='#070D32')
Data_Entry0_0.grid(row=2, column=1)

label_titre1_0 = Label(FrameA,  text = "Médiane", font=('courier', 10), bg='#87CEEB')
label_titre1_0.grid(row=1, column=2)

Data_Entry1_0=Entry(FrameA, font=('courier', 10), fg='#070D32')
Data_Entry1_0.grid(row=2, column=2)

label_titre2_0 = Label(FrameA,  text = "Mode", font=('courier', 10), bg='#87CEEB')
label_titre2_0.grid(row=1, column=3)

Data_Entry2_0=Entry(FrameA, font=('courier', 10), fg='#070D32')
Data_Entry2_0.grid(row=2, column=3)

#Deuxieme rangées des Entrées contenant les variables des Hommes
label_titre_1 = Label(Frame2,  text = "VARIABLES STATISTIQUES DES HOMMES", font=('courier', 10),  bg='#B5C4CA')
label_titre_1.pack()

FrameB = Frame(Frame2, bg='#BE155F', borderwidth='1' )
FrameB.pack(expand=YES, padx=0, pady=0)

label_titre0_1 = Label(FrameB,  text = "Moyenne", font=('courier', 10), bg='#FF5F4C')
label_titre0_1.grid(row=3, column=1)

Data_Entry0_1=Entry(FrameB, font=('courier', 10), fg='#070D32')
Data_Entry0_1.grid(row=4, column=1)

label_titre1_1 = Label(FrameB,  text = "Médiane", font=('courier', 10),  bg='#FF5F4C')
label_titre1_1.grid(row=3, column=2)

Data_Entry1_1=Entry(FrameB, font=('courier', 10), fg='#070D32')
Data_Entry1_1.grid(row=4, column=2)

label_titre2_1 = Label(FrameB,  text = "Mode", font=('courier', 10),  bg='#FF5F4C')
label_titre2_1.grid(row=3, column=3)

Data_Entry2_1=Entry(FrameB, font=('courier', 10), fg='#070D32')
Data_Entry2_1.grid(row=4, column=3)

#Troisieme rangées des Entrées contenant les variables des Femmes
label_titre_2 = Label(Frame2,  text = "VARIABLES STATISTIQUES DES FEMMES", font=('courier', 10),  bg='#B5C4CA')
label_titre_2.pack()

FrameD = Frame(Frame2, bg='#418109', borderwidth='1' )
FrameD.pack(expand=YES, padx=0, pady=0)

label_titre0_2 = Label(FrameD,  text = "Moyenne", font=('courier', 10),  bg='#A0FF4C')
label_titre0_2.grid(row=3, column=1)

Data_Entry0_2=Entry(FrameD, font=('courier', 10), fg='#070D32')
Data_Entry0_2.grid(row=4, column=1)

label_titre1_2 = Label(FrameD,  text = "Médiane", font=('courier', 10),  bg='#A0FF4C')
label_titre1_2.grid(row=3, column=2)

Data_Entry1_2=Entry(FrameD, font=('courier', 10), fg='#070D32')
Data_Entry1_2.grid(row=4, column=2)

label_titre2_2 = Label(FrameD,  text = "Mode", font=('courier', 10),  bg='#A0FF4C')
label_titre2_2.grid(row=3, column=3)

Data_Entry2_2=Entry(FrameD, font=('courier', 10), fg='#070D32')
Data_Entry2_2.grid(row=4, column=3)

#___Boutons__VARIABLES___________________________________________
Bouton1= Button (Frame2, text='VARIABLES', 
font=('courier', 8), underline= 1,  
width=10, height=1, bg='blue', fg='White',activebackground='green',
activeforeground='#BDBDBD', borderwidth='5', relief=RIDGE, 
command=statistic).pack(side=LEFT, padx=5, pady=5)

#___Boutons__GRAPHIQUES___________________________________________
Bouton2= Button (Frame2, text='GRAPHIQUES', 
font=('courier', 8), underline= 1,  
width=10, height=1, bg='red', fg='White',activebackground='green',
activeforeground='#BDBDBD', borderwidth='5', relief=RIDGE, 
command=Histogramme).pack(side=RIGHT, padx=5, pady=5)


#___FEMETURE DE LA FENETRE PROJET___________________________________________
Projet.mainloop()





