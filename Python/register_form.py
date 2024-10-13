# import librju ary from tkinter
import tkinter
from tkinter import* #* means: load everything of the library

# function to open a popUp window for the register form
def open_register_form_window():
    global user_registration
    global register_window
    global error_messages
    global error_messages_display
    global email_entry
    global password_entry
    global password_confirm_entry
    global register_btn
    global close_btn

    
    register_window = Tk()
    register_window.title("Kostenlos registrieren")
    register_window.geometry("600x600")
    register_window.eval("tk::PlaceWindow . center")

    title = Label(register_window, text="Melde dich kostenlos an!", font=("Arial", 25))
    title.place(relx=0.5, rely=0.05, anchor=CENTER)

    def user_registration():

            if email_entry.get() == "":
                error_messages_display.config(text=error_messages[0])
            elif password_entry.get() == "":
                error_messages_display.config(text=error_messages[2])
            elif password_confirm_entry.get() == "":
                error_messages_display.config(text=error_messages[5])
            else:
                print("valid thing")


    # EMail label and entry
    email_label = Label(register_window, text="Bitte Email angeben:", font=("Arial", 18))
    email_label.place(relx=.5, rely=.15, height=40, width=340, anchor=CENTER)
    email_entry = Entry(register_window)
    email_entry.place(relx=.5, rely=.22, height=40, width=340, anchor=CENTER)

    # Password label and entry
    password_lable = Label(register_window, text="Bitte gib ein Password ein:", font=("Arial", 18))
    password_lable.place(relx=.5, rely=.3, height=40, width=340, anchor=CENTER)
    password_entry = Entry(register_window)
    password_entry.place(relx=.5, rely=.37, height=40, width=340, anchor=CENTER)

    # Password conformation label and entry
    password_confirm_label = Label(register_window, text="Passwort wiederholen:", font=("Arial", 18))
    password_confirm_label.place(relx=.5, rely=.46, height=40, width=340, anchor=CENTER)
    password_confirm_entry = Entry(register_window)
    password_confirm_entry.place(relx=.5, rely=.53, height=40, width=340, anchor=CENTER)
    
    # Login and register buttons
    register_btn = Button(register_window, text="Registrieren", activebackground="gray", cursor="", command=user_registration) #need to set up the commands like =user_registration()
    register_btn.place(relx=.4, rely=.72, height=35, width=100, anchor=CENTER)
    close_btn = Button(register_window, text="Schließen", command=register_window.destroy) #need to set up the commands like =user_register()
    close_btn.place(relx=0.6, rely=.72, height=35, width=100, anchor=CENTER)


    # Error messages
    error_messages = [
        "Bitte E-Mail Adresse eingeben! \n"            #0
        "E-Mail darf nicht leer sein \n"               #1
        "Bitte Password eingeben! \n"                  #2
        "Bitte Password wiederholen \n"                #3
        "Password darf nicht leer sein \n"             #4
        "Bitte Password wiederholen \n"                #5
        "Passwort wiederholen darf nicht leer sein \n" #6
        "Felder dürfen nicht leer sein \n"             #7
    ]


    error_messages_display = Label(register_window, text=user_registration, font=("Arial", 16))
    error_messages_display.place(relx=0.5, rely=.64, anchor=CENTER)

    
