from PIL import Image, ImageTk
from ttkbootstrap import OUTLINE, Entry, Button, PRIMARY, Frame, Label
import login_frame
import tkinter as tk
import mysql.connector


class registro_frame(tk.Frame):

    def __init__(self):
        super().__init__()
        # Frame de Login
        self.pack(fill='both', expand=True)

        # Carregando a imagem
        reg_image = Image.open("VavaB.ico")
        # Redimensionando a imagem
        reg_image = reg_image.resize((100, 100), Image.ANTIALIAS)
        # Transformando em uma PhotoImage
        reg_photo = ImageTk.PhotoImage(reg_image)

        # Criando o Label com a imagem
        self.label = tk.Label(self, image=reg_photo)
        self.label.image = reg_photo

        # Posicionando o Label na janela
        self.label.place(relx=0.5, rely=0.10, anchor='center')

        # Entry do Nome
        self.__nome_entry = Entry(self, width=30, style=PRIMARY)
        self.__nome_entry.place(relx=0.5, rely=0.25, anchor='center')
        self.__nome_entry.insert(0, 'Nome Completo')
        self.__nome_entry.configure(foreground='gray')
        self.__nome_entry.bind('<FocusIn>', self.nome_entry_focus)
        self.__nome_entry.bind('<FocusOut>', self.nome_entry_focus)

        # Entry do Usuario
        self.__user_entry = Entry(self, width=30, style=PRIMARY)
        self.__user_entry.place(relx=0.5, rely=0.35, anchor='center')
        self.__user_entry.insert(0, 'Usuario')
        self.__user_entry.configure(foreground='gray')
        self.__user_entry.bind('<FocusIn>', self.user_entry_focus)
        self.__user_entry.bind('<FocusOut>', self.user_entry_focus)

        # Entry do Email
        self.__email_entry = Entry(self, width=30, style=PRIMARY)
        self.__email_entry.place(relx=0.5, rely=0.45, anchor='center')
        self.__email_entry.insert(0, 'Email')
        self.__email_entry.configure(foreground='gray')
        self.__email_entry.bind('<FocusIn>', self.email_entry_focus)
        self.__email_entry.bind('<FocusOut>', self.email_entry_focus)

        # Botão de Esqueceu a Senha
        self.forget_button = tk.Button(self, text="Confirmar Email", width=15)
        self.forget_button.configure(background='white', foreground='#578eed', activebackground='#578eed',activeforeground='white', command=self.forget_senha)
        self.forget_button.place(relx=0.65, rely=0.502, anchor='center')

        # Entry da Senha
        self.__senha_entry = Entry(self, width=30, style=PRIMARY)
        self.__senha_entry.place(relx=0.5, rely=0.55, anchor='center')
        self.__senha_entry.insert(0, 'Senha')
        self.__senha_entry.configure(foreground='gray')
        self.__senha_entry.bind('<FocusIn>', self.senha_entry_focus)
        self.__senha_entry.bind('<FocusOut>', self.senha_entry_focus)

        # Entry da Confirmação da Senha
        self.__confirma_senha_entry = Entry(self, width=30, style=PRIMARY)
        self.__confirma_senha_entry.place(relx=0.5, rely=0.65, anchor='center')
        self.__confirma_senha_entry.insert(0, 'Confirme sua Senha')
        self.__confirma_senha_entry.configure(foreground='gray')
        self.__confirma_senha_entry.bind('<FocusIn>', self.confirm_senha_entry_focus)
        self.__confirma_senha_entry.bind('<FocusOut>', self.confirm_senha_entry_focus)

        # Frame das Mensagens
        self.msg_frame = Frame(self)
        self.msg_frame.place(relx=0.5, rely=0.80, anchor='center')
        self.msg_frame.configure(height=100, width=300)
        self.msg = Label(self.msg_frame, text='Bem Vindo!', foreground='#578eed', font='Arial 10 bold')
        self.msg.place(relx=0.5, rely=0.5, anchor='center')

        # Botão de Voltar
        self.back_button = Button(self, text="Voltar", command=self.log_frame, style=(OUTLINE, PRIMARY), width=8)
        self.back_button.place(relx=0.7, rely=0.95, anchor='center')

        # Botão de Registrar
        self.back_button = Button(self, text="Registrar", style=(OUTLINE, PRIMARY), width=8, command=self.msgs)
        self.back_button.place(relx=0.3, rely=0.95, anchor='center')

    def log_frame(self):
        self.destroy()
        login_frame.login_frame()

    def nome_entry_focus(self, event):
        if self.__nome_entry.get() == 'Nome Completo':
            self.__nome_entry.delete(0, 'end')
            self.__nome_entry.config(foreground='black')
        else:
            if self.__nome_entry.get() == '':
                self.__nome_entry.insert(0, 'Nome Completo')
                self.__nome_entry.config(foreground='gray')

    @property
    def __nome(self):
        return self.__nome_entry

    def user_entry_focus(self, event):
        if self.__user_entry.get() == 'Usuario':
            self.__user_entry.delete(0, 'end')
            self.__user_entry.config(foreground='black')
        else:
            if self.__user_entry.get() == '':
                self.__user_entry.insert(0, 'Usuario')
                self.__user_entry.config(foreground='gray')

    @property
    def __user(self):
        return self.__user_entry

    def email_entry_focus(self, event):
        if self.__email_entry.get() == 'Email':
            self.__email_entry.delete(0, 'end')
            self.__email_entry.config(foreground='black')
        else:
            if self.__email_entry.get() == '':
                self.__email_entry.insert(0, 'Email')
                self.__email_entry.config(foreground='gray')

    @property
    def __email(self):
        return self.__email_entry

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

    def confirm_senha_entry_focus(self, event):
        if self.__confirma_senha_entry.get() == 'Confirme sua Senha':
            self.__confirma_senha_entry.delete(0, 'end')
            self.__confirma_senha_entry.config(foreground='black')
        else:
            if self.__confirma_senha_entry.get() == '':
                self.__confirma_senha_entry.insert(0, 'Confirme sua Senha')
                self.__confirma_senha_entry.config(foreground='gray')

    @property
    def __confirm_senha(self):
        return self.__confirma_senha_entry

    def msgs(self):
        nome = self.__nome.get()
        user = self.__user.get()
        email = self.__email.get()
        senha = self.__senha.get()
        confirma_senha = self.__confirm_senha.get()
        if (nome == 'Nome Completo' or len(nome) < 3) or (user == 'Usuario' or len(user) < 3) or (email == 'Email' or '@gmail.com' not in email):
            self.msg['text'] = 'Preencha todos os campos corretamente!'
        else:
            if senha != confirma_senha or len(confirma_senha) < 4:
                self.msg['text'] = 'As senhas não conferem!'
            else:
                resultado = self.servidor_sql(f"SELECT email FROM registros WHERE email = '{email}'")
                if resultado is not None:
                    self.msg['text'] = 'Esse email já foi usado!'
                else:
                    resultado = self.servidor_sql(f"SELECT user FROM registros WHERE user = '{user}'")
                    if resultado is not None:
                        self.msg['text'] = 'Esse nome de usuário já foi usado!'
                    else:
                        self.servidor_sql(f"INSERT INTO registros (nome,user,email,senha) VALUES ('{nome}', '{user}', '{email}', '{senha}')")
                        self.msg['text'] = 'Registrado com sucesso!'

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

    def forget_senha(self):
        self.msg['text'] = "Sinto muito, mas, no momento o\nesse serviço não está disponível!"
