import customtkinter
from tkinter import *
from tkinter import ttk           
import sqlite3
import awesometkinter as atk
from tkinter import filedialog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter,A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser
import datetime
import time
import tkinter.messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from PIL import Image
from barcode import EAN13
from barcode.writer import ImageWriter


conn = sqlite3.connect("venda.db")
c = conn.cursor()

result = c.execute('SELECT MAX(id) from intervalo')
for r in result:
    ger = r[0]
########################### Criando a Janela ####################################
root1 =customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
#b = Application(root1)
root1.geometry('1360x760+0+0')
root1.title('Lizard System')
root1.resizable(False, False)
data = datetime.datetime.now().date()
########################### Imagens ##############################################
imgcarr=PhotoImage(master=root1,file='imagem\iiii.png')
imgcerto= PhotoImage(master=root1,file='imagem\ok.png.png')


my_image = customtkinter.CTkImage(light_image=Image.open("imagem\Texto do seu parágrafo (5).png"),dark_image=Image.open("imagem\Texto do seu parágrafo (3).png"),size=(500, 500))


imgprodu=customtkinter.CTkImage(light_image=Image.open('imagem\produ.png'),dark_image=Image.open('imagem\produ.png'),size=(48, 48))

imgutil=customtkinter.CTkImage(light_image=Image.open('imagem\ooo.png'),dark_image=Image.open('imagem\ooo.png'),size=(48, 48))

imgforne=customtkinter.CTkImage(light_image=Image.open('imagem\orne.png'),dark_image=Image.open('imagem\orne.png'),size=(48, 48))

imgrela=customtkinter.CTkImage(light_image=Image.open('imagem\_relatorio-financeiro (1).png'),dark_image=Image.open('imagem\_relatorio-financeiro (1).png'),size=(48, 48))

imgdefi=customtkinter.CTkImage(light_image=Image.open('imagem\defi.png'),dark_image=Image.open('imagem\defi.png'),size=(48, 48))

imgsair=customtkinter.CTkImage(light_image=Image.open('imagem\sair.png'),dark_image=Image.open('imagem\sair.png'),size=(48, 48))

imgvenda=customtkinter.CTkImage(light_image=Image.open('imagem\endinha.png'),dark_image=Image.open('imagem\endinha.png'),size=(48, 48))

imghis=customtkinter.CTkImage(light_image=Image.open('imagem\el.png'),dark_image=Image.open('imagem\el.png'),size=(48, 48))

imginfo=customtkinter.CTkImage(light_image=Image.open('imagem\info.png'),dark_image=Image.open('imagem\info.png'),size=(48, 48))

imgtime=customtkinter.CTkImage(light_image=Image.open('imagem\oooooo.png'),dark_image=Image.open('imagem\oooooo.png'),size=(40, 40))

imgmodo=customtkinter.CTkImage(light_image=Image.open('imagem\code_22177.png'),dark_image=Image.open('imagem\code_22177.png'),size=(48, 48))

imgrel=customtkinter.CTkImage(light_image=Image.open('imagem\estat.png'),dark_image=Image.open('imagem\estat.png'),size=(48, 48))

imgdefi=customtkinter.CTkImage(light_image=Image.open('imagem\defi.png'),dark_image=Image.open('imagem\defi.png'),size=(48, 48))

imgtec=customtkinter.CTkImage(light_image=Image.open('imagem\ec.png'),dark_image=Image.open('imagem\ec.png'),size=(48, 48))

imgcai=customtkinter.CTkImage(light_image=Image.open('imagem\money_22144.png'),dark_image=Image.open('imagem\money_22144.png'),size=(48, 48))

imgli=customtkinter.CTkImage(light_image=Image.open('imagem\prod.png.png'),dark_image=Image.open('imagem\prod.png.png'),size=(48, 48))

imgcalc=customtkinter.CTkImage(light_image=Image.open('imagem\calculator_coin_dollar_money_icon.png'),dark_image=Image.open('imagem\calculator_coin_dollar_money_icon.png'),size=(48, 48))

imginp=customtkinter.CTkImage(light_image=Image.open('imagem\incerir.png'),dark_image=Image.open('imagem\incerir.png'),size=(48, 48))

imgatuap=customtkinter.CTkImage(light_image=Image.open('imagem\pppp.png'),dark_image=Image.open('imagem\pppp.png'),size=(48, 48))

imgdelp=customtkinter.CTkImage(light_image=Image.open('imagem\delp.png'),dark_image=Image.open('imagem\delp.png'),size=(48, 48))

imgpe=customtkinter.CTkImage(light_image=Image.open('imagem\search.png.png'),dark_image=Image.open('imagem\search.png.png'),size=(48, 48))

img3=customtkinter.CTkImage(light_image=Image.open('imagem\dbok.png'),dark_image=Image.open('imagem\dbok.png'),size=(48, 48))

img4=customtkinter.CTkImage(light_image=Image.open('imagem\dberror.png'),dark_image=Image.open('imagem\dberror.png'),size=(48, 48))

img1=customtkinter.CTkImage(light_image=Image.open('imagem\enda.png'),dark_image=Image.open('imagem\enda.png'),size=(160, 160))

imgcarr=customtkinter.CTkImage(light_image=Image.open('imagem\estat.png'),dark_image=Image.open('imagem\estat.png'),size=(48, 48))

imgcarr=customtkinter.CTkImage(light_image=Image.open('imagem\iiii.png'),dark_image=Image.open('imagem\iiii.png'),size=(48, 48))

imgok=customtkinter.CTkImage(light_image=Image.open('imagem\certo.png.png'),dark_image=Image.open('imagem\certo.png.png'),size=(48, 48))

imgclo=customtkinter.CTkImage(light_image=Image.open('imagem\sair.png'),dark_image=Image.open('imagem\sair.png'),size=(48, 48))

imgrel=customtkinter.CTkImage(light_image=Image.open('imagem\estat.png'),dark_image=Image.open('imagem\estat.png'),size=(48, 48))





















































imgfac= PhotoImage(file='imagem\oooo.png')
imgint= PhotoImage(file='imagem\gram.png.png')
imgemail= PhotoImage(file='imagem\email.png.png')
imgzap= PhotoImage(file='imagem\zap.png.png')
imgyou= PhotoImage(file='imagem\you.png.png')

data = datetime.datetime.now().date()
hora= datetime.datetime.now().strftime('%H:%M')
data3 = datetime.datetime.now().strftime('%B')
data4 = datetime.datetime.now().year

sql= 'SELECT fundoq FROM config'
c.execute(sql)
resultado=c.fetchall()
for b in resultado:
    utilizador=b[0]

result=c.execute('SELECT*FROM loja')
resultado=c.fetchall()
print(resultado)
for r in resultado :
    loja=r[0]
    loja1=r[1]
    loja3=r[2]
    loja4=r[3]
    loja5=r[4]
    loja6=r[5]
    loja7=r[6]

#Função para configurar a janela no modo noturno ou light.   
def change_appearance_mode(new_appearance_mode):
    customtkinter.set_appearance_mode(new_appearance_mode)

def produto():
    lista1=[]
    result = c.execute('SELECT nome from categoria')
    for r in result:
        nome= r[0]
        print(r)
        lista1.append(str(r[0]))
    class Database:
        def __init__(self, master, *args, **kwargs):
            self.master = master


            self.frm1=customtkinter.CTkFrame(master,height=90,width=1300)
            self.frm1.place(x=0,y=0)


            self.frm3=customtkinter.CTkFrame(master,height=600,width=1300)
            self.frm3.place(x=0,y=90)




            def chamar(self, *args, **kwargs):
                vcm=(master.register(validar),'%P')

            def validar(text):
                if text=='':return True
                try:
                    value=int(text)
                except ValueError:
                    return False
                return 0<=value <=1000000000000

            vcm=(master.register(validar),'%P')

            self.lbl1=customtkinter.CTkLabel(self.frm1,text=('Cadastro de Produtos'),font=('<arial>',19))
            self.lbl1.place(x=350,y=30)

            self.lbl3=customtkinter.CTkLabel(self.frm3,text=('Código de Barra*'),font=('<arial>',14))
            self.lbl3.place(x=155,y=40)




            self.ent10=customtkinter.CTkEntry(self.frm3,width=200,placeholder_text='676896',validate='key',validatecommand=vcm,fg_color='white',text_color='black')
            self.ent10.place(x=350,y=40)

            self.lbl4=customtkinter.CTkLabel(self.frm3,text=('Estoque*'),font=('<arial>',14))
            self.lbl4.place(x=155,y=100)

            self.ent4=customtkinter.CTkEntry(self.frm3,width=200,placeholder_text='10',validate='key',validatecommand=vcm,fg_color='white',text_color='black')
            self.ent4.place(x=350,y=100)

            self.lbl5=customtkinter.CTkLabel(self.frm3,text=('Preço De Compra*'),font=('<arial>',14))
            self.lbl5.place(x=155,y=160)

            self.ent5=customtkinter.CTkEntry(self.frm3,width=200,placeholder_text='3000',validate='key',validatecommand=vcm,fg_color='white',text_color='black')
            self.ent5.place(x=350,y=160)


            self.lbl6=customtkinter.CTkLabel(self.frm3,text=('Preço De Venda*'),font=('<arial>',14))
            self.lbl6.place(x=155,y=220)

            self.ent7=customtkinter.CTkEntry(self.frm3,width=200,placeholder_text='5000',validate='key',validatecommand=vcm,fg_color='white',text_color='black')
            self.ent7.place(x=350,y=220)


            self.lbl10=customtkinter.CTkLabel(self.frm3,text=('Nome*'),font=('<arial>',14))
            self.lbl10.place(x=155,y=280)


            self.ent3=customtkinter.CTkEntry(self.frm3,width=200,placeholder_text='Telefone',fg_color='white',text_color='black')
            self.ent3.place(x=350,y=280)

            self.lbl13=customtkinter.CTkLabel(self.frm3,text=('Categoria*'),font=('<arial>',14))
            self.lbl13.place(x=155,y=340)


            self.cb1=customtkinter.CTkComboBox(self.frm3,values=lista1,state='readonly',width=210,fg_color='white',text_color='black')
            self.cb1.place(x=350,y=340)

            self.btn1=customtkinter.CTkButton(self.frm3,image=imginp,compound=RIGHT,text='Inserir',command=self.get_itens)
            self.btn1.place(x=190,y=430)
        

            self.btn3=customtkinter.CTkButton(self.frm3,text=('Apagar'),image=imgdelp,compound=RIGHT,command=self.limpar_p)
            self.btn3.place(x=360,y=430)

            self.btn4=customtkinter.CTkButton(self.frm3,text=('Atualizar'),image=imgatuap,compound=RIGHT,command=self.atualizar)
            self.btn4.place(x=515,y=430)

            self.btn5=customtkinter.CTkButton(self.frm3,text=('Pesquisar'),image=imgpe,compound=RIGHT,command=self.search)
            self.btn5.place(x=580,y=20)




        def get_itens(self, *args, **kwargs):
            self.n3=self.ent3.get()
            self.n4=self.ent4.get()
            self.n5=self.ent5.get()
            self.n7=self.ent7.get()
            self.n10=self.ent10.get()
            self.n11=self.cb1.get()


            if self.n3=='' or self.n4=='' or self.n5=='' or self.n7=='':
                tkinter.messagebox.showinfo('Sebastião Augusto', 'Por Favor preencha os campos vazios!')
            else:
                self.totalpc= float(self.ent5.get())*float(self.ent4.get())
                self.totalpv = float(self.ent7.get())*float(self.ent4.get())
                self.lucro = float(self.totalpv)-float(self.totalpc)
                self.qtd=0
                self.lucror=0
                sql= 'INSERT INTO produto( id,nome, estoque,pc, pv,lucro,categoria,quantidade,lucror) VALUES(?,?,?,?,?,?,?,?,?)'
                c.execute(sql,(self.n10,self.n3,self.n4,self.n5,self.n7,self.lucro,self.n11,self.qtd,self.lucror))
                conn.commit()

                tkinter.messagebox.showinfo('Sebastião Augusto', 'Cadastro realizado com sucesso!')
                self.limpar()
        def search(self, *args, **kwargs):
            self.codigo=self.ent10.get()
            if self.codigo=='':
                tkinter.messagebox.showinfo('Sebastião Augusto', 'Coloque o Código do Produto!')
            else:
                sql= 'SELECT * FROM produto Where id=?'
                c.execute(sql,(self.codigo,))
                resultado=c.fetchall()
                for r in resultado:
                    self.n1 = r[1]
                    self.n2 = r[2]
                    self.n4 = r[4]
                    self.n5 = r[5]
                    self.n6 = r[6]
                    self.n7 = r[7]
                self.ent3.delete(0, END)
                self.ent3.insert(0, str(self.n1))
                self.ent4.delete(0, END)
                self.ent4.insert(0, str(self.n2))
                self.ent5.delete(0, END)
                self.ent5.insert(0, str(self.n4))
                self.ent7.delete(0, END)
                self.ent7.insert(0, str(self.n5))
                self.cb1.set(self.n7)
        def atualizar(self,*args, **kwargs):
            self.a1=self.ent3.get()
            self.a2=self.ent4.get()
            self.a3=self.ent5.get()
            self.a4=self.ent7.get()
            self.a7=self.cb1.get()
            self.a8=float(self.ent5.get())*float(self.ent4.get())
            self.a9=float(self.ent7.get())*float(self.ent4.get())
            self.a10=float(self.a9)-float(self.a8)

            query = 'UPDATE  produto SET nome=?, estoque=?,pc=?, pv=?, lucro=?,categoria=? WHERE id=?'
            c.execute(query,(self.a1,self.a2,self.a3,self.a4,self.a10,self.a7,self.ent10.get()))
            conn.commit()
            tkinter.messagebox.showinfo('Controle de estoque', 'Atualização Feita')
            self.limpar()

        def limpar(self, *args, **kwargs):
            self.ent3.delete(0, END)
            self.ent4.delete(0, END)
            self.ent5.delete(0, END)
            self.ent7.delete(0, END)

        def limpar_p(self, *args, **kwargs):
            self.codigo=self.ent10.get()
            var1='DELETE from vender where id=?'
            c.execute(var1, (self.codigo,))
            self.limpar()



    janela=Toplevel()
    janela.config(bg='white')
    b = Database(janela)
    janela.iconphoto(False,PhotoImage(file='imagem\loja.png.png'))
    janela.title('Formulário Produtos')
    janela.resizable(height=False,width=False)
    janela.geometry('900x700+1+1')
    janela.grab_set()
    janela.transient(root1)
    janela.focus_force()

