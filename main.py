import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk


root = Tk()

def connection(host, user, password):
    global db_connection
    try:
        db_connection = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            database = "BD_Exoplanetas"
        )
        messagebox.showinfo("Success", "Connection to database established successfully!")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")


def close_connection():
    if db_connection.is_connected():
        db_connection.close()
        messagebox.showinfo("Success", "Connection to database closed successfully!")

class App():
    #Construtor
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_tela()
        self.widgets_buttons()
        self.show_data()
        root.mainloop()
    
    #Definição da tela
    def tela(self):
        self.root.title("Banco de dados dos Exoplanetas")
        self.root.geometry("1100x700")
        self.root.resizable(True, True)#redimensionamento vertical e horizontal
        #self.root.maxsize(width = 900, height=700)#configura um tam maximo pra tela
        self.root.minsize(width= 550, height=300)
    
    #Definição dos frames da tela
    def frames_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, 
                             highlightbackground='black', highlightthickness=2)
        self.frame_1.place(relx= 0.01, rely= 0.53, relwidth=0.98, relheight=0.46)

        self.frame_2 = Frame(self.root)
        self.frame_2.place(relx=0.01, rely=0.01, relwidth=0.98 ,relheight=0.46)
    
    #Definição dos botões e labels 
    def widgets_buttons(self):
        self.abas = ttk.Notebook(self.frame_2)
        self.aba_main = Frame(self.abas)
        self.aba_insert = Frame(self.abas)
        self.aba_delete = Frame(self.abas)


        self.abas.add(self.aba_main, text='Principal')
        self.abas.add(self.aba_insert, text="Inserção")
        self.abas.add(self.aba_delete, text="Excluir")


        self.abas.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)


        #labels de local do database (no caso vai ser sempre localhost pra esse projeto)
        self.lb_host = Label(self.aba_main, text="Host:")
        self.lb_host.place(relx=0.05, rely=0.1)
        self.host_entry = Entry(self.aba_main)
        self.host_entry.place(relx= 0.2, rely=0.1)

        #inserção do usuário (pro acesso geral é o root
        self.lb_user = Label(self.aba_main, text="User:")
        self.lb_user.place(relx=0.05, rely=0.23)
        self.user_entry = Entry(self.aba_main)
        self.user_entry.place(relx= 0.2, rely=0.23)

        #inserção da senha
        self.lb_password = Label(self.aba_main, text="Password:")
        self.lb_password.place(relx=0.05, rely=0.36)
        self.password_entry = Entry(self.aba_main, show="*")
        self.password_entry.place(relx= 0.2, rely=0.36)

        #botão de conexão
        self.bt_connect = Button(self.aba_main, text="Connect", border=3, command= self.call_connection) 
        self.bt_connect.place(relx = 0.05, rely=0.85, relwidth=0.1, relheight=0.15)

        #botão de desconexão
        self.bt_desconnect = Button(self.aba_main, text="Desconnect", border=3, command= close_connection) 
        self.bt_desconnect.place(relx = 0.18, rely=0.85, relwidth=0.12, relheight=0.15)

        #botão de mostrar os dados
        self.bt_show_contents = Button(self.aba_main, text="Show Content", border=3, command= self.show_data)
        self.bt_show_contents.place(relx = 0.33, rely=0.85, relwidth=0.1, relheight=0.15)

        #botão da query_1
        self.bt_query1 = Button(self.aba_main, text="Query 1", border=3, command= self.query1)
        self.bt_query1.place(relx = 0.55, rely=0.46, relwidth=0.1, relheight=0.15)

        #botão da query_2
        self.bt_query1 = Button(self.aba_main, text="Query 2", border=3, command= self.query2)
        self.bt_query1.place(relx = 0.68, rely=0.46, relwidth=0.1, relheight=0.15)

        #botão da query_3
        self.bt_query1 = Button(self.aba_main, text="Query 3", border=3, command= self.query3)
        self.bt_query1.place(relx = 0.80, rely=0.46, relwidth=0.1, relheight=0.15)

        #botão da query_4
        self.bt_query1 = Button(self.aba_main, text="Query 4", border=3, command= self.query4)
        self.bt_query1.place(relx = 0.55, rely=0.66, relwidth=0.1, relheight=0.15)

        #botão da query_5
        self.bt_query1 = Button(self.aba_main, text="Query 5", border=3, command= self.query5)
        self.bt_query1.place(relx = 0.68, rely=0.66, relwidth=0.1, relheight=0.15)

        #botão da query_6
        self.bt_query1 = Button(self.aba_main, text="Query 6", border=3, command= self.query6)
        self.bt_query1.place(relx = 0.80, rely=0.66, relwidth=0.1, relheight=0.15)

        #label e entry de escolha da tabela
        self.lb_table = Label(self.aba_main, text="Chose table:")
        self.lb_table.place(relx=0.55, rely=0.1)
        self.table_entry = Entry(self.aba_main)
        self.table_entry.place(relx= 0.72, rely=0.1)

        #label e entry para inserção na tabela digitada
        self.lb_new_item = Label(self.aba_insert, text="Insert in the table:")
        self.lb_new_item.place(relx=0.1, rely=0.2)
        self.new_item_entry = Entry(self.aba_insert)
        self.new_item_entry.place(relx= 0.25, rely=0.2)

        self.bt_choose_table = Button(self.aba_insert, text="Get Table Columns", border=3, command= self.insert_data)
        self.bt_choose_table.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.15)

        #label e entry de consulta
        self.lb_deleted_item = Label(self.aba_delete, text="Delete from table:")
        self.lb_deleted_item.place(relx=0.1, rely=0.2)
        self.deleted_item_entry = Entry(self.aba_delete)
        self.deleted_item_entry.place(relx= 0.25, rely=0.2)

        self.bt_choose_table = Button(self.aba_delete, text="Get Table Columns", border=3, command= self.delete_data)
        self.bt_choose_table.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.15)
        

        self.listbox = tk.Listbox(self.frame_1)
        self.listbox.place(relx=0.1, rely= 0.6, relwidth=0.70, relheight=0.30)

    #conecta com o mysql 
    def call_connection(self):
        self.host = self.host_entry.get()
        self.user = self.user_entry.get()
        self.password = self.password_entry.get()
        connection(self.host, self.user, self.password)


    #insere dados na tabela cientista (Por Enquanto)
    def insert_data(self):
        self.table_name = self.new_item_entry.get()
        match self.table_name.lower(): 
            case "cientista":
                #Labels e entrys dos dados pelo usuário
                self.lb_id = Label(self.aba_insert, text="ID:")
                self.lb_id.place(relx=0.1, rely=0.3)
                self.id_entry = Entry(self.aba_insert)
                self.id_entry.place(relx= 0.15, rely=0.3)

                self.lb_name = Label(self.aba_insert, text="Name:")
                self.lb_name.place(relx=0.3, rely=0.3)
                self.name_entry = Entry(self.aba_insert)
                self.name_entry.place(relx= 0.35, rely=0.3)

                self.lb_center = Label(self.aba_insert, text="Centro:")
                self.lb_center.place(relx=0.5, rely=0.3)
                self.center_entry = Entry(self.aba_insert)
                self.center_entry.place(relx= 0.55, rely=0.3)

                self.lb_num_planets = Label(self.aba_insert, text="Num_exoplanetas:")
                self.lb_num_planets.place(relx=0.7, rely=0.3)
                self.num_planets_entry = Entry(self.aba_insert)
                self.num_planets_entry.place(relx= 0.8, rely=0.3)
                
                self.bt_insert_content = Button(self.aba_insert, text="Inserir", border=3, command=self.insert_cientista)
                self.bt_insert_content.place(relx=0.1, rely=0.8, relwidth=0.1, relheight=0.15)

    def insert_cientista(self):
        self.id = self.id_entry.get()
        self.insert_name = self.name_entry.get()
        self.insert_associated_center = self.center_entry.get()
        self.num_planets = self.num_planets_entry.get()
        self.cursor = db_connection.cursor()
        command = "INSERT INTO Cientista VALUES ('{id}' , '{name}' , {num_p} , '{center}' );".format(id=self.id, name=self.insert_name, num_p=self.num_planets, center=self.insert_associated_center)
        self.cursor.execute(command)
        db_connection.commit()
        self.cursor.close()


    def delete_data(self):
        self.table_name = self.deleted_item_entry.get()
        match self.table_name.lower(): 
            case "cientista":
                #Labels e entrys dos dados pelo usuário
                self.lb_id = Label(self.aba_delete, text="ID:")
                self.lb_id.place(relx=0.1, rely=0.3)
                self.id_entry = Entry(self.aba_delete)
                self.id_entry.place(relx= 0.15, rely=0.3)
                
                self.bt_insert_content = Button(self.aba_delete, text="Deletar", border=3, command=self.delete_cientista)
                self.bt_insert_content.place(relx=0.1, rely=0.8, relwidth=0.1, relheight=0.15)
                


    def delete_cientista(self):
        self.id = self.id_entry.get()
        self.cursor = db_connection.cursor()
        command = "DELETE FROM Cientista WHERE ID={id};".format(id=self.id)
        self.cursor.execute(command)
        db_connection.commit()
        self.cursor.close()


    #Querys de consulta do código
    def query1(self):
        self.listbox.delete(0, tk.END)
        self.cursor = db_connection.cursor()
        command = "SELECT C.nome FROM Cientista AS C NATURAL JOIN Observacao AS O WHERE O.LOCALIZACAO = 'Atacama, Chile';"
        self.cursor.execute(command)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listbox.insert(tk.END, row)
        self.cursor.close()

    def query2(self):
        self.listbox.delete(0, tk.END)
        self.cursor = db_connection.cursor()
        command = "select O.NOME_centro, E.NOME, ES.NOME_ESTRELA, ES.IDADE from Exoplaneta as E join Estrela as ES on E.ESTRELA_ASSOCIADA=ES.NOME_ESTRELA natural join identificacao_planetas as IP natural join Observacao as O where O.NOME_CENTRO='Mauna Kea';" 
        self.cursor.execute(command)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listbox.insert(tk.END, row)
        self.cursor.close()

    def query3(self):
        self.listbox.delete(0, tk.END)
        self.cursor = db_connection.cursor()
        command = "select O.NOME_CENTRO, count(*) from Exoplaneta as P join identificacao_planetas as IP on P.NOME=IP.NOME_PLANETA inner join Observacao as O on O.NOME_CENTRO=IP.NOME_CENTRO group by O.NOME_CENTRO;"
        self.cursor.execute(command)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listbox.insert(tk.END, row)
        self.cursor.close()

    def query4(self):
        self.listbox.delete(0, tk.END)
        self.cursor = db_connection.cursor()
        command = "select count(*), P.SETOR_PESQUISA from Pesquisa as P natural join P_fisica as PS group by P.SETOR_PESQUISA;"
        self.cursor.execute(command)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listbox.insert(tk.END, row)
        self.cursor.close()

    def query5(self):
        self.listbox.delete(0, tk.END)
        self.cursor = db_connection.cursor()
        command = "select NOME,num_exoplanetas from Cientista;"
        self.cursor.execute(command)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listbox.insert(tk.END, row)
        self.cursor.close()

    def query6(self):
        self.listbox.delete(0, tk.END)
        self.cursor = db_connection.cursor()
        command = "select count(*) from Estrela;"
        self.cursor.execute(command)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listbox.insert(tk.END, row)
        self.cursor.close()



    #Pega os dados da tabela para impressão
    def get_table_data(self):
        self.cursor = db_connection.cursor()
        comand = "SELECT * FROM {table_name};".format(table_name = self.table_name)
        self.cursor.execute(comand)
        data = self.cursor.fetchall()
        for row in data:
            self.respective_table.insert("", END, values=row)    
        self.cursor.close()

    #Imprime os dados do frame 2 em formato da respectiva tabela
    def show_data(self):
        self.table_name = self.table_entry.get()
        match self.table_name.lower():
            case "cientista":
                self.cientista = ttk.Treeview(self.frame_1, height=3, columns=("col1","col2","col3","col4","col5"))
                self.cientista.heading("#0", text="")
                self.cientista.heading("#1", text="ID")
                self.cientista.heading("#2", text="Nome")
                self.cientista.heading("#3", text="Exoplanetas_Identificados")
                self.cientista.heading("#4", text="Nome Centro")
                self.cientista.column("#0", width=5)
                self.cientista.column("#1", width=100)
                self.cientista.column("#2", width=100)
                self.cientista.column("#3", width=100)
                self.cientista.column("#4", width=100)
                self.cientista.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.46)
                self.respective_table = self.cientista
                self.get_table_data()
            case "observacao":
                self.c_observacao = ttk.Treeview(self.frame_1, height=3, columns=("col1","col2","col3"))
                self.c_observacao.heading("#0", text="")
                self.c_observacao.heading("#1", text="Nome")
                self.c_observacao.heading("#2", text="Localizacao")
                self.c_observacao.column("#0", width=5)
                self.c_observacao.column("#1", width=100)
                self.c_observacao.column("#2", width=100)
                self.c_observacao.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.46)
                self.respective_table = self.c_observacao
                self.get_table_data()
            case "pesquisa":
                self.c_pesquisa = ttk.Treeview(self.frame_1, height=3, columns=("col1","col2", "col3", "col4"))
                self.c_pesquisa.heading("#0", text="")
                self.c_pesquisa.heading("#1", text="ID")
                self.c_pesquisa.heading("#2", text="Num_Pesquisadores")
                self.c_pesquisa.heading("#3", text="Localizacao")
                self.c_pesquisa.heading("#4", text="Setor_Pesquisa")
                self.c_pesquisa.column("#0", width=5)
                self.c_pesquisa.column("#1", width=100)
                self.c_pesquisa.column("#2", width=100)
                self.c_pesquisa.column("#3", width=150)
                self.c_pesquisa.column("#4", width=200)
                self.c_pesquisa.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.46)
                self.respective_table = self.c_pesquisa
                self.get_table_data()
            case "exoplaneta":
                self.exoplanetas = ttk.Treeview(self.frame_1, height=2, columns=("col0","col1","col2","col3","col4","col5","col6","col7","col8","col9","col10"))
                self.exoplanetas.heading("#0", text="")
                self.exoplanetas.heading("#1", text="Nome")
                self.exoplanetas.heading("#2", text="Status")
                self.exoplanetas.heading("#3", text="Ano_Descoberta")
                self.exoplanetas.heading("#4", text="Estrela_Asso")
                self.exoplanetas.heading("#5", text="Identificação")
                self.exoplanetas.heading("#6", text="Dist_Estrela")
                self.exoplanetas.heading("#7", text="Moleculas")
                self.exoplanetas.heading("#8", text="Massa")
                self.exoplanetas.heading("#9", text="Raio")
                self.exoplanetas.heading("#10", text="Periodo")
                self.exoplanetas.column("#0", width=5)
                self.exoplanetas.column("#1", width=100)
                self.exoplanetas.column("#2", width=100)
                self.exoplanetas.column("#3", width=100)
                self.exoplanetas.column("#4", width=100)
                self.exoplanetas.column("#5", width=100)
                self.exoplanetas.column("#6", width=100)
                self.exoplanetas.column("#7", width=100)
                self.exoplanetas.column("#8", width=100)
                self.exoplanetas.column("#9", width=100)
                self.exoplanetas.column("#10", width=100)
                self.exoplanetas.place(relx=0.01, rely=0.1, relwidth=0.97, relheight=0.46)   
                self.respective_table = self.exoplanetas
                self.get_table_data()
            case "estrela":
                self.estrela = ttk.Treeview(self.frame_1, height=3, columns=("col0","col1","col2","col3","col4","col5"))
                self.estrela.heading("#0", text="")
                self.estrela.heading("#1", text="Nome")
                self.estrela.heading("#2", text="Idade")
                self.estrela.heading("#3", text="Raio")
                self.estrela.heading("#4", text="Massa")
                self.estrela.heading("#5", text="Metalicidade")
                self.estrela.column("#0", width=5)
                self.estrela.column("#1", width=100)
                self.estrela.column("#2", width=100)
                self.estrela.column("#3", width=100)
                self.estrela.column("#4", width=100)
                self.estrela.column("#5", width=100)
                self.estrela.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.46)        
                self.respective_table = self.estrela
                self.get_table_data()
            case "identificacao_estrelas":
                self.identificacao_estrelas= ttk.Treeview(self.frame_1, height=3, columns=("col1","col2","col3"))
                self.identificacao_estrelas.heading("#0", text="")
                self.identificacao_estrelas.heading("#1", text="Nome_Centro")
                self.identificacao_estrelas.heading("#2", text="Nome_estrela")
                self.identificacao_estrelas.column("#0", width=5)
                self.identificacao_estrelas.column("#1", width=100)
                self.identificacao_estrelas.column("#2", width=100)
                self.identificacao_estrelas.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.46)
                self.respective_table = self.identificacao_estrelas
                self.get_table_data()
            case "identificacao_planetas":
                self.identificacao_planetas = ttk.Treeview(self.frame_1, height=3, columns=("col1","col2","col3"))
                self.identificacao_planetas.heading("#0", text="")
                self.identificacao_planetas.heading("#1", text="Nome_Centro")
                self.identificacao_planetas.heading("#2", text="Nome_Planeta")
                self.identificacao_planetas.column("#0", width=5)
                self.identificacao_planetas.column("#1", width=100)
                self.identificacao_planetas.column("#2", width=100)
                self.identificacao_planetas.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.46)
                self.respective_table = self.identificacao_planetas
                self.get_table_data()
            case "p_biologia":
                self.p_biologia = ttk.Treeview(self.frame_1, height=3, columns=("col1","col2"))
                self.p_biologia.heading("#0", text="")
                self.p_biologia.heading("#1", text="ID Centro")
                self.p_biologia.column("#0", width=5)
                self.p_biologia.column("#1", width=100)
                self.p_biologia.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.46)
                self.respective_table = self.p_biologia
                self.get_table_data()
            case "p_fisica":
                self.p_fisica = ttk.Treeview(self.frame_1, height=3, columns=("col1","col2"))
                self.p_fisica.heading("#0", text="")
                self.p_fisica.heading("#1", text="ID Centro")
                self.p_fisica.column("#0", width=5)
                self.p_fisica.column("#1", width=100)
                self.p_fisica.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.46)
                self.respective_table = self.p_fisica
                self.get_table_data()    
            case "p_geologia":
                self.p_geologia = ttk.Treeview(self.frame_1, height=3, columns=("col1","col2"))
                self.p_geologia.heading("#0", text="")
                self.p_geologia.heading("#1", text="ID Centro")
                self.p_geologia.column("#0", width=5)
                self.p_geologia.column("#1", width=100)
                self.p_geologia.place(relx=0.01, rely=0.1, relwidth=0.98, relheight=0.46)
                self.respective_table = self.p_geologia
                self.get_table_data()    
            case default:
                self.error_message = Label(self.frame_1, text="Tabela inexistente")
                self.error_message.place(relx=0.05, rely=0.1)

App()   

