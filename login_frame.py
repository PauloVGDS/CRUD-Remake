import tkinter as tk
from PIL import Image, ImageTk
from ttkbootstrap import TOP, OUTLINE, DANGER, Frame, Entry, Button, Label, IntVar
from registro_frame import registro_frame
import mysql.connector
from admin_frame import admin_frame


class login_frame(tk.Frame):
    var1 = IntVar

    def __init__(self):
        super().__init__()
        # Frame de Login
        self.pack(fill='both', expand=True)
        # Carregando a imagem
        log_image = Image.open("valorant.png")
        checkon = Image.open("eye.png")
        checkoff = Image.open("eye-crossed.png")
        # Redimensionando a imagem
        log_image = log_image.resize((100, 100), Image.ANTIALIAS)
        checkon = checkon.resize((20, 20), Image.ANTIALIAS)
        checkoff = checkoff.resize((20, 20), Image.ANTIALIAS)
        # Transformando em uma PhotoImage
        log_photo = ImageTk.PhotoImage(log_image)
        self.checkon = ImageTk.PhotoImage(checkon)
        self.checkoff = ImageTk.PhotoImage(checkoff)

        # Criando o Label com a imagem
        self.label = Label(self, image=log_photo)
        self.label.image = log_photo

        # Posicionando o Label na janela
        self.label.pack(side=TOP, ipady=30)

        # Entry do Login
        self.__login_entry = Entry(self, width=30, style=DANGER)
        self.__login_entry.place(relx=0.5, rely=0.4, anchor='center', height=32)
        self.__login_entry.insert(0, 'Login')
        self.__login_entry.configure(foreground='gray')
        self.__login_entry.bind('<FocusIn>', self.login_entry_focus)
        self.__login_entry.bind('<FocusOut>', self.login_entry_focus)

        # Entry do Senha
        self.__senha_entry = Entry(self, width=30, style=DANGER)
        self.__senha_entry.place(relx=0.5, rely=0.50, anchor='center', height=32)
        self.__senha_entry.insert(0, 'Senha')
        self.__senha_entry.configure(foreground='gray')
        self.__senha_entry.bind('<FocusIn>', self.senha_entry_focus)
        self.__senha_entry.bind('<FocusOut>', self.senha_entry_focus)

        # Botão de Esqueceu a Senha
        self.forget_button = tk.Button(self, text="Esqueceu a senha?", width=15)
        self.forget_button.configure(background='white', foreground='#d9534f', activebackground='#d9534f',
                                     activeforeground='white', command=self.forget_senha)
        self.forget_button.place(relx=0.16, rely=0.55)

        # 'CheckButton'
        self.button_state = False
        self.check_button = tk.Button(self,command=self.show_senha,image=self.checkon)
        self.check_button.configure(background='white', activebackground='white')
        self.check_button.place(relx=0.85, rely=0.48)

        # Frame das Mensagens
        self.msg_frame = Frame(self)
        self.msg_frame.place(relx=0.5, rely=0.75, anchor='center')
        self.msg_frame.configure(height=100, width=300)
        self.msg = Label(self.msg_frame, text='          Bem Vindo!\nNão uma possui conta?\n        Registre-se já!', foreground='#d9534f',
                         font='Arial 10 bold')
        self.msg.place(relx=0.5, rely=0.5, anchor='center')

        # Frame do Botão
        self.button_frame = Frame(self)
        self.button_frame.place(relx=0, rely=0.875)
        self.button_frame.configure(height=50, width=300)

        # Botão Login
        self.login_button = Button(self.button_frame, text='Logar', style=(OUTLINE, DANGER), command=self.msgs, width=9)
        self.login_button.place(relx=0.3, rely=0.5, anchor='center')

        # Botão de Registro
        self.register_button = Button(self.button_frame, text='Registrar', style=(OUTLINE, DANGER),
                                      command=self.reg_frame, width=9)
        self.register_button.place(relx=0.7, rely=0.5, anchor='center')

    def login_entry_focus(self, event):
        if self.__login_entry.get() == 'Login':
            self.__login_entry.delete(0, 'end')
            self.__login_entry.config(foreground='black')
        else:
            if self.__login_entry.get() == '':
                self.__login_entry.insert(0, 'Login')
                self.__login_entry.config(foreground='gray')

    @property
    def __login(self):
        return self.__login_entry

    def senha_entry_focus(self, event):
        if self.__senha_entry.get() == 'Senha':
            self.__senha_entry.delete(0, 'end')
            self.__senha_entry.config(foreground='black')
        else:
            if self.__senha_entry.get() == '':
                self.__senha_entry.insert(0, 'Senha')
                self.__senha_entry.config(foreground='gray')

    @property
    def __senha(self):
        return self.__senha_entry

    def show_senha(self):
        global checkon,checkoff
        if self.var1 == 1:
            self.check_button.config(image=self.checkon,background='white',activebackground='white')
            self.__senha_entry['show'] = ''
            self.var1 = 0
        else:
            self.check_button.config(image=self.checkoff,background='white',activebackground='white')
            self.__senha_entry['show'] = '*'
            self.var1 = 1

    def reg_frame(self):
        self.destroy()
        registro_frame()

    def adm_frame(self):
        self.destroy()
        admin_frame()

    def info(self):
        print(f"Login: {self.__login_entry.get()}\nSenha: {self.__senha_entry.get()}")

    def msgs(self):
        login = self.__login.get()
        senha = self.__senha.get()
        if login == 'admin' and senha == 'Senha':
            self.adm_frame()
        else:
            if login == 'Login' and senha == 'Senha':
                self.msg['text'] = 'Preencha todos os campos!'

            else:
                resultado = self.servidor_sql(f"SELECT email,senha FROM registros WHERE email = '{login}' and senha = '{senha}'")
                print(resultado)
                if resultado is not None:
                    self.msg['text'] = 'Logado com sucesso!'
                else:
                    self.msg['text'] = '    Usuário e/ou senha incorretos!\nCaso não tenha conta, registre-se!'

    def forget_senha(self):
        self.msg['text'] = "Sinto muito, mas, no momento o\nesse serviço não está disponível!"

    @staticmethod
    def servidor_sql(comando):
        # Conecta ao servidor MySQL
        conexao = mysql.connector.connect(
            host="localhost",
            user="interface_login",
            password="!issFBeSC(4M8e*_",
            database="programa"
        )
        # Cria um cursor para executar as consultas SQL
        cursor = conexao.cursor()
        # Executa a consulta SQL
        cursor.execute(f"{comando}")

        # Armazena o resultado da consulta em uma variável
        if 'SELECT' in comando:
            resultado = cursor.fetchone()
            return resultado
        conexao.close()
