import tkinter as tk

# Set-up the window
window = tk.Tk()
window.title("Calulatrice")

# input chiffre 1
entry = tk.Entry()
entry.pack()




#lors du click sur le button + affectue addition
def touche_1_click():

    num = 1
    entry.insert(tk.END, num)

def touche_2_click():

    num = 2
    entry.insert(tk.END, num)

def touche_3_click():

    num = 3
    entry.insert(tk.END, num)

def touche_4_click():

    num = 4
    entry.insert(tk.END, num)

def touche_5_click():

    num = 5
    entry.insert(tk.END, num)

def touche_6_click():

    num = 6
    entry.insert(tk.END, num)        

def touche_7_click():

    num = 7
    entry.insert(tk.END, num)

def touche_8_click():

    num = 8
    entry.insert(tk.END, num) 

def touche_9_click():

    num = 9
    entry.insert(tk.END, num)  

def touche_0_click():

    num = 0
    entry.insert(tk.END, num)  

#lors du click sur le button + affectue addition
def addition_click(self):

   add = '+'
   entry.insert(tk.END, add)
   entry.get()
   
    # chiffre2 = entry2.get()
    # total =  (float(chiffre1)) +  (float(chiffre2))
    # entry3 = tk.Entry(width=40, bg="white", fg="black")
    # entry3.pack()
    # entry3.insert(0, total)

    


button_add = tk.Button(
  master=window,
    text="+",
    width=1,
    height=1,
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
    command=touche_3_click 
)

touche_4 = tk.Button(
  master=window,
    text="4",
    width=3,
    height=3,
    bg="white",
    fg="black",
    command=touche_4_click 
)

touche_5 = tk.Button(
  master=window,
    text="5",
    width=3,
    height=3,
    bg="white",
    fg="black",
    command=touche_5_click 
)

touche_6 = tk.Button(
  master=window,
    text="6",
    width=3,
    height=3,
    bg="white",
    fg="black",
    command=touche_6_click 
)

touche_7 = tk.Button(
  master=window,
    text="7",
    width=3,
    height=3,
    bg="white",
    fg="black",
    command=touche_7_click 
)

touche_8 = tk.Button(
  master=window,
    text="8",
    width=3,
    height=3,
    bg="white",
    fg="black",
    command=touche_8_click 
)

touche_9 = tk.Button(
  master=window,
    text="9",
    width=3,
    height=3,
    bg="white",
    fg="black",
    command=touche_9_click 
)

touche_0 = tk.Button(
  master=window,
    text="0",
    width=3,
    height=3,
    bg="white",
    fg="black",
    command=touche_0_click 
)

B1 = tk.Button( 
  master=window, 
  text="1", 
  width=3, 
  height=2, 
  bg="grey", 
  fg="white"
) # Boutton 1

B2 = tk.Button( 
  master=window, 
  text="2", 
  width=3, 
  height=2, 
  bg="grey", 
  fg="white"
) # Boutton 1

B3 = tk.Button( 
  master=window, 
  text="3", 
  width=3, 
  height=2, 
  bg="grey", 
  fg="white"
) # Boutton 1

B4 = tk.Button( 
  master=window, 
  text="4", 
  width=3, 
  height=2, 
  bg="grey", 
  fg="white"
) # Boutton 1

B5 = tk.Button( 
  master=window, 
  text="5", 
  width=3, 
  height=2, 
  bg="grey", 
  fg="white"
) # Boutton 1

B6 = tk.Button( 
  master=window, 
  text="6", 
  width=3, 
  height=2, 
  bg="grey", 
  fg="white"
) # Boutton 1

B7 = tk.Button( 
  master=window, 
  text="7", 
  width=3, 
  height=2, 
  bg="grey", 
  fg="white"
) # Boutton 1


B1.pack(side=tk.LEFT)
B2.pack(side=tk.RIGHT)
B3.pack(side=tk.LEFT)
B4.pack(side=tk.RIGHT)
B5.pack(side=tk.LEFT)
B6.pack(side=tk.RIGHT)
B7.pack(side=tk.LEFT)




# touche_1.pack()
# touche_2.pack()
# touche_3.pack()
# touche_4.pack()
# touche_5.pack()
# touche_6.pack()
# touche_7.pack()
# touche_8.pack()
# touche_9.pack()
# touche_0.pack()
# button_add.pack()


# Run the application
window.mainloop()
