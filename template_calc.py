from tkinter import * # Tkinter

#---------
# CLASSE :
#---------

# FENETRE :
#----------
fen = Tk() # Création de a fenêtr 1e
fen.geometry("200x240") # Définition de la fenêtre
fen.title("Calculatrice v1.0") # Titre de la calculatrice
fen["bg"]= "black" # Coleur de la fenêtre
fen["relief"] = "raised" # Profondeur de la fenêtre
#------------
# PROGRAMME :

def touche_1():

    num = 1
    entry.insert(tk.END, num)

def touche_2():

    num = 2
    entry.insert(tk.END, num)

def touche_3():

    num = 3
    entry.insert(tk.END, num)

def touche_4():

    num = 4
    entry.insert(tk.END, num)

def touche_5():

    num = 5
    entry.insert(tk.END, num)

def touche_6():

    num = 6
    entry.insert(tk.END, num)        

def touche_7():

    num = 7
    entry.insert(tk.END, num)

def touche_8():

    num = 8
    entry.insert(tk.END, num) 

def touche_9():

    num = 9
    entry.insert(tk.END, num)  

def touche_0():

    num = 0
    entry.insert(tk.END, num)  





# // Ecran calculatrice //

# // Bouttons //
ECRAN = Entry(fen, width=28, bg ="white", fg="black", relief=SUNKEN, bd=5).place(x=9, y=8)


B1 = Button(fen, text="1",command=touche_1, width=3, height=2, bg="white", fg="black").place(x=10, y=40) # Boutton 1
B2 = Button(fen, text="2",command=touche_2, width=3, height=2, bg="white", fg="black").place(x=50, y=40) # Boutton 2
B3 = Button(fen, text="3",command=touche_3, width=3, height=2, bg="white", fg="black").place(x=90, y=40) # Boutton 3
B4 = Button(fen, text="4",command=touche_4, width=3, height=2, bg="white", fg="black").place(x=10, y=90) # Boutton 4
B5 = Button(fen, text="5",command=touche_5, width=3, height=2, bg="white", fg="black").place(x=50, y=90) # Boutton 5
B6 = Button(fen, text="6",command=touche_6, width=3, height=2, bg="white", fg="black").place(x=90, y=90) # Boutton 6
B7 = Button(fen, text="7",command=touche_7, width=3, height=2, bg="white", fg="black").place(x=10, y=140) # Boutton 7
B8 = Button(fen, text="8",command=touche_8, width=3, height=2, bg="white", fg="black").place(x=50, y=140) # Boutton 8
B9 = Button(fen, text="9",command=touche_9, width=3, height=2, bg="white", fg="black").place(x=90, y=140) # Boutton 9
BC = Button(fen, text="C", width=3, height=2, bg="SkyBlue2", fg="white", relief=RIDGE).place(x=10, y=190) # Boutton C (Clear)
B0 = Button(fen, text="0",command=touche_0, width=3, height=2, bg="white", fg="black").place(x=50, y=190) # Boutton 0
BF = Button(fen, text=".", width=3, height=2, bg="white", fg="black").place(x=90, y=190) # Boutton = (égale)

BP = Button(fen, text="+", width=4, height=2, bg="SkyBlue2", fg="white", relief=GROOVE).place(x=150, y=40) # Boutton + (addition)
BS = Button(fen, text="-", width=4, height=2, bg="SkyBlue2", fg="white", relief=GROOVE).place(x=150, y=80) # Boutton - (soustacrtion)
BD = Button(fen, text="/", width=4, height=2, bg="SkyBlue2", fg="white", relief=GROOVE).place(x=150, y=120) # Boutton / (division)
BM = Button(fen, text="X", width=4, height=2, bg="SkyBlue2", fg="white", relief=GROOVE).place(x=150, y=160) # Boutton X (multiplication)
BE = Button(fen, text="=", width=4, height=1, bg="red", fg="white", relief=RIDGE).place(x=150, y=205) # Button = (égale)

fen.mainloop() # Gestion de la fenêtre
