import tkinter as tk

# Set-up the window
window = tk.Tk()
window.title("Calulatrice")

# input opération
entry = tk.Entry()
entry.pack()



def touche_1_click():
    entry.insert(0, '1')
def touche_2_click():
    entry.insert(0, '2')

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
    width=3,
    height=2,
    bg="blue",
    fg="white",
    command=addition_click 
)


touche_1 = tk.Button(
  master=window,
    text="1",
    width=3,
    height=3,
    bg="white",
    fg="black",
    command=touche_1_click 
)

touche_2 = tk.Button(
  master=window,
    text="2",
    width=3,
    height=3,
    bg="white",
    fg="black",
    command=touche_2_click 
)

touche_3 = tk.Button(
  master=window,
    text="3",
    width=3,
    height=3,
    bg="white",
    fg="black",
    command=division_click 
)

touche_4 = tk.Button(
  master=window,
    text="4",
    width=3,
    height=3,
    bg="white",
    fg="black",
    command=division_click 
)

touche_5 = tk.Button(
  master=window,
    text="5",
    width=3,
    height=3,
    bg="white",
    fg="black",
    command=division_click 
)

touche_6 = tk.Button(
  master=window,
    text="6",
    width=3,
    height=3,
    bg="white",
    fg="black",
    command=division_click 
)

touche_7 = tk.Button(
  master=window,
    text="7",
    width=3,
    height=3,
    bg="white",
    fg="black",
    command=division_click 
)

touche_8 = tk.Button(
  master=window,
    text="8",
    width=3,
    height=3,
    bg="white",
    fg="black",
    command=division_click 
)

touche_9 = tk.Button(
  master=window,
    text="9",
    width=3,
    height=3,
    bg="white",
    fg="black",
    command=division_click 
)

touche_1.pack()
touche_2.pack()
touche_3.pack()
touche_4.pack()
touche_5.pack()
touche_6.pack()
touche_7.pack()
touche_8.pack()
touche_9.pack()