def caixa():
    app =customtkinter.CTkToplevel()
    app.geometry("500x400")
    app.resizable(width=False, height=False)
    app.title('Caixa')
    app.iconphoto(False,PhotoImage(file='imagem\loja.png.png'))
    app.transient(root1)
    app.grab_set()
    app.focus_force()
    frm1=customtkinter.CTkLabel(app,image=img1,text='')
    frm1.place(x=180,y=50)
    data = datetime.datetime.now().date()


    def open_caixa():
        n1='1'
        query = 'UPDATE caixa SET status=?'
        c.execute(query,(n1))
        conn.commit()
        tkinter.messagebox.showinfo('Sebastião Augusto', 'Caixa Aberto!')
        btn1.config(state=DISABLED)
        btn3.config(state=NORMAL)
        cartao1='0'
        money='0'
        total='0'
        sql= 'INSERT INTO current(datinha,cartao,dinheiro,utilizador,total) VALUES(?,?,?,?,?)'
        c.execute(sql,(data,cartao1,money,utilizador,total))
        conn.commit()



    def close_caixa():
        n1='0'
        query = 'UPDATE caixa SET status=?'
        c.execute(query,(n1))
        conn.commit()
        tkinter.messagebox.showinfo('Sebastião Augusto', 'Caixa Fechado!')
        btn3.config(state=DISABLED)
        btn1.config(state=NORMAL)
        query = 'SELECT * FROM current'
        result = c.execute(query)
        resultado=c.fetchall()
        d1=str(data3)
        d2=str(data4)
        for r in resultado:
            datinha=r[0]
            cartao=r[1]
            dinheiro=r[2]
            utilizador=r[3]
            total=r[4]
        sql= 'INSERT INTO detalhes(datat,cartao,dinheiro,usuario,total,mez,ano) VALUES(?,?,?,?,?,?,?)'
        c.execute(sql,(datinha,cartao,dinheiro,utilizador,total,d1,d2))
        conn.commit()
        apagar()

    def apagar():
        c.execute('DELETE from current')
        conn.commit()




    sql= 'SELECT status FROM caixa'
    c.execute(sql)
    resultado=c.fetchall()
    resultado1=resultado[0][0]
    print(resultado1)

    if resultado1==1:
        btn1=customtkinter.CTkButton(app,text='Abrir Caixa',image=img3,compound=LEFT,command=open_caixa,state=DISABLED)
        btn1.place(x=50,y=300)
        btn3=customtkinter.CTkButton(app,text='Fechar Caixa',image=img4,compound=LEFT,command=close_caixa,state=NORMAL)
        btn3.place(x=340,y=300)
    else:
        btn3=customtkinter.CTkButton(app,text='Fechar Caixa',image=img4,compound=LEFT,command=close_caixa,state=DISABLED)
        btn3.place(x=340,y=300)

        btn1=customtkinter.CTkButton(app,text='Abrir Caixa',image=img3,compound=LEFT,command=open_caixa,state=NORMAL)
        btn1.place(x=50,y=300)

def informacao():
    janela1 = customtkinter.CTkToplevel()
    janela1.geometry('830x650+0+0')
    janela1.title('Informações')
    janela1.iconphoto(False, PhotoImage(master=janela1, file='imagem\loja.png.png'))
    janela1.transient(root1)
    janela1.focus_force()
    janela1.grab_set()
    janela1.resizable(False, False)

    def facebook():
        webbrowser.open(
            'https://web.facebook.com/profile.php?id=100063471113802&ref_component=mbasic_bookmark&ref_page=XMenuController')

    def link():
        webbrowser.open('https://chat.whatsapp.com/BDGuS3tVxfR1AQXq0cxOwa')



    def instagram():
        webbrowser.open('https://www.instagram.com/sebastiaoaugus24/')

    def youtube():
        webbrowser.open('https://www.youtube.com/channel/UCMqGy4xIIGs01ZVcBv0B8Cw')

    def email():
        webbrowser.open('https: // mail.google.com / mail / u / 0 /?dispatcher_command = master_lookup  '
                        '# starred?compose=CllgCJqbQMQZGCpFrcGCTmXKDPtXvChGNthptBTcddnxQzSffbXGpKcrQRKpdsZXVPJHTbGhmgB')


    lblnome2 = customtkinter.CTkLabel(janela1, text='Lizard System é um software de Gestão De Vendas\n Apesar de ser fácil de Usar recomendamos a contactar os desenvolvedores para melhor Instrução',font=('<Perpetua>',14))
    lblnome2.place(x=30, y=90)

    lblnome4 =customtkinter.CTkLabel(janela1, text='Trato Dela Por Versão  2.0 por que antes disso houve outros projectos que não tiveram  sucesso\n A persistência me ajudou a chegar até Esta versão Super Top ', font=('<Perpetua>',14))
    lblnome4.place(x=30, y=580)

    lblnome6 =customtkinter.CTkLabel(janela1, text='Detalhes:', font=('<Perpetua>',17))
    lblnome6.place(x=30, y=180)

    # img1 = PhotoImage(master=janela1, file='imagem\oooo.png')
    lblnome5 =Label(janela1, text='',image=imgfac)
    lblnome5.place(x=10, y=230)

    lblnome6 =customtkinter.CTkButton(janela1, text='Lizard System', font=('<tamoha>', 18), command=facebook)
    lblnome6.place(x=90, y=240)

    # img3 = PhotoImage(master=janela1, file='imagem\zap.png.png')
    lblnomez = Label(janela1, bg='white',image=imgzap)
    lblnomez.place(x=280, y=240)

    lblnomeza =customtkinter.CTkButton(janela1, text='Comunidade Lizard', font=('<tamoha>', 18),command=link)
    lblnomeza.place(x=335, y=250)

    # img4 = PhotoImage(master=janela, file='imagem\you.png.png')
    lblnomez = Label(janela1, bg='white',image=imgyou)
    lblnomez.place(x=15, y=310)

    lblnomeyo =customtkinter.CTkButton(janela1, text='Lizards Projects',font=('<tamoha>', 18),command=youtube)
    lblnomeyo.place(x=90, y=315)

    # img5 = PhotoImage(master=janela, file='imagem\gram.png.png')
    lblnomeint = Label(janela1,bg='white',image=imgint)
    lblnomeint.place(x=280, y=310)

    lblnomein = customtkinter.CTkButton(janela1, text='sebastiaoaugus24',font=('<tamoha>', 18), command=instagram)
    lblnomein.place(x=340, y=315)

    #img6 = PhotoImage(master=janela1, file='imagem\email.png.png')
    lblnomeint = Label(janela1, bg='white',image=imgemail)
    lblnomeint.place(x=10, y=500)

    lblnomeem =customtkinter.CTkButton(janela1, text='sebasebastiaoaugusto@gmail.com',font=('<tamoha>', 18),command=email)
    lblnomeem.place(x=70, y=510)

