import tkinter as tk
from PIL import Image, ImageTk
from login_frame import login_frame

class Janela(tk.Tk):
    def __init__(self):
        super().__init__()
        self.var1 = 0
        self.title("God's Interface")
        self.geometry("300x500")
        # Carregando a imagem
        icon = Image.open("X-Foda-02.ico")
        icon_photo = ImageTk.PhotoImage(icon)
        # Definindo o ícone da janela
        self.iconphoto(False, icon_photo)

        self.inicial = login_frame()
        self.inicial.pack(expand=True)
        self.mainloop()

