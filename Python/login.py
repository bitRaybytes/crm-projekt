# import library from tkinter
import tkinter
from tkinter import* # * means: load everything of the library
import register_form 

# setup the window of the login screen
login_window = Tk() # root = window
login_window.title("Bitte anmelden") # window title
# login_window.geometry("800x800") # window size
login_window.state("zoomed")


class user_login_frame():
    global user_login
    def user_login():
        username = "Ray"
        password = "12345"
        user_pw = password
    
        global dashboard_frame
        global dashboard_frame_label
    
        if login_email_entry.get() == "":
            login_error_label.config(text=login_error_msgs[1])
        elif password_title_entry.get() == "":
            login_error_label.config(text=login_error_msgs[2])
        elif login_email_entry.get() == "" or password_title_entry.get() == "":
            login_error_label.config(text=login_error_msgs[0])
        else: # initialize a frame for the dashboard with sidebar
            dashboard_frame = Frame(login_window)
            dashboard_frame.grid(row=0, column=0)
            dashboard_frame_label = Label(dashboard_frame, text="Lable test")
            dashboard_frame_label.grid(row=5, column=0)
            
   



login_error_msgs = [
    "Bitte E-Mail und Password eingeben.",
    "Bitte E-Mail eingeben",
    "Bitte Password eingeben"
]
login_error_label = Label(login_window, text=user_login, font=("Arial", 16))
login_error_label.place(relx=0.5, rely=0.55, anchor=CENTER)

# Navigation Bar (Menu)
# create a new navigaton bar and asign it to the login window
navigation = Menu(login_window) # navigaton is the name of the whole menubar
# add the file menus
filemenu = Menu(navigation, tearoff=0)
navigation.add_cascade(label="Anmeldung", menu=filemenu) # Adds a cascading element onto the menubar
filemenu.add_command(label="Login") # commands for submenu structure
filemenu.add_command(label="Registrieren") 
filemenu.add_command(label="Schließen", command=login_window.destroy)
# add a new menu btn (Contact)
# initialize a new hierarchy with Menu(xxx)
contact_navigation = Menu(navigation, tearoff=0) # a new cascading hierarchy for a new menu element
navigation.add_cascade(label="Kontakt", menu=contact_navigation) # adds the element onto the menubar
contact_navigation.add_command(label="Untermenü") # commands for submenu structure
contact_navigation.add_command(label="Erster Punkt")
contact_navigation.add_command(label="zweiter Punkt")
# add a new menu btn (Help)
# inititalize a new hierarchy with Menu(xxx)
help_navigation = Menu(navigation, tearoff=0) # a new cascading hierarchy for a new menu element
navigation.add_cascade(label="Hilfe", menu=help_navigation) # adds the element onto the menubar
help_navigation.add_command(label="FAQ") # commands for submenu structure
help_navigation.add_command(label="Hilfe")

# Login Architecture
# Login username and password
# Username
login_email = Label(login_window, text="Bitte Anmeldedaten eingeben:", font=("Arial", 25)) # Login Title initializing
login_email.place(relx=.5, rely=.35, anchor=CENTER) # Login Title Placement 
login_email_entry = Entry(login_window) # Entry for username
login_email_entry.place(relx=.5, rely=.4, height=40, width=340, anchor=CENTER)
# Password
password_title = Label(login_window, text="Bitte Passwort eingeben:", font=("Arial", 25)) # Password Title initializing
password_title.place(relx=.5, rely=.45, anchor=CENTER)
password_title_entry = Entry(login_window, show="*") # Entry for username
password_title_entry.place(relx=.5, rely=.5, height=40, width=340, anchor=CENTER)

# Login and register buttons
login_btn = Button(login_window, text="Anmelden", activebackground="gray", cursor="", command= user_login) #need to set up the commands like =user_login()
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