def nova_venda():
    data = datetime.datetime.now().date()
    hora= datetime.datetime.now().strftime('%H:%M')
    data3 = datetime.datetime.now().strftime('%B')
    data4 = datetime.datetime.now().year
    selflistastock= []
    selflista_id=[]
    selflistaqtd=[]
    selflistalucro=[]
    class vender:
        def __init__(self, master, *args, **kwargs):
            self.master = master

            self.frm3=customtkinter.CTkFrame(master,width=600,height=1000)
            self.frm3.place(x=801,y=0)
            
            self.frm1=customtkinter.CTkFrame(master,width=800,height=1000)
            self.frm1.place(x=0,y=0)

            def chamar(self, *args, **kwargs):
                vcm=(master.register(validar),'%P')

            def validar(text):
                if text=='':return True
                try:
                    value=int(text)
                except ValueError:
                    return False
                return 0<=value <=1000000000000

            vcm=(master.register(validar),'%P')

            self.lista = ttk.Treeview(self.frm3, height=18, column=('col1','col2','col3','col4'))
            self.lista.heading('#0', text='')
            self.lista.heading('#1', text='NºItem')
            self.lista.heading('#2', text='Produto')
            self.lista.heading('#3', text='Quantidade')
            self.lista.heading('#4', text='Preço')

            
            self.lista.column('#0', width=10)
            self.lista.column('#1', width=70)
            self.lista.column('#2', width=150)
            self.lista.column('#3', width=150)
            self.lista.column('#4', width=150)
            self.barra_rolagen = Scrollbar(self.frm3, orient='vertical',command=self.lista.yview)
            self.lista.configure(yscroll= self.barra_rolagen.set)
            self.lista.bind('<Double-1>',self.on_click)
            self.barra_rolagen.place(x=533, y=0)
            self.lista.place(x=0, y=0)



            self.lblcdb=customtkinter.CTkLabel(self.frm1,text=('Código Do Produto'),font=('<arial>',14))
            self.lblcdb.place(x=50,y=100)

            self.entcdb=customtkinter.CTkEntry(self.frm1,width=300,font=('<arial>',14),placeholder_text='676896',validate='key',validatecommand=vcm)
            self.entcdb.place(x=260,y=100)
            self.entcdb.bind("<KeyRelease>",self.search_products)

            self.lblcb1=customtkinter.CTkLabel(self.frm1,text=('Modo De Pagamento'),font=('<arial>',14))
            self.lblcb1.place(x=10,y=450)

            self.cb1=customtkinter.CTkComboBox(self.frm1,values=['Cartão','Dinheiro','Duplo'],state='readonly')
            self.cb1.place(x=22,y=480)
            self.cb1.set('Dinheiro')


            self.lblqtd=customtkinter.CTkLabel(self.frm1,text=('Quantidade'),font=('<arial>',14))
            self.lblqtd.place(x=250,y=450)

            self.entqtd=customtkinter.CTkEntry(self.frm1,width=180,font=('<arial>',14),placeholder_text='1',validate='key',validatecommand=vcm)
            self.entqtd.place(x=220,y=480)
            self.entqtd.bind("<Return>",self.carrinho)

            self.lblmoney=customtkinter.CTkLabel(self.frm1,text=('Dinheiro'),font=('<arial>',14))
            self.lblmoney.place(x=460,y=450)

            self.entmoney=customtkinter.CTkEntry(self.frm1,width=150,font=('<arial>',14),validate='key',validatecommand=vcm)
            self.entmoney.place(x=430,y=480)

            self.lblcard=customtkinter.CTkLabel(self.frm1,text=('Cartão'),font=('<arial>',14))
            self.lblcard.place(x=660,y=450)

            self.lbltotal = customtkinter.CTkLabel(self.frm3, text='Preço Total:',font=('<arial>',14))
            self.lbltotal.place(x=0, y=400)

            self.entcard=customtkinter.CTkEntry(self.frm1,width=150,font=('<arial>',14),validate='key',validatecommand=vcm)
            self.entcard.place(x=630,y=480)

            self.lblcard=customtkinter.CTkLabel(self.frm1,text=('Cliente'),font=('<arial>',14))
            self.lblcard.place(x=50,y=560)

            self.entclie=customtkinter.CTkEntry(self.frm1,width=190,font=('<arial>',14))
            self.entclie.place(x=150,y=560)

            self.lblchange=customtkinter.CTkLabel(self.frm3,text=('Troco:'),font=('<arial>',14))
            self.lblchange.place(x=0,y=450)




            self.btn_carr =customtkinter.CTkButton(self.frm1,image=imgcarr,compound=RIGHT,text='Carrinho',command=self.carrinho)
            self.btn_carr.place(x=630, y=540)
        



            self.btn_fin = customtkinter.CTkButton(self.frm3,image=imgok,command=self.factura,text='Finalizar(F5)',compound=LEFT)
            self.btn_fin.place(x=400, y=610)
            self.master.bind("<KeyPress-F5>",self.factura)
            
            self.btn_del =customtkinter.CTkButton(self.frm3,image=imgdelp,command=self.deletar_venda,text='Limpar',compound=LEFT)
            self.btn_del.place(x=10, y=610)

            self.nome_product=customtkinter.CTkLabel(self.frm1,text='Producto :',font=('<arial>',14))
            self.nome_product.place(x=50,y=170)

            self.valor_product=customtkinter.CTkLabel(self.frm1,text='Preço : ',font=('<arial>',14))
            self.valor_product.place(x=50,y=200)

            sql= 'SELECT status FROM caixa'
            c.execute(sql)
            resultado=c.fetchall()
            self.resultado1=resultado[0][0]
            print(self.resultado1)
            if self.resultado1==0:
                self.entcdb.configure(state=DISABLED)
                
            else:
                self.entcdb.configure(state=NORMAL)

            self.treeview()
            self.inserir()
            
        def search_products(self, *args, **kwargs):
            self.cdb=self.entcdb.get()
            query = 'SELECT * FROM produto Where id=?'
            result = c.execute(query, (self.cdb,))
            resultado=c.fetchall()
            for self.r in resultado:
                self.get_id = self.r[0]
                self.get_nome = self.r[1]
                self.get_stock = self.r[2]
                self.get_inferior = self.r[3]
                self.get_cp = self.r[4]
                self.get_pv= self.r[5]
                self.get_lucro= self.r[6]
                self.get_categoria= self.r[7]
                self.fornecedor= self.r[8]
                self.quantidade= self.r[9]
                self.lucror= self.r[10]

            self.nome_product.configure(text='Producto :' + str(self.get_nome))
            self.valor_product.configure(text='Preço : ' + str(self.get_pv) + 'Kz')


        def carrinho(self, *args, **kwargs):
            self.quantity_value = int(self.entqtd.get())
            print(self.get_stock)
            if  self.quantity_value >= int(self.get_stock):
                tkinter.messagebox.showinfo('Lizard System', 'Quantidade acima do estoque!')
            else:
                self.preco_final = (float(self.quantity_value) * float(self.get_pv)) 

                self.lucrop = (self.get_pv - self.get_cp)
                self.lucrov = (self.lucrop * self.quantity_value)
                self.counter = 0
            

                self.a1 = (self.quantidade + self.quantity_value)
                self.a3 = (self.a1*self.lucrop)
                self.a0 = (self.get_stock - self.quantity_value)
                self.x_index = 0
                self.y_index = 30
                self.counter =0
                self.user=utilizador

                selflistalucro.append(self.a3)
                selflista_id.append(self.get_id)
                selflistaqtd.append(self.a1)
                selflistastock.append(self.a0)
            

                sql= 'INSERT INTO intervalo(produto,quantidade,total,datinha,hora,lucro,mes,user,ano,categoria) VALUES(?,?,?,?,?,?,?,?,?,?)'
                c.execute(sql,(self.get_nome,self.quantity_value,self.preco_final,data,hora,self.lucrov,data3,self.user,data4,self.get_categoria))
                conn.commit()

                self.totalizando()
                self.treeview()
                self.inserir()


        def caixa(self, *args, **kwargs):
            query = 'SELECT * FROM current'
            result = c.execute(query)
            resultado=c.fetchall()
            for r in resultado:
                self.cartaop=r[1]
                self.dinheiro=r[2]
            self.cc=int(self.cartaop)+int(self.cartao)
            self.d=int(self.dinheiro)+self.troco_get
            self.completo=self.cc+self.d
            sql= 'UPDATE current SET cartao=?,dinheiro=?,total=?'
            c.execute(sql,(self.cc,self.d,self.completo))
            conn.commit()
        def totalizando(self, *args, **kwargs):
            c.execute('SELECT SUM(total) FROM intervalo')
            braga=c.fetchall()
            self.totaliz=braga[0][0]
            self.lbltotal.configure(text='Total:')
            self.lbltotal.configure(text='Total:'+str(self.totaliz)+'kz')

        def troco(self, *args, **kwargs):
            self.modo=self.cb1.get()
            if self.modo=='Cartão':
                self.entcard.delete(0, END)
                self.entcard.insert(END, self.totaliz)
                self.entmoney.insert(END, 0)
                self.cartao=int(self.entcard.get())
                self.troco_get=int(self.entmoney.get())
                self.change=''
            elif self.modo=='Dinheiro':
                #self.entcard.configure(state=DISABLED)
                self.entcard.insert(END, 0)
                self.cartao=int(self.entcard.get())
                self.troco_get=int(self.entmoney.get())
                self.change=self.troco_get - self.totaliz
                self.lblchange.configure(text='Troco:'+str(self.change)+'Kz')
            elif self.modo=='Duplo':
                self.cartao=int(self.entcard.get())
                self.troco_get=int(self.entmoney.get())
                self.duplo=self.cartao + self.troco_get
                if self.duplo<self.totaliz:
                    tkinter.messagebox.showinfo('Sebastião Augusto', 'Valores Insuficientes!')
                else:
                    self.final= int((self.totaliz)-self.troco_get)
                    self.change=self.cartao-self.final
                    self.lblchange.configure(text='Troco:'+str(self.change)+'Kz')
            conn.commit()


        def treeview(self, *args, **kwargs):
            self.lista1=[]  
            sql = 'SELECT id,produto,quantidade,total FROM  intervalo '
            c.execute(sql)
            resultado=c.fetchall()
            for r in resultado:
                self.lista1.append(r)
            return self.lista1
        def inserir(self, *args, **kwargs):
            self.lista.delete(*self.lista.get_children())
            for item in self.lista1:   
                self.lista.insert('','end',values=item)

        def on_click(self, *args, **kwargs):
            self.lista.selection()
            for n in self.lista.selection():
                col1,col2,col3,col4= self.lista.item(n,'values')
                self.codigo=col1
        def deletar_venda(self, *args, **kwargs):
            c.execute('DELETE FROM intervalo')
            selflistalucro.clear()
            selflista_id.clear()
            selflistastock.clear()
            selflistaqtd.clear()
            conn.commit()
            self.treeview()
            self.inserir()
            self.totalizando()

        def banco(self, *args, **kwargs):
            c.execute('DELETE from intervalo')
            conn.commit()
        def produto(self, *args, **kwargs):
            self.listap=[]  
            sql = 'SELECT produto FROM  intervalo '
            c.execute(sql)
            resultado=c.fetchall()
            for p in resultado:
                self.listap.append(str(p[0]))
        def quantifyl(self, *args, **kwargs):
            self.listaq=[]  
            sql = 'SELECT quantidade FROM  intervalo '
            c.execute(sql)
            resultado=c.fetchall()
            for q in resultado:
                self.listaq.append(str(q[0]))

        def total(self, *args, **kwargs):
            self.listat=[]  
            sql = 'SELECT total FROM  intervalo '
            c.execute(sql)
            resultado=c.fetchall()
            for t in resultado:
                self.listat.append(str(t[0]))
        
        def datinha(self, *args, **kwargs):
            self.listad=[]  
            sql = 'SELECT datinha FROM  intervalo '
            c.execute(sql)
            resultado=c.fetchall()
            for d in resultado:
                self.listad.append(str(d[0]))
        def hora(self, *args, **kwargs):
            self.listah=[]  
            sql = 'SELECT hora FROM  intervalo '
            c.execute(sql)
            resultado=c.fetchall()
            for h in resultado:
                self.listah.append(str(h[0]))
        def lucro_b(self, *args, **kwargs):
            self.listal=[]  
            sql = 'SELECT lucro FROM  intervalo '
            c.execute(sql)
            resultado=c.fetchall()
            for l in resultado:
                self.listal.append(str(l[0]))

        def mez(self, *args, **kwargs):
            self.listam=[]  
            sql = 'SELECT mes FROM  intervalo '
            c.execute(sql)
            resultado=c.fetchall()
            for m in resultado:
                self.listam.append(str(m[0]))
        def utilizador(self, *args, **kwargs):
            self.listau=[]  
            sql = 'SELECT user FROM  intervalo '
            c.execute(sql)
            resultado=c.fetchall()
            for u in resultado:
                self.listau.append(str(u[0]))
        def ano(self, *args, **kwargs):
            self.listaa=[]  
            sql = 'SELECT ano FROM  intervalo '
            c.execute(sql)
            resultado=c.fetchall()
            for a in resultado:
                self.listaa.append(str(a[0]))
        def categoria(self, *args, **kwargs):
            self.listaca=[]  
            sql = 'SELECT categoria FROM  intervalo '
            c.execute(sql)
            resultado=c.fetchall()
            for ca in resultado:
                self.listaca.append(str(ca[0]))

        def venda(self, *args, **kwargs):
            self.produto()
            self.quantifyl()
            self.total()
            self.datinha()
            self.hora()
            self.lucro_b()
            self.mez()
            self.utilizador()
            self.ano()
            self.categoria()
            self.counter=0
            for self.v in range (len(self.listap)):
                print(self.v) 
                sql= 'INSERT INTO vender(produto,quantidade,total,datinha,hora,lucro,mes,user,ano,categoria) VALUES(?,?,?,?,?,?,?,?,?,?)'
                c.execute(sql,(self.listap[self.v],self.listaq[self.v],self.listat[self.v],self.listad[self.v],self.listah[self.v],self.listal[self.v],self.listam[self.v],self.listau[self.v],self.listaa[self.v],self.listaca[self.v]))
                conn.commit()
        def retroceder(self, *args, **kwargs):
            for self.e in range (len(selflista_id)):
                sql= 'UPDATE produto SET estoque=?,quantidade=?,lucror=? WHERE id=?'
                c.execute(sql,(selflistastock[self.e],selflistaqtd[self.e],selflistalucro[self.e],selflista_id[self.e]))
                conn.commit()

        def factura(self, *args, **kwargs):
            self.troco()
            self.caixa()
            self.venda()
            self.retroceder()
            self.banco()
            self.treeview()
            self.inserir()
            self.entclie.delete(0,END)
            self.entqtd.delete(0,END)
            c.execute('SELECT a4 FROM definicao')
            resultado3=c.fetchall()
            self.resultado3=resultado3[0][0]
            print(self.resultado3)
            if self.resultado3=='0':
                fact='Facturas\Factura'+str(ger)
                cabeça= canvas.Canvas(fact+str('.pdf'),pagesize=(300,570))
                cabeça.setFont('Helvetica-Bold',10)
                cabeça.drawImage(loja,100,480)
                cabeça.drawString(10,460,'Empresa: '+str(loja7))
                cabeça.drawString(10,440,'Comércio Geral Lda Importação e Exportação de Produto')
                cabeça.rect(10, 430, 280, 3,fill=True, stroke=False)
                cabeça.setFont('Helvetica',10)
                cabeça.drawString(10,420,'Munícipio-Bairro: '+str(loja5)+'-'+str(loja6))
                cabeça.drawString(10,410,'NIF :'+str(loja3))
                cabeça.drawString(10,400,'Telefone: '+str(loja1))
                cabeça.drawString(10,390,'Email: '+str(loja4))
                cabeça.drawString(230,380,''+str(data))
                cabeça.rect(10, 370, 280, 3,fill=True, stroke=False)
                cabeça.setFont('Helvetica',8)
                cabeça.drawString(10,360,'Produto')
                cabeça.drawString(130,360,'Qtd')
                cabeça.drawString(190,360,'Total Preço')

                for cont, l in enumerate(self.listap):
                    cabeça.drawString(10,350-10*cont,l)
                    print(type(cont))

                for conti,p in enumerate(self.listaq):
                    n1=str(p)
                    cabeça.drawString(130,350-10*conti,n1)

                for contin,q in enumerate(self.listat):
                    n3=str(q)
                    print(type(contin))
                    n4=int(contin)
                    cabeça.drawString(190,350-10*n4,n3)
                cabeça.rect(10,200, 280, 3,fill=True, stroke=False)
                self.n3=int(self.entmoney.get())
                self.n4=int(self.entcard.get())
                self.soma=self.n3+self.n4
                cabeça.drawString(10,190,'Pago'+str(self.soma)+'kz')
                cabeça.drawString(100,190,'Troco'+str(self.change)+'kz')
                cabeça.drawString(200,190,'Pagamento'+str(self.cb1.get()))
                cabeça.drawString(200,170,'Hora:'+str(hora))
                cliente=(self.entclie.get())
                cabeça.drawString(10,170,'Cliente:'+str(cliente))
                cabeça.setFont('Helvetica-Bold',10)
                cabeça.drawString(10,150,'Total:'+str(self.totaliz)+'kz')
                cabeça.drawString(100,70,'Obrigado,Volte Sempre')
                cabeça.save()
                self.deletar_venda()
                webbrowser.open(fact+str('.pdf'))
            else: 
                fact='Facturas\Factura'+str(ger)
                cabeça= canvas.Canvas(fact+str('.pdf'))
                cabeça.setFont('Helvetica-Bold',13)
                cabeça.drawImage(loja,180,650)
                cabeça.drawString(60,610,'Empresa: '+str(loja7))
                cabeça.drawString(600,590,'Comércio Geral Lda importação e exportaçâo de Produto')
                cabeça.rect(60, 575, 480, 3,fill=True, stroke=False)
                cabeça.drawString(230,160,'Obrigado,Volte Sempre')
                cabeça.drawString(60,280,'Total:'+str(self.totaliz)+'kz')
                cabeça.setFont('Helvetica',11)
                cabeça.drawString(60,565,'Munícipio-Bairro: '+str(loja5)+'-'+str(loja6))
                cabeça.drawString(60,555,'NIF :'+str(loja3))
                cabeça.drawString(60,545,'Telefone: '+str(loja1))
                cabeça.drawString(400,555,'Email: '+str(loja4))
                cabeça.drawString(400,545,''+str(data))
                cabeça.rect(60, 538, 480, 3,fill=True, stroke=False)
                #cabeça.rect(0, 528, 280, 1,fill=True, stroke=False)
                cabeça.drawString(60,523,'Produto')
                cabeça.drawString(260,523,'Qtd')
                cabeça.drawString(360,523,'Total Preço')

                for cont, l in enumerate(self.listap):
                    cabeça.drawString(60,513-10*cont,l)

                for conti,p in enumerate(self.listaq):
                    n1=str(p)
                    cabeça.drawString(260,513-10*conti,n1)
                for contin,q in enumerate(self.listat):
                    n3=str(q)
                    n4=int(contin)
                    cabeça.drawString(360,513-10*n4,n3)
                cabeça.rect(60, 353, 480, 1,fill=True, stroke=False)
                cabeça.drawString(60,343,'Pago')
                cabeça.drawString(160,343,'Troco')
                self.n3=int(self.entmoney.get())
                self.n4=int(self.entcard.get())
                self.soma=self.n3+self.n4
                cabeça.drawString(60,329,str(self.soma)+'kz')
                cabeça.drawString(160,329,str(self.change)+'kz')
                #cabeça.rect(110, 40, 380, 1,fill=True, stroke=False)
                cabeça.drawString(260,343,'Pagamento:'+str(self.cb1.get()))
                cabeça.drawString(460,313,'Hora:'+str(hora))
                cabeça.drawString(460,343,'Cliente:')
                cliente=(self.entclie.get())
                cabeça.drawString(460,329,str(cliente)) 
                cabeça.rect(60, 305, 480, 1,fill=True, stroke=False)
                cabeça.showPage()
                cabeça.save()
                self.deletar_venda()
                webbrowser.open(fact+str('.pdf'))

           





    app =customtkinter.CTkToplevel()
    app.geometry("1350x680")
    app.resizable(width=False, height=False)
    app.config(bg='#FFFFFF')
    b = vender(app)
    app.title('Formlário De Venda')
    app.iconphoto(False,PhotoImage(file='imagem\loja.png.png'))
    app.grab_set()
    app.transient(root1)
    app.focus_force()

