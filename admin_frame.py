import tkinter as tk
from PIL import Image, ImageTk
from ttkbootstrap import OUTLINE, DARK, Entry, Button, Label, LabelFrame,OptionMenu,PRIMARY,DANGER
import mysql.connector
import login_frame


class admin_frame(tk.Frame):
    # Lock Portrait Trash User Envelope
    def __init__(self):
        super().__init__()
        # Frame de Administração
        self.pack(fill='both', expand=True)
        # Carregando a imagem
        adm_image = Image.open("X-Foda-02.ico")
        lock_image = Image.open("lock.png")
        portrait_image = Image.open("portrait.png")
        trash_image = Image.open("trash.png")
        user_image = Image.open("user.png")
        envelope_image = Image.open("envelope.png")
        zoom_image = Image.open("zoom-in.png")
        cloud_image = Image.open("cloud-upload-alt.png")
        # Redimensionando a imagem
        adm_image = adm_image.resize((100, 100), Image.ANTIALIAS)
        lock_image = lock_image.resize((20, 20),Image.ANTIALIAS)
        portrait_image = portrait_image.resize((20, 20),Image.ANTIALIAS)
        trash_image = trash_image.resize((20, 20),Image.ANTIALIAS)
        user_image = user_image.resize((20, 20),Image.ANTIALIAS)
        envelope_image = envelope_image.resize((20, 20),Image.ANTIALIAS)
        zoom_image = zoom_image.resize((20, 20),Image.ANTIALIAS)
        cloud_image = cloud_image.resize((20, 20),Image.ANTIALIAS)
        # Transformando em uma PhotoImage
        self.adm_photo = ImageTk.PhotoImage(adm_image)
        self.portrait_photo = ImageTk.PhotoImage(portrait_image)
        self.lock_photo = ImageTk.PhotoImage(lock_image)
        self.user_photo = ImageTk.PhotoImage(user_image)
        self.trash_photo = ImageTk.PhotoImage(trash_image)
        self.envelope_photo = ImageTk.PhotoImage(envelope_image)
        self.zoom_photo = ImageTk.PhotoImage(zoom_image)
        self.cloud_photo = ImageTk.PhotoImage(cloud_image)
        # Criando o Label com a imagem
        self.label = Label(self, image=self.adm_photo)


        # Posicionando o Label na janela
        self.label.place(relx=0.5, rely=0.10, anchor='center')
        self.Frame = LabelFrame()
        self.Frame.place(height=325,width=300,rely=0.55,relx=0.5,anchor='center')

        # Entry da busca de registro no servidor
        self.busca_entry = Entry(self.Frame, width=30, style=DARK)
        self.busca_entry.place(relx=0.4, rely=0.13, anchor='center')
        self.busca_entry.insert(0, 'Email para busca de registro')
        self.busca_entry.configure(foreground='gray')
        self.busca_entry.bind('<FocusIn>', self.busca_entry_focus)
        self.busca_entry.bind('<FocusOut>', self.busca_entry_focus)

        # Botão de Deletar
        self.del_button = tk.Button(self.Frame, text='Deletar',image=self.trash_photo,command=self.delete)
        self.del_button.configure(background='white',foreground='white',activebackground='white')
        self.del_button.place(relx=0.9, rely=0.13, anchor='w',width=30,height=33)

        # Botão de Buscar
        self.back_button = tk.Button(self.Frame, text="Buscar", command=self.busca, width=8,image=self.zoom_photo)
        self.back_button.configure(background='white', foreground='white', activebackground='white')
        self.back_button.place(relx=0.76, rely=0.13, anchor='w', width=40, height=33)

        # Label do Retrato
        self.portrait_label = Label(self.Frame,image=self.portrait_photo)
        self.portrait_label.image = self.portrait_photo
        self.portrait_label.place(relx=0.15,rely=0.25,anchor='e')
        self.portrait_text = Label(self.Frame,text=': Nome',font='Tahoma 10 bold')
        self.portrait_text.place(relx=0.15,rely=0.25,anchor='w')

        # Label da Email
        self.envelop_label = Label(self.Frame,image=self.envelope_photo)
        self.envelop_label.image = self.envelope_photo
        self.envelop_label.place(relx=0.15, rely=0.36, anchor='e')
        self.envelop_text = Label(self.Frame,text=': Email',font='Tahoma 10 bold')
        self.envelop_text.place(relx=0.15, rely=0.36, anchor='w')

        # Label da Usuário
        self.user_label = Label(self.Frame,image=self.user_photo)
        self.user_label.image = self.user_photo
        self.user_label.place(relx=0.15, rely=0.47, anchor='e')
        self.user_text = Label(self.Frame,text=': User',font='Tahoma 10 bold')
        self.user_text.place(relx=0.15, rely=0.47, anchor='w')

        # Label da Senha
        self.lock_label = Label(self.Frame,image=self.lock_photo)
        self.lock_label.image = self.lock_photo
        self.lock_label.place(relx=0.15, rely=0.581, anchor='e')
        self.lock_text = Label(self.Frame,text=': Senha',font='Tahoma 10 bold')
        self.lock_text.place(relx=0.15, rely=0.581, anchor='w')

        # Option Menu
        self.var = tk.StringVar(self)
        opcoes = ['',"Email", "Nome", "User", "Senha"] # Opções
        self.var.set(opcoes[1])  # valor inicial
        self.menu = OptionMenu(self.Frame, self.var, *opcoes, style=(OUTLINE, PRIMARY))
        self.menu.place(relx=0.21, rely=0.75, anchor='center',width=90)

        # Botão de Voltar
        self.find_button = Button(self, text="Voltar", style=(OUTLINE, DARK), width=8,command=self.log_frame)
        self.find_button.place(relx=0.5, rely=0.935, anchor='center')

        # Entry da busca de registro no servidor
        self.change_entry = Entry(self.Frame, width=35, style=PRIMARY)
        self.change_entry.place(relx=0.06, rely=0.86, anchor='w')
        self.change_entry.insert(0, f'Primeiramente procure um registro!')
        self.change_entry.config(foreground='gray')
        self.change_entry.bind('<FocusIn>', self.change_entry_focus)
        self.change_entry.bind('<FocusOut>', self.change_entry_focus)

        # Botão de Alterar
        self.change_button = tk.Button(self.Frame, text='Alt',command=self.alterar_reg,image=self.cloud_photo)
        self.change_button.configure(background='white',foreground='white',activebackground='white')
        self.change_button.place(relx=0.85, rely=0.86,anchor='w',width=30,height=33)

        # Label de avisos
        self.msg_label = Label(self.Frame, text='')
        self.msg_label.place(relx=0.5, rely=0.95,anchor='center')



    def log_frame(self):
        self.destroy()
        login_frame.login_frame()


    def busca_entry_focus(self, event):
        if self.busca_entry.get() == 'Email para busca de registro':
            self.busca_entry.delete(0, 'end')
            self.busca_entry.config(foreground='black')
        else:
            if self.busca_entry.get() == '':
                self.busca_entry.insert(0, 'Email para busca de registro')
                self.busca_entry.config(foreground='gray')


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
            resultado = cursor.fetchone()
            conexao.close()

            return resultado


    def busca(self):
        email = self.busca_entry.get()
        dados = self.servidor_sql(f"SELECT nome,email,user,senha FROM registros Where email = '{email}'")
        try:
            self.portrait_text['text'] = f": {dados[0]}"
            self.envelop_text['text'] = f": {dados[1]}"
            self.user_text['text'] = f": {dados[2]}"
            self.lock_text['text'] = f": {dados[3]}"
        except TypeError:
            pass

    def delete(self):
        email = self.busca_entry.get()
        if email != 'Email para busca de registro' and email != '':
            self.servidor_sql(f"DELETE FROM registros WHERE email = '{email}'")
            self.portrait_text['text'] = f": DELETADO!"
            self.portrait_text.configure(foreground="#d9534f")
            self.envelop_text['text'] = f": DELETADO!"
            self.envelop_text.configure(foreground="#d9534f")
            self.user_text['text'] = f": DELETADO!"
            self.user_text.configure(foreground="#d9534f")
            self.lock_text['text'] = f": DELETADO!"
            self.lock_text.configure(foreground="#d9534f")
        else:
            self.busca_entry.config(foreground='#d9534f')

    def alterar_reg(self):
        option = self.var.get().lower()
        answer = self.change_entry.get()
        target = self.busca_entry.get()
        try:
            if answer == 'Primeiramente procure um registro!' or target == 'Email para busca de registro':
                self.change_entry.config(foreground='#ff5252')
            else:
                resultado = self.servidor_sql(f"SELECT email,user FROM registros WHERE email = '{answer}'")
                if answer != target and resultado is None and answer != '':
                    self.servidor_sql(f"UPDATE registros SET {option} = '{answer}' WHERE email = '{target}'")
                else:
                    self.msg_label['text'] = f'{option} já existente!'
        except:
            self.msg_label['text'] = f'Nome de Usuario já existente!'


    def change_entry_focus(self,event):
        if self.change_entry.get() == 'Primeiramente procure um registro!':
            self.change_entry.delete(0, 'end')
            self.change_entry.config(foreground='black')
        else:
            if self.change_entry.get() == '':
                self.change_entry.insert(0, 'Primeiramente procure um registro!')
                self.change_entry.config(foreground='gray')






 # (43, 'PauloVGDS', 'Paulo Vinicius Gomes da Silva', 'lordkingvini1732@gmail.com', 'lordkingvini1732')