from tkinter import *
import webbrowser


def open_graven_channel():
    webbrowser.open_new("https://youtube.com/gravenilvectuto")


window = Tk()

window.title("My Application")
window.geometry("720x480")
window.minsize(480, 360)
window.iconbitmap("logo.ico")
window.config(background='#41b77F')

frame = Frame(window, bg='#41b77F')

label_title = Label(frame, text="Bienvenue sur l'application", font=("Courrier", 40), bg='#41b77F', fg='white')
label_title.pack()

label_subtitle = Label(frame, text="Hey salut a tous c'est Antoine", font=("Courrier", 25), bg='#41b77F', fg='white')
label_subtitle.pack()

yt_button = Button(frame, text="Ouvrir Youtube", font=("Courrier", 25), bg='white', fg='#41b77F',command=open_graven_channel)
yt_button.pack(pady=25, fill=X)

frame.pack(expand=YES)
window.mainloop()