def statics():
    janela=customtkinter.CTkToplevel()
    janela.title('Estatísticas')
    janela.config(bg='#299ebf')
    janela.geometry('1300x720')
    janela.resizable(False,False)
    janela.grab_set()
    janela.transient(root1)
    janela.focus_force()
    c = conn.cursor()
    c.execute('DELETE FROM statics_produto')
    c.execute('DELETE FROM statics_categoria')
    c.execute('DELETE FROM stastic_mes')
    c.execute('DELETE FROM statics_vendedor')

    conn.commit()









    data = datetime.datetime.now().date()
    hora= datetime.datetime.now().strftime('%H:%M')
    data3 = datetime.datetime.now().strftime('%B')
    data4 = datetime.datetime.now().year
    var3=str(data4)
    var1=str(data3)


    result='SELECT SUM(total) FROM vender where ano=? and mes=?'
    query=c.execute(result,(var3,var1,))
    resultado=c.fetchall()
    n3=resultado[0][0]

    result='SELECT SUM(lucro) FROM vender where ano=? and mes=?'
    c.execute(result,(var3,var1,))
    rt=c.fetchall()
    lucro=rt[0][0]


    c.execute('SELECT categoria FROM produto ')
    cat=c.fetchall()
    labels=[]
    for c in cat:
        labels.append(str(c[0]))
        print(labels)

    c = conn.cursor()
    c.execute('SELECT mes FROM vender ')
    mez=c.fetchall()
    meze=[]
    for m in mez:
        meze.append(str(m[0]))
        print(meze)
    nova_lim=list(set(meze))
    totals=[]
    for p in range(len(nova_lim)):
        result='SELECT SUM(total) FROM vender where mes=? and ano=?'
        c.execute(result,(nova_lim[p],var3,))
        resultado9=c.fetchall()
        for q in resultado9:
            print(q)
            totals.append(int(q[0]or 0))
    for s in range(len(nova_lim)):
        sql= 'INSERT INTO stastic_mes(nome,total) VALUES(?,?)'
        c.execute(sql,(nova_lim[s],totals[s],))
        conn.commit()

    c = conn.cursor()
    listap=[]  
    sql = 'SELECT produto FROM  vender'
    c.execute(sql)
    resultado=c.fetchall()
    for p in resultado:
        listap.append(str(p[0]))
    nova_li=list(set(listap))
    produto=[]
    print(str(nova_li))
    for p in range(len(nova_li)):
        result='SELECT SUM(total) FROM vender where produto=? and mes=? and ano=?'
        c.execute(result,(nova_li[p],var1,var3,))
        resultado3=c.fetchall()
        for q in resultado3:
            print(q)
            produto.append(int(q[0] or 0))
    for s in range(len(nova_li)):
        sql= 'INSERT INTO statics_produto(nome,total) VALUES(?,?)'
        c.execute(sql,(nova_li[s],produto[s],))
        conn.commit()

    c = conn.cursor()
    listac=[]  
    sql = 'SELECT categoria FROM  vender'
    c.execute(sql)
    resultado=c.fetchall()
    for c in resultado:
        listac.append(str(c[0]))
    nova_lic=list(set(listac))
    categoria=[]
    print(str(nova_lic))
    c = conn.cursor()
    for c1 in range(len(nova_lic)):
        result='SELECT SUM(total) FROM vender where categoria=? and mes=? and ano=? '
        query=c.execute(result,(nova_lic[c1],var1,var3,))
        resultado4=c.fetchall()
        for c3 in resultado4:
            print(c3)
            categoria.append(int(c3[0]or 0))

    for s in range(len(nova_lic)):
        sql= 'INSERT INTO statics_categoria(nome,total) VALUES(?,?)'
        c.execute(sql,(nova_lic[s],categoria[s],))
        conn.commit()

    c = conn.cursor()
    listave=[]  
    sql = 'SELECT user FROM  vender'
    c.execute(sql)
    resultado5=c.fetchall()
    for u in resultado5:
        listave.append(str(u[0]))
    nova_liv=list(set(listave))
    vendedor=[]
    print(str(nova_liv))
    for z in range(len(nova_liv)):
        result='SELECT SUM(total) FROM vender where user=? and mes=? and ano=?'
        c.execute(result,(nova_liv[z],var1,var3,))
        resultado6=c.fetchall()
        for v in resultado6:
            print(v)
            vendedor.append(int(v[0]or 0))
    for s in range(len(nova_liv)):
        sql= 'INSERT INTO statics_vendedor(nome,total) VALUES(?,?)'
        c.execute(sql,(nova_liv[s],vendedor[s],))
        conn.commit()

    lista1=[]
    lista3=[]
    lista4=[]
    lista5=[]
    lista6=[]
    lista7=[]
    lista8=[]
    lista9=[]
    sql = 'SELECT nome FROM statics_vendedor '
    c.execute(sql)
    resultado=c.fetchall()
    for n1 in resultado:
        lista1.append(str(n1[0]))

    sql = 'SELECT total FROM statics_vendedor '
    c.execute(sql)
    resultado=c.fetchall()
    for t in resultado:
        lista3.append(int(t[0] or 0))

    sql = 'SELECT nome FROM statics_categoria ORDER BY total DESC LIMIT 5'
    c.execute(sql)
    resultado=c.fetchall()
    for nc in resultado:
        lista4.append(str(nc[0]))
    sql = 'SELECT total FROM statics_categoria ORDER BY total DESC LIMIT 5'
    c.execute(sql)
    resultado=c.fetchall()
    for tc in resultado:
        lista5.append(int(tc[0] or 0))

    sql = 'SELECT nome FROM statics_produto ORDER BY total DESC LIMIT 10 '
    c.execute(sql)
    resultado=c.fetchall()
    for np in resultado:
        lista6.append(str(np[0]))

    sql = 'SELECT total FROM statics_produto ORDER BY total DESC LIMIT 10'
    c.execute(sql)
    resultado=c.fetchall()
    for tp in resultado:
        lista7.append(int(tp[0])or 0)

    sql = 'SELECT nome FROM stastic_mes'
    c.execute(sql)
    resultado=c.fetchall()
    for nm in resultado:
        lista8.append(str(nm[0]))

    sql = 'SELECT total FROM stastic_mes'
    c.execute(sql)
    resultado=c.fetchall()
    for tm in resultado:
        lista9.append(int(tm[0]or 0))

    print(lista6)
    frame_quadro=Frame(janela,width=1370 ,height=750,pady=15,padx=7,relief='flat',bg='#299ebf')
    frame_quadro.place(x=0,y=50)


    lblnome=Label(janela,bg='#299ebf',text='Extrato De Vendas',font=('arial 14 bold'))
    lblnome.place(x=530,y=10)

    frame_total=Frame(frame_quadro,width=200,bg='white',height=130,pady=15,padx=7,relief='flat')
    frame_total.place(x=5,y=30)


    lblnome1=Label(frame_total,bg='white',text='Total Vendido',font=('arial 11 bold'),anchor=CENTER)
    lblnome1.place(x=10,y=0)

    lblnome3=Label(frame_total,bg='white',text=''+str(n3)+'Kz',font=('arial 16 bold'),anchor=CENTER,fg='#59f63a')
    lblnome3.place(x=15,y=20)




    frame_quantidade=Frame(frame_quadro,width=200,bg='white',height=130,pady=15,padx=7,relief='flat')
    frame_quantidade.place(x=240,y=30)


    lblquant1=Label(frame_quantidade,bg='white',text='Valor Lucrado',font=('arial 11 bold'),anchor=CENTER)
    lblquant1.place(x=10,y=0)

    lblquant3=Label(frame_quantidade,bg='white',text=''+str(lucro)+'Kz',font=('arial 16 bold'),anchor=CENTER,fg='#59f63a')
    lblquant3.place(x=25,y=20)


    frame_mensal=Frame(frame_quadro,width=830,bg='white',height=200,pady=15,padx=7,relief='flat')
    frame_mensal.place(x=450,y=30)


    lblquant1=Label(frame_mensal,bg='white',text='Facturamento Mensal',font=('arial 11 bold'),anchor=CENTER)
    lblquant1.place(x=0,y=0)


    venda_mensal=[1500,4300,6386,9300,9300,11000,3000,4345,1780,6340,8300,7890]


    figura=plt.figure(figsize=(13.6,2.5),dpi=60)
    ax=figura.add_subplot(111)

    ax.bar(lista8,lista9, color='#82b1ff')
    c=0

    for i in ax.patches:
        ax.text(i.get_x()-.03,i.get_height()+.5,str(lista9[c])+'Kz',fontsize=13,fontstyle='italic',verticalalignment='baseline',color='black')
        c+=1
    ax.patch.set_facecolor('#FFFFFF')
    ax.spines['bottom'].set_color('black')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('black')
    ax.spines['left'].set_linewidth(1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(True)
    ax.tick_params(bottom=False,left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True,color='#EEEEEE')
    ax.xaxis.grid(False)

    canva=FigureCanvasTkAgg(figura,frame_mensal)
    canva.get_tk_widget().place(x=0,y=30)


    frame_produto=Frame(frame_quadro,width=440,bg='white',height=490,pady=15,padx=7,relief='flat')
    frame_produto.place(x=5,y=168)



    lblproduto=Label(frame_produto,bg='white',text='Facturamento Produto Top-10',font=('arial 11 bold'),anchor=CENTER)
    lblproduto.place(x=0,y=0)

    figura=plt.figure(figsize=(8,8),dpi=51.5)
    ax=figura.add_subplot(111)

    ax.barh(lista6,lista7, color='#82b1ff')
    ax.set_alpha(0.8)
    p0=0
    for i in ax.patches:
        ax.text(i.get_width()+.3,i.get_y()+.50,str(lista7[p0])+'Kz',fontsize=13,fontstyle='italic',verticalalignment='center',color='black')
        p0+=1

    ax.patch.set_facecolor('#FFFFFF')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)


    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_color('#DDDDDD')
    ax.tick_params(bottom=False,left=False)
    ax.set_axisbelow(True)
    #ax.yaxis.grid(True,color='#EEEEEE')
    ax.xaxis.grid(False)
    n1=0.1
    explode=[]
    for i in range(len(lista5)):
        explode.append((n1))

    canva_prod=FigureCanvasTkAgg(figura,frame_produto)
    canva_prod.get_tk_widget().place(x=15,y=50)

    frame_pizza=Frame(frame_quadro,width=400,bg='white',height=419,pady=15,padx=7,relief='flat')
    frame_pizza.place(x=450,y=240)


    lblcategoria=Label(frame_pizza,bg='white',text='Facturamento Por Categoria',font=('arial 11 bold'),anchor=CENTER)
    lblcategoria.place(x=0,y=0)

    figura=plt.Figure(figsize=(5.15,4),dpi=75)
    ax=figura.add_subplot(111)



    colors=['#00fbff','#ff5fb6','#ff5f68','#99ff99','#ffcc99']
    ax.pie(lista5,explode=explode,wedgeprops=dict(width=0.64),labels=lista4,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)

    canva_categoria=FigureCanvasTkAgg(figura,frame_pizza)
    canva_categoria.get_tk_widget().place(x=0,y=50)





    frame_vendedor=Frame(frame_quadro,width=420,bg='white',height=419,pady=15,padx=7,relief='flat')
    frame_vendedor.place(x=860,y=240)


    lblven=Label(frame_vendedor,bg='white',text='Facturamento Por Vendedor',font=('arial 11 bold'),anchor=CENTER)
    lblven.place(x=0,y=0)

    figura=plt.Figure(figsize=(6.8,5.8),dpi=60)
    ax=figura.add_subplot(111)


    ax.bar(lista1, lista3, color=colors)
    c=0

    for i in ax.patches:
        ax.text(i.get_x()-.03,i.get_height()+.5,str(lista3[c])+'Kz',fontsize=13,fontstyle='italic',verticalalignment='center',color='black')
        c+=1
    ax.patch.set_facecolor('#FFFFFF')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(True)
    ax.tick_params(bottom=False,left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(True,color='#EEEEEE')
    ax.xaxis.grid(False)
    canva=FigureCanvasTkAgg(figura,frame_vendedor)
    canva.get_tk_widget().place(x=0,y=50)

def calculadora():
    class Calculator(customtkinter.CTkFrame):
        def __init__(self, master, **kwargs):
            super().__init__(master,**kwargs)
            #ttk.Style().configure("TButton", font="TkFixedFont 12")
            self.pack(fill=BOTH, expand=YES)
            self.digitsvar = StringVar(value=0)
            self.xnum = DoubleVar()
            self.ynum = DoubleVar()
            self.operator = StringVar(value="+")

            if "bootstyle" in kwargs:
                self.bootstyle = kwargs.pop("bootstyle")
            else:
                self.bootstyle = None
            self.create_num_display()
            self.create_num_pad()

        def create_num_display(self):
            container = customtkinter.CTkFrame(master=self)
            container.pack(fill=X, pady=20)
            digits = customtkinter.CTkLabel(
                master=container,
                font=('<arial>',14),
                textvariable=self.digitsvar,
                anchor=E,
            )
            digits.pack(fill=X)

        def create_num_pad(self):
            container = customtkinter.CTkFrame(master=self)
            container.pack(fill=BOTH, expand=YES)
            matrix = [
                ("%", "C", "CE", "/"),
                (7, 8, 9, "*"),
                (4, 5, 6, "-"),
                (1, 2, 3, "+"),
                ("±", 0, ".", "="),
            ]
            for i, row in enumerate(matrix):
                container.rowconfigure(i, weight=1)
                for j, num_txt in enumerate(row):
                    container.columnconfigure(j, weight=1)
                    btn = self.create_button(master=container, text=num_txt)
                    btn.grid(row=i, column=j, sticky=NSEW, padx=1, pady=1)

        def create_button(self, master, text):
            return customtkinter.CTkButton(
                master=master,
                text=text,
                command=lambda x=text: self.on_button_pressed(x),
                width=2,
            )

        def reset_variables(self):
            self.xnum.set(value=0)
            self.ynum.set(value=0)
            self.operator.set("+")

        def on_button_pressed(self, txt):
            """Handles and routes all button press events."""
            display = self.digitsvar.get()

            # remove operator from screen after button is pressed
            if len(display) > 0:
                if display[0] in ["/", "*", "-", "+"]:
                    display = display[1:]

            if txt in ["CE", "C"]:
                self.digitsvar.set("")
                self.reset_variables()
            elif isinstance(txt, int):
                self.press_number(display, txt)
            elif txt == "." and "." not in display:
                self.digitsvar.set(f"{display}{txt}")
            elif txt == "±":
                self.press_inverse(display)
            elif txt in ["/", "*", "-", "+"]:
                self.press_operator(txt)
            elif txt == "=":
                self.press_equals(display)

        def press_number(self, display, txt):
            """A digit button is pressed"""
            if display == "0":
                self.digitsvar.set(txt)
            else:
                self.digitsvar.set(f"{display}{txt}")

        def press_inverse(self, display):
            """The inverse number button is pressed"""
            if display.startswith("-"):
                if len(display) > 1:
                    self.digitsvar.set(display[1:])
                else:
                    self.digitsvar.set("")
            else:
                self.digitsvar.set(f"-{display}")

        def press_operator(self, txt):
            """An operator button is pressed"""
            self.operator.set(txt)
            display = float(self.digitsvar.get())
            if self.xnum.get() != 0:
                self.ynum.set(display)
            else:
                self.xnum.set(display)
            self.digitsvar.set(txt)

        def press_equals(self, display):
            """The equals button is pressed."""
            if self.xnum.get() != 0:
                self.ynum.set(display)
            else:
                self.xnum.set(display)
            x = self.xnum.get()
            y = self.ynum.get()
            op = self.operator.get()
            if all([x, y, op]):
                result = eval(f"{x}{op}{y}")
                self.digitsvar.set(result)
                self.reset_variables()

    app = customtkinter.CTkToplevel()
    app.title('Calculadora')
    app.geometry=('650x650')
    app.iconphoto(False,PhotoImage(file='imagem\loja.png.png'))
    #app.resizable=()
    B=Calculator(app)
    app.grab_set()
    app.transient(root1)
    app.focus_force()

def categoria():
    class Application:
        def __init__(self, master, *args, **kwargs):
            self.master = master


            def chamar(self, *args, **kwargs):
                vcm=(master.register(validar),'%P')

            def validar(text):
                if text=='':return True
                try:
                    value=int(text)
                except ValueError:
                    return False
                return 0<=value <=100

            vcm=(master.register(validar),'%P')



            self.lbl1=customtkinter.CTkLabel(master,text=('Categoria'),font=('<arial>',19))
            self.lbl1.place(x=200,y=10)

            self.ent1=customtkinter.CTkEntry(master,width=250,font=('<arial>',14),validatecommand=vcm,validate='key',placeholder_text='01')
            self.ent1.place(x=160,y=80)

            self.lbl2=customtkinter.CTkLabel(master,text=('Categoria Nº'),font=('<arial>',14))
            self.lbl2.place(x=30,y=80)

            self.ent2=customtkinter.CTkEntry(master,width=250,font=('<arial>',14))
            self.ent2.place(x=160,y=130)

            self.lbl3=customtkinter.CTkLabel(master,text=('Nome'),font=('<arial>',14))
            self.lbl3.place(x=30,y=130)


            self.ent3=customtkinter.CTkEntry(master,width=250,font=('<arial>',14))
            self.ent3.place(x=160,y=170)
            self.lbl5=customtkinter.CTkLabel(master,text=('Fornecedor'),font=('<arial>',14))
            self.lbl5.place(x=30,y=170)

            self.btn1=customtkinter.CTkButton(master,compound=RIGHT,text='Inserir',command=self.cadastro,width=30, height=10)
            self.btn1.place(x=160,y=230)
            self.btn3=customtkinter.CTkButton(master,text=('Deletar'),compound=RIGHT,command=self.eliminar,width=30, height=10)
            self.btn3.place(x=260,y=230)

            self.btn3=customtkinter.CTkButton(master,text=('Atualizar'),compound=RIGHT,command=self.atualizar,width=30, height=10)
            self.btn3.place(x=360,y=230)

            self.btn5=customtkinter.CTkButton(master,text=('Pesquisar'),command=self.pesquisar,width=30, height=10)
            self.btn5.place(x=419,y=80)



        def cadastro(self, *args, **kwargs):
            self.n1=self.ent1.get()
            self.n2=self.ent2.get()
            self.n3=self.ent3.get()

            if self.n1=='' or self.n2=='' or self.n3=='':
                tkinter.messagebox.showinfo('Sebastião Augusto', 'Por Favor preencha os campos vazios!')
            else:
                sql= 'INSERT INTO categoria(numero,nome,fornecedor) VALUES(?,?,?)'
                c.execute(sql,(self.n1,self.n2,self.n3))
                conn.commit()
                tkinter.messagebox.showinfo('Sebastião Augusto', 'Cadastro Realizado com Sucesso')
        def pesquisar(self, *args, **kwargs):
                sql= 'SELECT * FROM categoria Where numero=?'
                c.execute(sql,(self.ent1.get(),))
                resultado=c.fetchall()
                for r in resultado:
                    self.n1 = r[1]
                    self.n2 = r[2]
                    
                self.ent2.delete(0, END)
                self.ent2.insert(0, str(self.n1))
                self.ent3.delete(0, END)
                self.ent3.insert(0, str(self.n2))

        def atualizar(self, *args, **kwargs):
            self.n1=self.ent2.get()
            self.n3=self.ent3.get()
            query = 'UPDATE categoria SET nome=?,fornecedor=? WHERE numero=?'
            c.execute(query, (self.n1,self.n3, self.ent1.get()))
            conn.commit()
            tkinter.messagebox.showinfo('Sebastião Augusto', 'Atualização Feita')


        def eliminar(self, *args, **kwargs):
            query='DELETE FROM categoria where numero=?'
            c.execute(query,(self.ent1.get(),))
            conn.commit()
            tkinter.messagebox.showinfo('Sebastião Augusto', 'Dados Removidos')








        


    janela1=customtkinter.CTkToplevel()
    b = Application(janela1)
    janela1.resizable(height=False,width=False)
    janela1.title('Caixa')
    janela1.iconphoto(False,PhotoImage(file='imagem\loja.png.png'))
    janela1.geometry('550x350+1+1')
    janela1.grab_set()
    janela1.focus_force()
    janela1.transient(root1)

def definicao():
    class Database:
        def __init__(self, master, *args, **kwargs):
            self.master = master




            self.frm3=customtkinter.CTkFrame(master,width=700,height=1000)
            self.frm3.place(x=300,y=0)
            
            self.frm1=customtkinter.CTkFrame(master,width=300,height=1000)
            self.frm1.place(x=0,y=0)

            self.tabControl =customtkinter.CTkTabview(master)
            self.tab2 =customtkinter.CTkFrame(self.tabControl,width=700,height=1000)
            self.tab3 =customtkinter.CTkFrame(self.tabControl,width=700,height=1000)

            self.tab2=self.tabControl.add('Funcionalidade')
            self.tab3=self.tabControl.add('Base De Dados')
            self.tabControl.pack(expand = 1, fill ="both")

            self.label9 = customtkinter.CTkLabel(self.tab2, text=' Aparência',font=('<arial>',14)) 
            self.label9.place(x=300, y=15)  


            self.label1 =customtkinter.CTkLabel(self.tab2, text='Tipo De Factura',font=('<arial>',14))
            self.label1.place(x=300, y=100)

       
            img1=PhotoImage(file='imagem\efresh_restore_rotate_undo_icon (2).png')
            img3=PhotoImage(file='imagem\efresh_restore_rotate_undo_icon (4).png')
            img4=PhotoImage(file='imagem\dbok.png')     


            self.check_var3=StringVar()
            self.lblmodo3=customtkinter.CTkCheckBox(self.tab2,text='Folha A4 ',variable=self.check_var3,onvalue='on',offvalue='off',checkmark_color='pink',command=self.factu)
            self.lblmodo3.place(x=13,y=140)        
            
            self.check_var4=StringVar()
            self.lblmodo4=customtkinter.CTkCheckBox(self.tab2,text='Ticket',variable=self.check_var4,onvalue='on',offvalue='off',checkmark_color='pink',command=self.ticket)
            self.lblmodo4.place(x=550,y=140)

            self.btn1 = customtkinter.CTkButton(self.tab2, text='Obter Licença',fg_color='pink',command=self.botao)
            self.btn1.place(x=13, y=300) 

            self.lblnome4 = customtkinter.CTkButton(self.tab2, text='Versão  2.0 ',font=('<arial>',14), fg_color='pink',command=self.link)
            self.lblnome4.place(x=640, y=410)
            self.labelcab = customtkinter.CTkLabel(self.tab3, text=' Dados Da Empresa',font=('<arial>',14))
            self.labelcab.place(x=340, y=10)

            self.label3 =customtkinter.CTkLabel(self.tab3, text='Empresa:',font=('<arial>',14))
            self.label3.place(x=10, y=100)

            self.ent3=customtkinter.CTkEntry(self.tab3,width=200,font=('<arial>',14))
            self.ent3.place(x=150,y=100)


            self.label4 =customtkinter.CTkButton(self.tab3, text='Logotipo',font=('<arial>',14),command=self.logotipo)
            self.label4.place(x=650, y=200)

            self.label4 =customtkinter.CTkLabel(self.tab3, text='Contactos:',font=('<arial>',14))
            self.label4.place(x=10, y=150)

            self.ent4=customtkinter.CTkEntry(self.tab3,width=200,font=('<arial>',14))
            self.ent4.place(x=150,y=150)

            self.label5 =customtkinter.CTkLabel(self.tab3, text='NIF:', font=('<arial>',14),)
            self.label5.place(x=360, y=100)

            self.ent5=customtkinter.CTkEntry(self.tab3,width=200,font=('<arial>',14))
            self.ent5.place(x=420,y=100)


            self.label7 = customtkinter.CTkLabel(self.tab3, text=' Munícipio:',font=('<arial>',14))
            self.label7.place(x=10, y=200)

            self.ent7=customtkinter.CTkEntry(self.tab3,width=200,font=('<arial>',14))
            self.ent7.place(x=150,y=200)

            self.label8 =customtkinter.CTkLabel(self.tab3, text=' Bairro:',font=('<arial>',14)) 
            self.label8.place(x=350, y=150)

            self.ent8=customtkinter.CTkEntry(self.tab3,width=200,font=('<arial>',14))
            self.ent8.place(x=420,y=150)

            self.label9 =customtkinter.CTkLabel(self.tab3, text=' Email:', font=('<arial>',14))
            self.label9.place(x=350, y=200)

            self.ent9=customtkinter.CTkEntry(self.tab3,width=200,font=('<arial>',14))
            self.ent9.place(x=420,y=200)



            self.cb1=customtkinter.CTkComboBox(self.tab3,values=['Produto','Venda','Caixa','Categoria'],state='readonly')
            self.cb1.place(x=180,y=310)

            self.check_var5=StringVar()
            self.lblmodo5=customtkinter.CTkCheckBox(self.tab3,text='Reiniciar base de Dados',variable=self.check_var5,onvalue='on',offvalue='off',checkmark_color='blue',fg_color='pink',text_color='black',command=self.dedados)
            self.lblmodo5.place(x=10,y=310)

            self.btn5 =customtkinter.CTkButton(self.tab3,image=imgok,compound=RIGHT,text='Guardar',fg_color='pink',command=self.terminado)
            self.btn5.place(x=640, y=380)

 



            
            c.execute('SELECT a4 FROM definicao')
            resultado3=c.fetchall()
            self.resultado3=resultado3[0][0]
            print(self.resultado3)
            if self.resultado3=='1':
                self.lblmodo3.configure(state=DISABLED)
            else:
                self.lblmodo4.configure(state=DISABLED)



        def logotipo(self, *args, **kwargs):
            self.filename1=filedialog.askopenfilename()

        def botao(self,*args, **kwargs):
            self.barra =ttk.Progressbar(self.tab2,orient=HORIZONTAL,length=250)
            self.barra.place(x=180, y=300)
            for p in range(10):
                self.barra['value']+=10
                self.tab2.update_idletasks()
                time.sleep(0.7)
            tkinter.messagebox.showinfo('Lizard System', 'A Licença será Dada Após O Pagamento A Empresa\n Por favor entre em contacto com o Desenvolvedor!')
            self.barra.destroy()

        def link(self,*args, **kwargs):
            webbrowser.open('https://ricardomassungui.github.io/site-pessoal/perfil/pg-projectos.html')




  
        def factu(self, *args, **kwargs):
            self.mgb = tkinter.messagebox.askokcancel('Configurações', 'Ativar Formato A4 para Factura?')
            print(self.mgb)
            self.n1='1'
            if self.mgb == True:
                sql= 'UPDATE definicao SET a4=?'
                c.execute(sql,(self.n1))
                conn.commit()

        def ticket(self, *args, **kwargs):
            self.mgb = tkinter.messagebox.askokcancel('Configurações', 'Ativar Formato Ticket para Factura?')
            print(self.mgb)
            self.n1='0'
            if self.mgb == True:
                sql= 'UPDATE definicao SET a4=?'
                c.execute(sql,(self.n1))
                conn.commit()


        def terminado(self, *args, **kwargs):
            self.n8=self.filename1
            self.n9=self.ent3.get()
            self.n1=self.ent4.get()
            self.n3=self.ent5.get()
            self.n5=self.ent7.get()
            self.n6=self.ent8.get()
            self.n7=self.ent9.get()
            query = 'UPDATE loja SET logotipo=?,contacto=?,nif=?, municipio=?,bairro=?, email=?,nome=?'
            c.execute(query, (self.n8,self.n1,self.n3,self.n5,self.n6,self.n7,self.n9))
            conn.commit()
            tkinter.messagebox.showinfo('Sebastião Augusto', 'Atualização Feita')
        def dedados(self, *args, **kwargs):
            self.combo=self.cb1.get()
            if self.combo=='':
                tkinter.messagebox.showinfo('Lizard', 'Selecione Os Dados a serem Deletados')
            else:
                self.mgb = tkinter.messagebox.askokcancel('Configurações', 'Tem certeza que quer reiniciar a base de dados?')
                if self.mgb == True:
                    if self.combo=='Produto':
                        c.execute('DELETE from produto')
                        conn.commit()
                    elif self.combo=='Categoria':
                        c.execute('DELETE from categoria')
                        conn.commit()
                    elif self.combo=='Caixa':
                        c.execute('DELETE from detalhes')
                        conn.commit()
                    elif self.combo=='Venda': 
                        c.execute('DELETE from vender')
                        conn.commit()                                    
                    tkinter.messagebox.showinfo('Sebastião Augusto', 'Base De Dados Reiniciada!')
                else:
                    self.mgb== False


    Windows=customtkinter.CTkToplevel()
    Windows.geometry("800x500")
    Windows.resizable(width=False, height=False)
    b = Database(Windows)
    Windows.title('Definições')
    Windows.iconphoto(False,PhotoImage(file='imagem\loja.png.png'))
    Windows.transient(root1)
    Windows.grab_set()
    Windows.focus_force()

def barcode():
    janela=customtkinter.CTkToplevel()
    janela.geometry("800x500")
    janela.resizable(width=False, height=False)
    janela.iconphoto(False,PhotoImage(file='imagem\loja.png.png'))
    janela.title('Barcode')
    janela.transient(root1)
    janela.grab_set()
    janela.focus_force()


    def gerar():
        cod=ent.get()
        my_code=EAN13(cod,writer=ImageWriter())
        my_code.save('new_code1')

    lbl1=customtkinter.CTkLabel(janela,text='Código')
    lbl1.place(x=180,y=100)

    ent=customtkinter.CTkEntry(janela,width=200)
    ent.place(x=280,y=100)

    bota1=customtkinter.CTkButton(janela,text='Gerar Barcode',corner_radius=10,border_width=1,command=gerar)
    bota1.place(x=310,y=200)

def usuario():
    class Application:
        def __init__(self, master, *args, **kwargs):
            self.master = master



            self.lbl1=customtkinter.CTkLabel(master,text=('Usuários'),font=('<arial>' ,19))
            self.lbl1.place(x=280,y=30)

            self.ent1=customtkinter.CTkEntry(master,width=200,font=('<arial>' ,14))
            self.ent1.place(x=200,y=80)

            self.lbl2=customtkinter.CTkLabel(master,text=('Nome Usuário'),font=('<arial>' ,14))
            self.lbl2.place(x=30,y=80)
            self.ent2=customtkinter.CTkEntry(master,width=200,font=('<arial>' ,14))
            self.ent2.place(x=200,y=130)

            self.lbl3=customtkinter.CTkLabel(master,text=('Nome Completo'),font=('<arial>' ,14))
            self.lbl3.place(x=30,y=130)
            vsenha = StringVar()
            self.ent3=customtkinter.CTkEntry(master,width=200,font=('<arial>' ,14),textvariable=vsenha, show='*')
            self.ent3.place(x=200,y=180)

            self.lbl4=customtkinter.CTkLabel(master,text=('Senha'),font=('<arial>' ,14))
            self.lbl4.place(x=30,y=180)

            self.ent4=customtkinter.CTkEntry(master,width=200,font=('<arial>' ,14))
            self.ent4.place(x=200,y=230)
            self.lbl5=customtkinter.CTkLabel(master,text=('Telefone'),font=('<arial>' ,14))
            self.lbl5.place(x=30,y=230)

            self.lbl6=customtkinter.CTkLabel(master,text=('Perfil'),font=('<arial>' ,14))
            self.lbl6.place(x=30,y=280)

            self.cb1=customtkinter.CTkComboBox(master,values=['Administrador','Operador'],state='readonly',width=200,fg_color='white',text_color='black')
            self.cb1.place(x=200,y=280)
            self.cb1.set('Operador')

            self.btn1=customtkinter.CTkButton(master,image=imginp,compound=RIGHT,text='Inserir',command=self.cadastro)
            self.btn1.place(x=15,y=330)

            self.btn3=customtkinter.CTkButton(master,text=('Deletar'),image=imgdelp,compound=RIGHT,command=self.eliminar)
            self.btn3.place(x=175,y=330)

            self.btn3=customtkinter.CTkButton(master,text=('Atualizar'),image=imgatuap,compound=RIGHT,command=self.atualizar)
            self.btn3.place(x=335,y=330)
            

            self.btn5=customtkinter.CTkButton(master,text=('Pesquisar'),image=imgpe,command=self.pesquisar)
            self.btn5.place(x=485,y=50)



        def cadastro(self, *args, **kwargs):
            self.n1=self.ent1.get()
            self.n2=self.ent2.get()
            self.n3=self.ent3.get()
            self.n4=self.ent4.get()
            self.n6=self.cb1.get()

            if self.n1=='' or self.n2=='' or self.n3=='' or self.n4=='':
                tkinter.messagebox.showinfo('Sebastião Augusto', 'Por Favor preencha os campos vazios!')
            else:
                sql= 'INSERT INTO users(id,name,foto,telefone,senha) VALUES(?,?,?,?,?)'
                c.execute(sql,(self.n1,self.n2,self.n6,self.n4,self.n3))
                conn.commit()
                tkinter.messagebox.showinfo('Sebastião Augusto', 'Cadastro Realizado com Sucesso')
        def pesquisar(self, *args, **kwargs):
                sql= 'SELECT * FROM users Where id=?'
                result=c.execute(sql,(self.ent1.get(),))
                resultado=c.fetchall()
                for r in resultado:
                    self.n1 = r[1]
                    self.n2 = r[2]
                    self.n3 = r[3]
                    self.n4 = r[4]
                    
                self.ent2.delete(0, END)
                self.ent2.insert(0, str(self.n1))
                self.ent3.delete(0, END)
                self.ent3.insert(0, str(self.n3))
                self.ent4.delete(0, END)
                self.ent4.insert(0, str(self.n4))
                self.cb1.set(self.n2)

        def atualizar(self, *args, **kwargs):
            self.n1=self.ent1.get()
            self.n2=self.ent2.get()
            self.n3=self.ent3.get()
            self.n4=self.ent4.get()
            self.n5=self.cb1.get()
            query = 'UPDATE users SET senha=?,name=?,foto=?,telefone=? WHERE id=?'
            c.execute(query, (self.n3, self.n2,self.n5,self.n4, self.ent1.get()))
            conn.commit()
            tkinter.messagebox.showinfo('Sebastião Augusto', 'Atualização Feita')


        def eliminar(self, *args, **kwargs):
            query='DELETE FROM users where id=?'
            c.execute(query,(self.ent1.get(),))
            conn.commit()
            tkinter.messagebox.showinfo('Sebastião Augusto', 'Dados Removidos')








        


    janela1=customtkinter.CTkToplevel()
    b = Application(janela1)
    janela1.resizable(height=False,width=False)
    janela1.iconphoto(False,PhotoImage(file='imagem\loja.png.png'))
    janela1.title('Formulário Utilizador')
    janela1.geometry('700x500+1+1')
    janela1.grab_set()
    janela1.transient(root1)
    janela1.focus_force()

def relatorio():
    janela1=customtkinter.CTkToplevel()
    janela1.resizable(height=False,width=False)
    janela1.geometry('650x350+1+1')
    janela1.title('Relatório')
    janela1.iconphoto(False,PhotoImage(file='imagem\loja.png.png'))
    janela1.grab_set()
    janela1.transient(root1)
    janela1.focus_force()


    data = datetime.datetime.now().date()
    hora= datetime.datetime.now().strftime('%H:%M')
    data3 = datetime.datetime.now().strftime('%B')
    data4 = datetime.datetime.now().year


    def anual():
        lista0=[]
        lista1=[]
        lista3=[]
        n1=str(data4)
        sql=('SELECT produto from vender WHERE ano=?')
        c.execute(sql,(n1,))
        result =c.fetchall()

        sql=('SELECT SUM(total) from vender WHERE ano=?')
        c.execute(sql,(n1,))
        result1 =c.fetchall()
        totaliza=result1[0][0]

        sql=('SELECT SUM(lucro) from vender WHERE ano=?')
        c.execute(sql,(n1,))
        result3 =c.fetchall()
        lucro=result3[0][0]

        sql=('SELECT quantidade from vender WHERE ano=?')
        c.execute(sql,(n1,))
        query = c.fetchall()

        sql=('SELECT total from vender WHERE ano=?')
        c.execute(sql,(n1,))
        marcelo =c.fetchall()
        for p in query:
            print(p)
            lista1.append(str(p[0]))
        for r in result:
            print(r)
            lista0.append(str(r[0]))

        for t in marcelo:
            print(t)
            lista3.append(str(t[0]))


        fact='Relatorio anual\Relatorio'+str(n1)
        cabeça= canvas.Canvas(fact+str('.pdf'))
        x=740
        cabeça.setFont('Helvetica',16)
        cabeça.drawString(230,760,str(n1))
        cabeça.drawString(190,780,'Relatorio anual')
        cabeça.drawString(430,740,'Preço Total')
        cabeça.drawString(240,740,'Quantidade')
        cabeça.drawString(40,740,'Produto')
        cabeça.setFont('Helvetica',11)
        x=740


        for v in range(len(lista0)):
            print(v)
            x-=20
            cabeça.drawString(40,x, str(lista0[v]))
            cabeça.drawString(260,x, str(lista1[v]))
            cabeça.drawString(430,x, str(lista3[v])) 
            if x<=80:
                cabeça.showPage()
                x=860
                x-=20
            else:
                print()
        x-=40
        cabeça.setFont('Helvetica-Bold',11)
        cabeça.drawString(40,x,'Total:'+ str(totaliza)+'Kz')
        cabeça.drawString(430,x,'Lucro:'+ str(lucro)+'Kz')

                


        cabeça.save()
        webbrowser.open(fact+str('.pdf'))


    def diario():
        lista0=[]
        lista1=[]
        lista3=[]
        n1=str(data4)
        n3=str(data)
        sql=('SELECT produto from vender WHERE datinha=?')
        c.execute(sql,(n3,))
        result =c.fetchall()


        sql=('SELECT quantidade from vender WHERE datinha=?')
        c.execute(sql,(n3,))
        query = c.fetchall()

        sql=('SELECT SUM(total) from vender WHERE datinha=?')
        c.execute(sql,(n3,))
        result1 =c.fetchall()
        totaliza=result1[0][0]

        sql=('SELECT SUM(lucro) from vender WHERE datinha=?')
        c.execute(sql,(n3,))
        result3 =c.fetchall()
        lucro=result3[0][0]

        sql=('SELECT total from vender WHERE datinha=?')
        c.execute(sql,(n3,))
        marcelo =c.fetchall()
        for p in query:
            print(p)
            lista1.append(str(p[0]))
        for r in result:
            print(r)
            lista0.append(str(r[0]))

        for t in marcelo:
            print(t)
            lista3.append(str(t[0]))

        fact='Relatorio Diario\Relatorio'+str(n3)
        cabeça= canvas.Canvas(fact+str('.pdf'))
        x=740
        cabeça.setFont('Helvetica',14)
        cabeça.drawString(190,780,'Relatório Diário De Vendas')
        cabeça.drawString(230,760,str(n3))
        cabeça.drawString(430,740,'Preço Total')
        cabeça.drawString(240,740,'Quantidade')
        cabeça.drawString(40,740,'Produto')
        cabeça.setFont('Helvetica',11)
        x=740


        for v in range(len(lista0)):
            print(v)
            x-=20
            cabeça.drawString(40,x, str(lista0[v]))
            cabeça.drawString(260,x, str(lista1[v]))
            cabeça.drawString(430,x, str(lista3[v])) 
            if x<=80:
                cabeça.showPage()
                x=860
                x-=20
            else:
                print()
        x-=60
        cabeça.setFont('Helvetica-Bold',11)
        cabeça.drawString(40,x,'Total:'+ str(totaliza)+'Kz')
        cabeça.drawString(430,x,'Lucro:'+ str(lucro)+'Kz')                


        cabeça.save()
        webbrowser.open(fact+str('.pdf'))
        
    def mensal():
        lista0=[]
        lista1=[]
        lista3=[]
        n1=str(data4)
        n3=str(data3)
        sql=('SELECT produto from vender WHERE mes=? and ano=?')
        c.execute(sql,(n3,n1,))
        result =c.fetchall()

        sql=('SELECT SUM(total) from vender WHERE mes=? and ano=?')
        c.execute(sql,(n3,n1,))
        result1 =c.fetchall()
        totaliza=result1[0][0]

        sql=('SELECT SUM(lucro) from vender WHERE mes=? and ano=?')
        c.execute(sql,(n3,n1,))
        result3 =c.fetchall()
        lucro=result3[0][0]

        sql=('SELECT quantidade from vender WHERE mes=? and ano=?')
        c.execute(sql,(n3,n1,))
        query = c.fetchall()

        sql=('SELECT total from vender WHERE mes=? and ano=?')
        c.execute(sql,(n3,n1,))
        marcelo =c.fetchall()
        for p in query:
            print(p)
            lista1.append(str(p[0]))
        for r in result:
            print(r)
            lista0.append(str(r[0]))

        for t in marcelo:
            print(t)
            lista3.append(str(t[0]))


        fact='RelatorioM\Relatorio'+str(n3)
        cabeça= canvas.Canvas(fact+str('.pdf'))
        x=740
        cabeça.setFont('Helvetica',16)
        cabeça.drawString(190,780,'Relatório Mensal De Vendas')
        cabeça.drawString(230,760,str(n3))
        cabeça.drawString(430,740,'Preço Total')
        cabeça.drawString(240,740,'Quantidade')
        cabeça.drawString(40,740,'Produto')
        cabeça.setFont('Helvetica',11)
        x=740


        for v in range(len(lista0)):
            print(v)
            x-=20
            cabeça.drawString(40,x, str(lista0[v]))
            cabeça.drawString(260,x, str(lista1[v]))
            cabeça.drawString(430,x, str(lista3[v])) 
            if x<=80:
                cabeça.showPage()
                x=860
                x-=20
            else:
                print()       
        x-=60
        cabeça.setFont('Helvetica-Bold',11)
        cabeça.drawString(40,x,'Total:'+ str(totaliza)+'Kz')
        cabeça.drawString(430,x,'Lucro:'+ str(lucro)+'Kz') 
                


        cabeça.save()
        webbrowser.open(fact+str('.pdf'))    

    def caixa_anual():
        lista0=[]
        lista1=[]
        lista3=[]
        lista4=[]
        lista5=[]
        n1=str(data4)
        sql=('SELECT cartao from detalhes WHERE ano=?')
        c.execute(sql,(n1,))
        result =c.fetchall()


        sql=('SELECT dinheiro from detalhes WHERE ano=?')
        c.execute(sql,(n1,))
        query = c.fetchall()

        sql=('SELECT total from detalhes WHERE ano=?')
        c.execute(sql,(n1,))
        marcelo =c.fetchall()

        sql=('SELECT usuario from detalhes WHERE ano=?')
        c.execute(sql,(n1,))
        c1=c.fetchall()

        sql=('SELECT datat from detalhes WHERE ano=?')
        c.execute(sql,(n1,))
        c3=c.fetchall()

        for p in query:
            print(p)
            lista1.append(str(p[0]))
        for r in result:
            print(r)
            lista0.append(str(r[0]))

        for t in marcelo:
            print(t)
            lista3.append(str(t[0]))

        for d in c1:
            print(d)
            lista5.append(str(d[0]))

        for u in c3:
            print(u)
            lista4.append(str(u[0]))




        fact='Relatorio anual\Caixa'+str(n1)
        cabeça= canvas.Canvas(fact+str('.pdf'))
        x=740
        cabeça.setFont('Helvetica',13)
        cabeça.drawString(220,780,' Entrada Do Caixa')
        cabeça.drawString(240,740,'Total')
        cabeça.drawString(140,740,'Dinheiro')
        cabeça.drawString(40,740,'Cartao')
        cabeça.drawString(340,740,'Data')
        cabeça.drawString(440,740,'Vendedor')
        cabeça.setFont('Helvetica',11)
        x=740


        for v in range(len(lista0)):
            print(v)
            x-=20
            cabeça.drawString(40,x, str(lista0[v]))
            cabeça.drawString(140,x, str(lista1[v]))
            cabeça.drawString(240,x, str(lista3[v])) 
            cabeça.drawString(340,x, str(lista4[v]))
            cabeça.drawString(460,x, str(lista5[v]))
            if x<=80:
                cabeça.showPage()
                x=860
                x-=20
            else:
                print()
                


        cabeça.save()
        webbrowser.open(fact+str('.pdf'))
    def caixa_mensal():
        lista0=[]
        lista1=[]
        lista3=[]
        lista4=[]
        lista5=[]
        n1=str(data4)
        n3=str(data3)

        sql=('SELECT cartao from detalhes WHERE ano=? and  mez=?')
        c.execute(sql,(n1,n3,))
        result =c.fetchall()


        sql=('SELECT dinheiro from detalhes WHERE ano=? and  mez=?')
        c.execute(sql,(n1,n3,))
        query = c.fetchall()

        sql=('SELECT total from detalhes WHERE ano=? and  mez=?')
        c.execute(sql,(n1,n3,))
        marcelo =c.fetchall()

        sql=('SELECT usuario from detalhes WHERE ano=? and  mez=?')
        c.execute(sql,(n1,n3))
        c1=c.fetchall()

        sql=('SELECT datat from detalhes WHERE ano=? and  mez=?')
        c.execute(sql,(n1,n3))
        c3=c.fetchall()

        for p in query:
            print(p)
            lista1.append(str(p[0]))
        for r in result:
            print(r)
            lista0.append(str(r[0]))

        for t in marcelo:
            print(t)
            lista3.append(str(t[0]))

        for d in c1:
            print(d)
            lista5.append(str(d[0]))

        for u in c3:
            print(u)
            lista4.append(str(u[0]))




        fact='RelatorioM\Caixa'+str(n3)
        cabeça= canvas.Canvas(fact+str('.pdf'))
        x=740
        cabeça.setFont('Helvetica',13)
        cabeça.drawString(220,780,' Entrada Do Caixa')
        cabeça.drawString(240,740,'Total')
        cabeça.drawString(140,740,'Dinheiro')
        cabeça.drawString(40,740,'Cartao')
        cabeça.drawString(340,740,'Data')
        cabeça.drawString(440,740,'Vendedor')
        cabeça.setFont('Helvetica',11)
        x=740


        for v in range(len(lista0)):
            print(v)
            x-=20
            cabeça.drawString(40,x, str(lista0[v]))
            cabeça.drawString(140,x, str(lista1[v]))
            cabeça.drawString(240,x, str(lista3[v])) 
            cabeça.drawString(340,x, str(lista4[v]))
            cabeça.drawString(460,x, str(lista5[v]))
            if x<=80:
                cabeça.showPage()
                x=860
                x-=20
            else:
                print()
                


        cabeça.save()
        webbrowser.open(fact+str('.pdf'))
    def cai_diario(): 
        lista0=[]
        lista1=[]
        lista3=[]
        lista4=[]
        lista5=[]
        n1=str(data)
        sql=('SELECT cartao from detalhes WHERE datat=?')
        c.execute(sql,(n1,))
        result =c.fetchall()


        sql=('SELECT dinheiro from detalhes WHERE datat=?')
        c.execute(sql,(n1,))
        query = c.fetchall()

        sql=('SELECT total from detalhes WHERE datat=?')
        c.execute(sql,(n1,))
        marcelo =c.fetchall()

        sql=('SELECT usuario from detalhes WHERE datat=?')
        c.execute(sql,(n1,))
        c1=c.fetchall()

        sql=('SELECT datat from detalhes WHERE datat=?')
        c.execute(sql,(n1,))
        c3=c.fetchall()

        for p in query:
            print(p)
            lista1.append(str(p[0]))
        for r in result:
            print(r)
            lista0.append(str(r[0]))

        for t in marcelo:
            print(t)
            lista3.append(str(t[0]))

        for d in c1:
            print(d)
            lista5.append(str(d[0]))

        for u in c3:
            print(u)
            lista4.append(str(u[0]))




        fact='Relatorio Diario\Caixa'+str(n1)
        cabeça= canvas.Canvas(fact+str('.pdf'))
        x=740
        cabeça.setFont('Helvetica',13)
        cabeça.drawString(220,780,' Entrada Do Caixa')
        cabeça.drawString(240,740,'Total')
        cabeça.drawString(140,740,'Dinheiro')
        cabeça.drawString(40,740,'Cartao')
        cabeça.drawString(340,740,'Data')
        cabeça.drawString(440,740,'Vendedor')
        cabeça.setFont('Helvetica',11)
        x=740


        for v in range(len(lista0)):
            print(v)
            x-=20
            cabeça.drawString(40,x, str(lista0[v]))
            cabeça.drawString(140,x, str(lista1[v]))
            cabeça.drawString(240,x, str(lista3[v])) 
            cabeça.drawString(340,x, str(lista4[v]))
            cabeça.drawString(460,x, str(lista5[v]))
            if x<=80:
                cabeça.showPage()
                x=860
                x-=20
            else:
                print()
                


        cabeça.save()
        webbrowser.open(fact+str('.pdf'))
    

    lbl1=customtkinter.CTkLabel(janela1,text=('Impressão De Relatórios'),font=('<arial>' ,19))
    lbl1.place(x=210,y=10)

    btn1=customtkinter.CTkButton(janela1,text='Relatório Diário:',command=diario)
    btn1.place(x=50,y=70)

    btn4=customtkinter.CTkButton(janela1,text=('Relatório Mensal'),command=mensal)
    btn4.place(x=250,y=70)

    btn3=customtkinter.CTkButton(janela1,text=('Relatório Anual'),command=anual)
    btn3.place(x=450,y=70)

    btn5=customtkinter.CTkButton(janela1,text=('Mensal Caixa'),command=caixa_mensal)
    btn5.place(x=50,y=210)
    btn6=customtkinter.CTkButton(janela1,text=('Diário  Caixa'),command=cai_diario)
    btn6.place(x=260,y=210)
    btn7=customtkinter.CTkButton(janela1,text=('Anual  Caixa'),command=caixa_anual)
    btn7.place(x=450,y=210)

def listas():
    tela = customtkinter.CTkToplevel()
    tela.title('Listagens')
    tela.iconphoto(False,PhotoImage(file='imagem\loja.png.png'))
    tela.geometry('1270x700+0+0')
    tela.focus_force()
    tela.grab_set()
    tela.resizable(False, False)



    framec = customtkinter.CTkFrame(tela, width=1350, height=1000)
    framec.place(x=0, y=270)

    tabControl =customtkinter.CTkTabview(tela)
    tab2 =customtkinter.CTkFrame(tabControl,width=700,height=1000)
    tab3 =customtkinter.CTkFrame(tabControl,width=700,height=1000)
    tab4 =customtkinter.CTkFrame(tabControl,width=700,height=1000)

    tab2=tabControl.add('Produtos')
    tab3=tabControl.add('Vendas')
    tab4=tabControl.add('Usuários')
    tabControl.pack(expand = 1, fill ="both")



    def pett():
        lista = ttk.Treeview(tab2, height=17, column=('col1','col2','col3','col4','col5','col6','col7','col8','col9','col10','col11'))
        
        lista.heading('#0', text='')
        lista.heading('#1', text='Código')
        lista.heading('#2', text='Produto')
        lista.heading('#3', text='Estoque')
        lista.heading('#4', text='Estoque Inferior')
        lista.heading('#5', text='Preço Compra')
        lista.heading('#6', text='Preço Venda')
        lista.heading('#7', text='Categoria')
        lista.heading('#8', text='Fornecedor')
        lista.heading('#9', text='Qtd Vendida')
        lista.heading('#10', text='Lucro Estimado')
        lista.heading('#11', text='Lucro de vendas')
        lista.column('#0', width=0)   
        lista.column('#1', width=50)
        lista.column('#2', width=150)
        lista.column('#3', width=100)
        lista.column('#4', width=100)
        lista.column('#5', width=100)
        lista.column('#6', width=100)
        lista.column('#7', width=150)
        lista.column('#8', width=150)
        lista.column('#9', width=110)
        lista.column('#10', width=110)
        lista.column('#11', width=110)



        barra_rolagen =customtkinter.CTkScrollbar(tab2,command=lista.yview)
        barra_rolagen.place(x=1245, y=0)

        lista.place(x=10, y=0)
        lista.configure(yscrollcommand=barra_rolagen.set)


        
        lista1=motrar()


        for item in lista1:
        
            lista.insert('','end',values=item)



    def motrar():
        sql = 'SELECT id,nome,estoque,inferior,pc,pv,categoria,fornecedor,quantidade,lucro,lucror FROM  produto'
        result =c.execute(sql)
        resultado=c.fetchall()
        lista1=[]
        for r in resultado:
            lista1.append(r)
        return lista1

    def venda():
        listav = ttk.Treeview(tab3, height=17, column=('col1','col2','col3','col4','col5','col6','col7','col8','col9','col10'))
        
        listav.heading('#0', text='')
        listav.heading('#1', text='Produto')
        listav.heading('#2', text='Quantidade')
        listav.heading('#3', text='Valor Total')
        listav.heading('#4', text='Data')
        listav.heading('#5', text='Hora')
        listav.heading('#6', text='Vendedor')
        listav.heading('#7', text='Lucro Gerado')
        listav.heading('#8', text='Categoria Produto')
        listav.heading('#9', text='Mês')
        listav.heading('#10', text='Ano')
        listav.column('#0', width=0)   
        listav.column('#1', width=50)
        listav.column('#2', width=150)
        listav.column('#3', width=100)
        listav.column('#4', width=100)
        listav.column('#5', width=100)
        listav.column('#6', width=100)
        listav.column('#7', width=150)
        listav.column('#8', width=150)
        listav.column('#9', width=110)
        listav.column('#10', width=110)




        barra_rolagenv = customtkinter.CTkScrollbar(tab3,command=listav.yview)
        barra_rolagenv.place(x=1134, y=0)

        listav.place(x=10, y=0)
        listav.configure(yscrollcommand=barra_rolagenv.set)

        lista3=list_Venda()


        for item in lista3:
        
            listav.insert('','end',values=item)



    def list_Venda():
        sql = 'SELECT produto,quantidade,total,datinha,hora,user,lucro,categoria,mes,ano FROM  vender'
        result =c.execute(sql)
        resultado1=c.fetchall()
        lista3=[]
        for r in resultado1:
            lista3.append(r)
        return lista3

    def util():
        listau = ttk.Treeview(tab4, height=17, column=('col1','col2','col3','col4','col5'))
        
        listau.heading('#0', text='')
        listau.heading('#1', text='Username')
        listau.heading('#2', text='Nome')
        listau.heading('#3', text='Perfil')
        listau.heading('#4', text='Senha')
        listau.heading('#5', text='Telefone')

        listau.column('#0', width=0)   
        listau.column('#1', width=50)
        listau.column('#2', width=150)
        listau.column('#3', width=100)
        listau.column('#4', width=100)
        listau.column('#5', width=100)





        barra_rolagenu = customtkinter.CTkScrollbar(tab4,command=listau.yview)
        barra_rolagenu.place(x=860, y=0)

        listau.place(x=360, y=0)
        listau.configure(yscrollcommand=barra_rolagenu.set)

        lista3=list_utilizador()


        for item in lista3:
        
            listau.insert('','end',values=item)



    def list_utilizador():
        sql = 'SELECT id,name,foto,senha,telefone FROM  users'
        result =c.execute(sql)
        resultado1=c.fetchall()
        lista4=[]
        for r in resultado1:
            lista4.append(r)
        return lista4

    venda()
    pett()
    util()


def relogio():
    data1 = datetime.datetime.now().strftime('%H:%M:%S')
    lblhora.after(1000,relogio)
    lblhora.configure(text=''+str(data1+'\n')+str(data))


########################## Adicionando Frame ###################################
customtkinter.set_default_color_theme('dark-blue')


frame3=customtkinter.CTkFrame(root1,height=300,width=1400)
frame3.place(x=0,y=690)

frame=customtkinter.CTkFrame(root1,height=590,width=880)
frame.place(x=230,y=80)

lbl1=customtkinter.CTkLabel(frame,image=my_image,text='')
lbl1.place(x=180,y=100)

########################## Botões ####################################################

btn1=customtkinter.CTkButton(root1,text='Produtos',image=imgprodu,compound=RIGHT,corner_radius=14, border_width=1,width=190, height=50,command=produto)
btn1.place(x=15,y=80)

btn3=customtkinter.CTkButton(root1,text='Usuários',image=imgutil,compound=RIGHT,corner_radius=14, border_width=1,width=190, height=50,command=usuario)
btn3.place(x=15,y=170)

btn4=customtkinter.CTkButton(root1,text='Categoria',image=imgforne,compound=RIGHT,corner_radius=14, border_width=1,width=190, height=50,command=categoria)
btn4.place(x=15,y=260)

btn5=customtkinter.CTkButton(root1,text='Relatório',image=imghis,compound=RIGHT,corner_radius=14, border_width=1,width=190, height=50,command=relatorio)
btn5.place(x=15,y=350)

btn6=customtkinter.CTkButton(root1,text='Nova Venda',image=imgvenda,compound=RIGHT,corner_radius=14, border_width=1,width=190, height=50,command=nova_venda)
btn6.place(x=15,y=440)

btn7=customtkinter.CTkButton(root1,text='Estatísticas',image=imgrela,compound=RIGHT,corner_radius=14, border_width=1,width=190, height=50,command=statics)
btn7.place(x=15,y=530)

btn8=customtkinter.CTkButton(root1,text='Informações',image=imginfo,compound=RIGHT,corner_radius=14, border_width=1,width=190, height=50,command=informacao)
btn8.place(x=1130,y=80)

optionmenu_1 = customtkinter.CTkOptionMenu(master=root1, corner_radius=15, values=["Light", "Dark"],width=190, height=50, command=change_appearance_mode)
optionmenu_1.place(x=1130,y=620)
optionmenu_1.set('Dark')

btn9=customtkinter.CTkButton(root1,text='Código De Barra',image=imgmodo,compound=RIGHT,corner_radius=14, border_width=1,width=190, height=50,command=barcode)
btn9.place(x=1130,y=530)

btn10=customtkinter.CTkButton(root1,text='Calculadora',image=imgcalc,compound=RIGHT,corner_radius=14, border_width=1,width=190, height=50,command=calculadora)
btn10.place(x=1130,y=440)

btn11=customtkinter.CTkButton(root1,text='Caixa',image=imgcai,compound=RIGHT,corner_radius=14, border_width=1,width=190, height=50,command=caixa)
btn11.place(x=1130,y=350)

btn13=customtkinter.CTkButton(root1,text='Definições',image=imgdefi,compound=RIGHT,corner_radius=14, border_width=1,width=190, height=50,command=definicao)
btn13.place(x=1130,y=260)

btn12=customtkinter.CTkButton(root1,text='Listas',image=imgli,compound=RIGHT,corner_radius=14, border_width=1,width=190, height=50,command=listas)
btn12.place(x=1130,y=170)

btn14=customtkinter.CTkButton(root1,text='Sair',image=imgclo,compound=RIGHT,corner_radius=14, border_width=1,width=190, height=50,command=root1.destroy)
btn14.place(x=15,y=630)


lblhora=customtkinter.CTkLabel(frame3,text='')
lblhora.place(x=1253,y=10)

relogio()

root1.mainloop()