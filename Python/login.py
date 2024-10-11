# import librju ary from tkinter
import tkinter
from tkinter import* #* means: load everything of the library
import register_form 

# setup the window of the login screen
login_window = Tk() # root = window
login_window.title("Bitte anmelden") # window title
# login_window.geometry("800x800") # window size
login_window.state("zoomed")

# Navigation Bar (Menu)
# create a new navigaton bar and asign it to the login window
navigation = Menu(login_window)
# add the file menus
filemenu = Menu(navigation, tearoff=0)
navigation.add_cascade(label="Anmeldung", menu=filemenu)
filemenu.add_command(label="Login")
filemenu.add_command(label="Registrieren")
filemenu.add_command(label="Schließen", command=login_window.destroy)
# add a new menu btn (Contact)
# initialize a new hierarchy with Menu(xxx)
contact_navigation = Menu(navigation, tearoff=0)
navigation.add_cascade(label="Kontakt", menu=contact_navigation)
contact_navigation.add_command(label="Untermenü")
contact_navigation.add_command(label="Erster Punkt")
contact_navigation.add_command(label="zweiter Punkt")
# add a new menu btn (Help)
# inititalize a new hierarchy with Menu(xxx)
help_navigation = Menu(navigation, tearoff=0)
navigation.add_cascade(label="Hilfe", menu=help_navigation)
help_navigation.add_command(label="FAQ")
help_navigation.add_command(label="Hilfe")

# Login Architecture
# Login username and password
# Username
login_title = Label(login_window, text="Bitte Anmeldedaten eingeben:", font=("Arial", 25)) # Login Title initializing
login_title.place(relx=.5, rely=.35, anchor=CENTER) # Login Title Placement 
login_title_entry = Entry(login_window) # Entry for username
login_title_entry.place(relx=.5, rely=.4, height=40, width=340, anchor=CENTER)
# Password
password_title = Label(login_window, text="Bitte Passwort eingeben:", font=("Arial", 25)) # Password Title initializing
password_title.place(relx=.5, rely=.45, anchor=CENTER)
password_title_entry = Entry(login_window) # Entry for username
password_title_entry.place(relx=.5, rely=.5, height=40, width=340, anchor=CENTER)

# Login and register buttons
login_btn = Button(login_window, text="Anmelden", activebackground="gray", cursor="") #need to set up the commands like =user_login()
login_btn.place(relx=.4, rely=.6, width=150, height=35)
register_btn = Button(login_window, text="Registrieren", command=register_form.open_register_form_window) #need to set up the commands like =user_register()
register_btn.place(relx=0.5, rely=.6, height=35, width=150)

# title text of the website: 
# "Was hast du heute vor?"
title_label = Label(login_window, text="Was hast du heute vor?", font=("Arial", 36))
title_label.place(relx=.5, rely=0.1, anchor=CENTER)

# subtitle
# Bitte logge dich ein
subtitle_label = Label(login_window, text="Bitte logge dich ein", font=("Arial", 25))
subtitle_label.place(relx=0.5, rely=.2, anchor=CENTER)

# Window frame: initializing necessary items
login_window.config(menu=navigation) # to initialize the menubar (navigation)
login_window.mainloop() # to initialize the window frame (popup)