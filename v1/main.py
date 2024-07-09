#--------------------------
# Dépendance

from tkinter import *
import emoji

#-------------------------

#-------------------------
#inforamtion sur la page
root = Tk()
root.geometry("300x400")
root.title(" convertisseur de masse ")
#-------------------------

#--------------------------------------------------------------------------
# definition des variables

        
#----------------------------------------
# Clear les espaces de texte
def clear():
    Output.delete("1.0", "end-1c")
    inputtxt.delete("1.0", "end-1c")
#---------------------------------------

#---------------------------------------
# Défénition de variable pour la 
# conversion entre C to F & F to C & C to K & K to C & F to K & K to F

def C_to_F():
    INPUT = inputtxt.get("1.0", "end-1c")
    Output.delete("1.0", "end-1c")
    try:
        C = float(INPUT)
        F = round((C * 9/5) + 32, 2)
        Output.insert(END, f"Le degrée de température est de {F} ° Fahrenheit\n")
    except ValueError:
        Output.insert(END, emoji.emojize("oups une erreur est survenue\n 🙃"))

def F_to_C():
    INPUT = inputtxt.get("1.0", "end-1c")
    Output.delete("1.0", "end-1c")
    try:
        F = float(INPUT)
        C = round((F - 32) * 5/9, 2)
        Output.insert(END, f"Le degrée de température est de {C} ° Celsuis\n")
    except ValueError:
        Output.insert(END, emoji.emojize("oups une erreur est survenue\n 🙃"))
def C_to_K():
    INPUT = inputtxt.get("1.0", "end-1c")
    Output.delete("1.0", "end-1c")
    try:
        C = float(INPUT)
        K = round(C + 273.15, 2)
        Output.insert(END, f"Le degrée de température est de {K} ° Kelvin\n")
    except ValueError:
        Output.insert(END, emoji.emojize("oups une erreur est survenue\n 🙃"))

def K_to_C():
    INPUT = inputtxt.get("1.0", "end-1c")
    Output.delete("1.0", "end-1c")
    try:
        K = float(INPUT)
        C = round(K - 273.15, 2)
        Output.insert(END, f"Le degrée de température est de {C} ° Celsius\n")
    except ValueError:
        Output.insert(END, emoji.emojize("oups une erreur est survenue\n 🙃"))
def F_to_K():
    INPUT = inputtxt.get("1.0", "end-1c")
    Output.delete("1.0", "end-1c")
    try:
        F = float(INPUT)

        K = float(round((F - 32) * 5/9 + 273.15, 2))
        Output.insert(END, f"Le degrée de température est de {K} ° Kelvin\n")
    except ValueError:
        Output.insert(END, emoji.emojize("oups une erreur est survenue\n 🙃"))

def K_to_F():
    INPUT = inputtxt.get("1.0", "end-1c")
    Output.delete("1.0", "end-1c")
    try:
        K = float(INPUT)
        F = float(round((K - 273.15) * 9/5 + 32, 2))
        Output.insert(END, f"Le degrée de température est de {F} ° Celsius\n")
    except ValueError:
        Output.insert(END, emoji.emojize("oups une erreur est survenue\n 🙃"))


#--------------------------------------
#Deffinition variable exit
def exit():
    root.destroy()
#-------------------------------------

#--------------------------------------------------------------------------

#-------------------------------------
# Propriété de la page

l = Label(text = "Quelle est le degrée de température",).grid(row=0, column=1, columnspan=2)

inputtxt = Text(root, height=2,
                width = 30,
                bg = "light yellow",)

inputtxt.grid(row=2, column=1, columnspan=2)

 
c_to_f = Button(root, height = 2,
                 width = 20, 
                 text ="Celsius à fahrenheit",
                 command = lambda:C_to_F()).grid(row=3, column=1)
f_to_c = Button(root, height = 2,
                 width = 20, 
                 text ="Fahrenheit à Celsius",
                 command = lambda:F_to_C()).grid(row=3, column=2)
c_to_k = Button(root, height = 2,
                 width = 20, 
                 text ="Celsius à Kelvin",
                 command = lambda:C_to_K()).grid(row=4, column=1)
k_to_c = Button(root, height = 2,
                 width = 20, 
                 text ="Kelvin à Celsius",
                 command = lambda:K_to_C()).grid(row=4, column=2)
k_to_f = Button(root, height = 2,
                 width = 20, 
                 text ="Kelvin à fahrenheit",
                 command = lambda:K_to_F()).grid(row=5, column=1)
f_to_k = Button(root, height = 2,
                 width = 20, 
                 text ="Fahrenheit à Kelvin",
                 command = lambda:F_to_K()).grid(row=5, column=2)

Output = Text(root,height=10,
                width = 30, 
              bg = "light cyan")
Output.grid(row=6, column=1, columnspan=2)

Clear = Button(root, height = 2,
                 width = 20, 
                 text ="Clear",
                 command = lambda:clear()).grid(row=7, column=1)

exit_button = Button(root, height = 2,
                 width = 20,  text="Exit", command=root.destroy).grid(row=7, column=2)


root.bind("<Escape>", lambda event:exit()) # Touche sur le clavier pour faire l'application

# Suite des éléments sur la page
#l.pack() # titre
#inputtxt.pack() # entrée de la donner
#c_to_f.pack(pady=20) # La type de conversion
#f_to_c.pack(pady=20) # La type de conversion
#Output.pack()  # sortie de la donnée
#Clear.pack() # Vide les zone de donnée
#exit_button.pack(pady=20) # boutton pour la sortie

mainloop()