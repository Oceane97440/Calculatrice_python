import tkinter as tk

# Set-up the window
window = tk.Tk()
window.title("Calulatrice")

# input chiffre 1
entry = tk.Entry()
entry.pack()

# input chiffre 2
entry2 = tk.Entry()
entry2.pack()


#lors du click sur le button + affectue addition
def addition_click():

    chiffre1 = entry.get()
    chiffre2 = entry2.get()
    total =  (float(chiffre1)) +  (float(chiffre2))
    entry3 = tk.Entry(width=40, bg="white", fg="black")
    entry3.pack()
    entry3.insert(0, total)

    


button_add = tk.Button(
  master=window,
    text="+",
    width=5,
    height=5,
    bg="blue",
    fg="black",
    command=addition_click 
)

#lors du click sur le button + affectue soustration

def soustration_click():
#récupère le nbr1
    chiffre1 = entry.get()
    chiffre2 = entry2.get()
    total =  (float(chiffre1)) -  (float(chiffre2))
    entry3 = tk.Entry(width=40, bg="white", fg="black")
    entry3.pack()
    entry3.insert(0, total)

    


button_soustraire = tk.Button(
  master=window,
    text="-",
     width=5,
    height=5,
    bg="blue",
    fg="black",
    command=soustration_click 
)


#lors du click sur le button + affectue multiplication
def multiplication_click():
#récupère le nbr1
    chiffre1 = entry.get()
    chiffre2 = entry2.get()
    total =  (float(chiffre1)) *  (float(chiffre2))
    entry3 = tk.Entry(width=40, bg="white", fg="black")
    entry3.pack()
    entry3.insert(0, total)

    


button_multiplier = tk.Button(
  master=window,
    text="*",
    width=5,
    height=5,
    bg="blue",
    fg="black",
    command=multiplication_click 
)



#lors du click sur le button + affectue division
def division_click():
#récupère le nbr1
    chiffre1 = entry.get()
    chiffre2 = entry2.get()
    total =  (float(chiffre1)) /  (float(chiffre2))
    entry3 = tk.Entry(width=40, bg="white", fg="black")
    entry3.pack()
    entry3.insert(0, total)

    


button_diviser = tk.Button(
  master=window,
    text="/",
    width=5,
    height=5,
    bg="blue",
    fg="black",
    command=division_click 
)







button_add.pack()
button_soustraire.pack()
button_multiplier.pack()
button_diviser.pack()


# Run the application
window.mainloop()
