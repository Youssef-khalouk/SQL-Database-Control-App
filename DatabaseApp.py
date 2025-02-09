
from tkinter import *
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

window=Tk()
window.geometry('1200x650+20+5')
window.resizable(False,False)
window.title('Control_Database')
window.iconbitmap('database_ico.ico')

#__________________________________________Frames__________________________________________________________

Frame_1=Frame(window,background='#c6c6c6',width=304,height=625,bd=2,relief=GROOVE)
Frame_1.place(x=5,y=35)
Frame_2=Frame(window,background='#c6c6c6',width=304,height=200,bd=2,relief=GROOVE)
Frame_2.place(x=315,y=35)

#__________________________________________Labels_________________________________________________________

l1=Label(window,text='Database',background='#ff948c',font=('tajawal',15,'bold'))
l1.pack(fill=X)

                               #===========Frame_1============
l2=Label(Frame_1,text='Connect Database',width=42,background='#ff948c') 
l2.place(x=0,y=0)
l3=Label(Frame_1,text=' Server Name :',background='#c6c6c6')
l3.place(x=5,y=30)
l4=Label(Frame_1,text='\tUser :',background='#c6c6c6')
l4.place(x=5,y=60)
l5=Label(Frame_1,text='       password :',background='#c6c6c6')
l5.place(x=5,y=90)
lib1=Label(Frame_1,text='',background='#c6c6c6')
lib1.place(x=5,y=140)
lib2=Label(Frame_1,text='[Vide]',background='#c6c6c6')
lib2.place(x=130,y=200)

                               #===========Frame_2============
l6=Label(Frame_2,text='Create Database',width=42,background='#ff948c')
l6.place(x=0,y=0)
l7=Label(Frame_2,text=' DB Name :',background='#c6c6c6')
l7.place(x=5,y=30)
l8=Label(Frame_2,text='Table cols :',background='#c6c6c6')
l8.place(x=5,y=130)
l9=Label(Frame_2,text='  Add cols :',background='#c6c6c6')
l9.place(x=5,y=160)
l10=Label(Frame_1,text='Database Founds',width=42,background='#ff948c')
l10.place(x=0,y=175)

image1=PhotoImage(file='database.png',width=700,height=630)
l11=Label(window,image=image1)
l11.place(x=675,y=30)

#__________________________________________Entrys_________________________________________________________
                               #===========Frame_1============

va1=StringVar()
va2=StringVar()

Entry_1=Entry(Frame_1,textvariable=va1,justify='center',bd=1)
Entry_1.place(x=90,y=30)
Entry_2=Entry(Frame_1,textvariable=va2,justify='center',bd=1)
Entry_2.place(x=90,y=60)
Entry_3=Entry(Frame_1,justify='center',bd=1)
Entry_3.place(x=90,y=90)

va1.set('localhost')
va2.set('root')

                               #===========Frame_2============
Entry_10=StringVar()                               
Entry_4=Entry(Frame_2,justify='center',textvariable=Entry_10,bd=1)
Entry_4.place(x=90,y=30)

#__________________________________________Buttons_________________________________________________________
                               #===========Frame_1============
Button_1=Button(Frame_1,text='Connect',height=3,bd=1,cursor='hand2',bg='whitesmoke')
Button_1.place(x=220,y=42)

                               #===========Frame_2============
Button_2=Button(Frame_2,text='Create Table',width=15,bd=1,cursor='hand2',bg='whitesmoke')
Button_2.place(x=100,y=130)
Button_3=Button(Frame_2,text='Add Columns',width=15,bd=1,cursor='hand2',bg='whitesmoke')
Button_3.place(x=100,y=160)
Button_4=Button(Frame_2,text='Create',background='#f4dfb4',bd=1,cursor='hand2',width=10,bg='whitesmoke')
Button_4.place(x=160,y=70)
Button_5=Button(Frame_2,text='Delete',background='#f4dfb4',bd=1,cursor='hand2',width=10,bg='whitesmoke')
Button_5.place(x=70,y=70)
Button_6=Button(Frame_2,text='Hide',background='#f4dfb4',bd=1,cursor='hand2',foreground='blue',width=7)
Button_6.place(x=240,y=130)
Button_7=Button(Frame_2,text='Hide',background='#f4dfb4',bd=1,cursor='hand2',foreground='blue',width=7)
Button_7.place(x=240,y=160)

#__________________________________________Fonctions_________________________________________________________

global background_1
background_1=StringVar()
background_2=StringVar()
background_3=StringVar()
background_4=StringVar()
background_1.set('#c6c6c6')
background_2.set('#ff948c')
background_4.set('#7ED5C5')
Vx=StringVar()
def DataBase_F(v1,v2,v3):
    Data=mysql.connector.connect(host=v1,user=v2,password=v3)
    cursor=Data.cursor()
    cursor.execute('show Databases')
    global frame_Database
    frame_Database=LabelFrame(Frame_1,text='Database',background=background_1.get(),width=295,height=415,bd=2)
    frame_Database.place(x=2,y=200)   
    x=1
    y=10 
    for row in cursor:
        ll=Label(frame_Database,text=(x,':',row),background=background_1.get())
        ll.place(x=15,y=y)
        y+=30
        x+=1 
    cursor.close()
    global AA
    def AA(theme):
        if theme == 'Light_mode':
            for wedget in frame_Database.winfo_children():
                wedget.config(bg='#c6c6c6')
        elif theme == 'Darck_mode':
            for wedget in frame_Database.winfo_children():
                wedget.config(bg='#383B7A')
        else:
            pass
var1=StringVar()
var2=StringVar()
var3=StringVar()     
def DBconect():
    var1.set(Entry_1.get())
    var2.set(Entry_2.get())
    var3.set(Entry_3.get())
    try:
        Data=mysql.connector.connect(host=var1.get(),user=var2.get(),password=var3.get())
        cursor=Data.cursor()
        cursor.execute('show Databases')
        lib1.config(text='√ Server conected secesfuly',foreground='green')
        lib2.config(text='')
        DataBase_F(var1.get(),var2.get(),var3.get())
        Vx.set('True')
        Button_1.config(text='dsconnected',fg='red')
        messagebox.showinfo('Connected','Connected secsesfuly')
    except mysql.connector.Error as error :
        messagebox.showerror('Error',error) 
        Entry_1.delete(0,'end')
        Entry_2.delete(0,'end')
        Entry_3.delete(0,'end')     
def DB_dsconnected():
    var1.set('')
    var2.set('')
    var3.set('')  
    Button_1.config(text='Connect',fg='black')
    try:
        try:
            create_table_frame.destroy()
        except:    
            Add_Column_Frame.destroy()
    except:
        pass
    lib1.config(text='')
    Vx.set('')
    lib2.config(text='[Vide]')
    frame_Database.destroy()
    messagebox.showinfo('Dsconnected','Desconnected seccesfuly')
def Delete_Database():
    try:
        Data=mysql.connector.connect(host=var1.get(),user=var2.get(),password=var3.get())
        cursor=Data.cursor()
        cursor.execute('drop database {}'.format(Entry_4.get()))
        Entry_4.delete(0,'end')
        frame_Database.destroy()
        cursor.close()
        DataBase_F(var1.get(),var2.get(),var3.get())
        
        messagebox.showinfo(title='Delete',message='Deleted secsesfuly')
    except mysql.connector.Error as error:
        messagebox.showerror('Error',error)
def DBcreate():
    try:
        Data=mysql.connector.connect(host=var1.get(),user=var2.get(),password=var3.get())
        cursor=Data.cursor()
        cursor.execute('create database {}'.format(Entry_4.get()))
        Entry_4.delete(0,'end')
        frame_Database.destroy()
        DataBase_F(var1.get(),var2.get(),var3.get())
        cursor.close()
        messagebox.showinfo('Create Database','Database is created')
    except mysql.connector.Error as error:
        messagebox.showerror('Error',error)
def Create_Table():
    try:
        Data=mysql.connector.connect(host=var1.get(),user=var2.get(),password=var3.get())
        cursor=Data.cursor()
        cursor.execute('show Databases')
        global create_table_frame
        create_table_frame=Frame(window,background=background_1.get(),bd=2,relief=GROOVE)
        create_table_frame.place(x=315,y=240,width=304,height=420)
        lll=Label(create_table_frame,text='Create Table',background=background_2.get())
        lll.pack(fill=X)
        lll1=Label(create_table_frame,text='Select DB Name :',background=background_1.get())
        lll1.place(x=5,y=30)
        lest0=[]
        for row in cursor:
            lest0.append(row)
        combobox_var0=StringVar()
        ttk.Combobox(create_table_frame,values=lest0,textvariable=combobox_var0).place(x=120,y=30)
        cursor.close()
        lll2=Label(create_table_frame,text='Table Name :',background=background_1.get())
        lll2.place(x=5,y=60)
        Entry_5=Entry(create_table_frame,justify='center',width=23)
        Entry_5.place(x=120,y=60)
        lll3=Label(create_table_frame,text='Columen Name :',background=background_1.get())
        lll3.place(x=5,y=90)
        Entry_6=Entry(create_table_frame,justify='center',width=23)
        Entry_6.place(x=120,y=90)
        lll4=Label(create_table_frame,text='Taype Name :',background=background_1.get())
        lll4.place(x=5,y=120)
        combobox_var2=StringVar()
        lest2=['INT','VARCHAR','TEXT','DATE','INTEGER PRIMARY KEY AUTO_INCREMENT']
        ttk.Combobox(create_table_frame,values=lest2,textvariable=combobox_var2).place(x=120,y=120)
        lll5=Label(create_table_frame,text='length :',background=background_1.get())
        lll5.place(x=5,y=150)
        combobox_var3=StringVar()
        lest3=['11','100','200','1000','10000']
        ttk.Combobox(create_table_frame,values=lest3,textvariable=combobox_var3).place(x=120,y=150)
        global Df
        def Df(Theme):
            if Theme == 'Darck_mode':
                create_table_frame.config(bg='#383B7A')
                lll.config(bg='#050847')
                lll1.config(bg='#383B7A')
                lll2.config(bg='#383B7A')
                lll3.config(bg='#383B7A')
                lll4.config(bg='#383B7A')
                lll5.config(bg='#383B7A')
                Button_8.config(bg='#178082')
            elif Theme == 'Light_mode':
                create_table_frame.config(bg='#c6c6c6')
                lll.config(bg='#ff948c')
                lll1.config(bg='#c6c6c6')
                lll2.config(bg='#c6c6c6')
                lll3.config(bg='#c6c6c6')
                lll4.config(bg='#c6c6c6')
                lll5.config(bg='#c6c6c6')
                Button_8.config(bg='#7ED5C5')
        def Create_Table():
            try:
                Data=mysql.connector.connect(host=var1.get(),user=var2.get(),password=var3.get(),database=combobox_var0.get())
                cursor=Data.cursor()
                var_=combobox_var2.get()
                if var_ == 'INTEGER PRIMARY KEY AUTO_INCREMENT' or 'DATE':
                    cursor.execute('CREATE TABLE {} ( {} {} )'.format(Entry_5.get(),Entry_6.get(),combobox_var2.get()))
                    cursor.close()
                    messagebox.showinfo('Create table','Table is created scsesfuly')
                    Entry_5.delete(0,'end')
                    Entry_6.delete(0,'end')
                    combobox_var2.set('')
                    combobox_var3.set('')
                else:
                    cursor.execute('CREATE TABLE {} ( {} {} ({}))'.format(Entry_5.get(),Entry_6.get(),combobox_var2.get(),combobox_var3.get()))
                    cursor.close()
                    messagebox.showinfo('Create table','Table is created scsesfuly')
                    Entry_5.delete(0,'end')
                    Entry_6.delete(0,'end')
                    combobox_var2.set('')
                    combobox_var3.set('')
            except mysql.connector.Error as error :
                messagebox.showerror('Error',error)
        Button_8=Button(create_table_frame,command=Create_Table,text='Create table and ferst columen',bg=background_4.get(),padx=1,pady=1,bd=1,cursor='hand2')
        Button_8.place(x=80,y=180)
    except:
        messagebox.showerror(title='Error',message='Connect server ferst!')
def Add_Columns():
    try:
        def Rest(event):
            comb.destroy()  
            Data=mysql.connector.connect(host=var1.get(),user=var2.get(),password=var3.get(),database=combobox_var0.get())
            cursor=Data.cursor()
            cursor.execute('show tables')
            lest6=[]
            for row in cursor:
                lest6.append(row)
            comb1=ttk.Combobox(Add_Column_Frame,values=lest6,textvariable=combobox_var4)
            comb1.place(x=120,y=60)
        Data=mysql.connector.connect(host=var1.get(),user=var2.get(),password=var3.get())
        cursor=Data.cursor()
        cursor.execute('show Databases')
        global Add_Column_Frame
        Add_Column_Frame=Frame(window,background=background_1.get(),bd=2,relief=GROOVE)
        Add_Column_Frame.place(x=315,y=240,width=304,height=420)
        ll1=Label(Add_Column_Frame,text='Add Columnes',background=background_2.get())
        ll1.pack(fill=X)
        ll2=Label(Add_Column_Frame,text='Select DB Name :',background=background_1.get())
        ll2.place(x=5,y=30)
        lest0=[]
        for row in cursor:
            lest0.append(row)
        combobox_var0=StringVar()
        comb2=ttk.Combobox(Add_Column_Frame,values=lest0,textvariable=combobox_var0)
        comb2.place(x=120,y=30)
        comb2.bind("<<ComboboxSelected>>",Rest)
        ll3=Label(Add_Column_Frame,text='Select Table :',background=background_1.get())
        ll3.place(x=5,y=60)
        lest6=[]
        combobox_var4=StringVar()
        comb=ttk.Combobox(Add_Column_Frame,values=lest6,textvariable=combobox_var4)
        comb.place(x=120,y=60)
        global Dcol
        def Dcol(Theme):
            if Theme == 'Darck_mode':
                Add_Column_Frame.config(bg='#383B7A')
                ll1.config(bg='#050847')
                ll2.config(bg='#383B7A')
                ll3.config(bg='#383B7A')
                Button_9.config(bg='#178082')
                Button_10.config(bg='#178082')
                Button_11.config(bg='#178082')
                try:
                    Acol('Darck_mode')
                except:
                    pass
            elif Theme == 'Light_mode': 
                Add_Column_Frame.config(bg='#c6c6c6')
                ll1.config(bg='#ff948c')
                ll2.config(bg='#c6c6c6')
                ll3.config(bg='#c6c6c6')
                Button_9.config(bg='#7ED5C5')
                Button_10.config(bg='#7ED5C5')
                Button_11.config(bg='#7ED5C5')                
                try:
                    Acol('Light_mode')
                except:
                    pass
        def create_col():
            varr=combobox_var0.get()
            if varr !='':
                frame_Database1=LabelFrame(Add_Column_Frame,text='Create Columns',background=background_1.get(),width=295,height=280,bd=2)
                frame_Database1.place(x=2,y=120)
                Data=mysql.connector.connect(host=var1.get(),user=var2.get(),password=var3.get(),database=varr)
                l1=Label(frame_Database1,text='Columen Name :',background=background_1.get())
                l1.place(x=5,y=30)
                Entry_6=Entry(frame_Database1,justify='center',width=23)
                Entry_6.place(x=120,y=30)
                l2=Label(frame_Database1,text='Taype Name :',background=background_1.get())
                l2.place(x=5,y=60)
                combobox_var2=StringVar()
                lest2=['INT','VARCHAR','TEXT','DATE','INTEGER PRIMARY KEY AUTO_INCREMENT']
                ttk.Combobox(frame_Database1,values=lest2,textvariable=combobox_var2).place(x=120,y=60)
                l3=Label(frame_Database1,text='length :',background=background_1.get())
                l3.place(x=5,y=90)
                combobox_var3=StringVar()
                lest3=['11','100','200','1000','10000']
                ttk.Combobox(frame_Database1,values=lest3,textvariable=combobox_var3).place(x=120,y=90)
                l4=Label(frame_Database1,text='Default :',background=background_1.get())
                l4.place(x=5,y=120)
                combobox_var5=StringVar()
                lest4=['NOT NULL','NULL']
                ttk.Combobox(frame_Database1,values=lest4,textvariable=combobox_var5).place(x=120,y=120)
                lest5=['FIRST']
                Data=mysql.connector.connect(host=var1.get(),user=var2.get(),password=var3.get(),database=varr)
                cursor=Data.cursor()
                cursor.execute(' describe  {}'.format(combobox_var4.get()))        
                for row in cursor:
                    lest5.append('After '+row[0])       
                l5=Label(frame_Database1,text='Size :',background=background_1.get())
                l5.place(x=5,y=150)            
                combobox_var6=StringVar()               
                comboS=ttk.Combobox(frame_Database1,values=lest5,textvariable=combobox_var6)
                comboS.place(x=120,y=150)
                global Acol
                def Acol(Theme):
                    if Theme == 'Darck_mode':
                        frame_Database1.config(bg='#383B7A')
                        l1.config(bg='#383B7A')
                        l2.config(bg='#383B7A')
                        l3.config(bg='#383B7A')
                        l4.config(bg='#383B7A')
                        l5.config(bg='#383B7A')
                        Button_8.config(bg='#178082')                    
                    elif Theme == 'Light_mode': 
                        frame_Database1.config(bg='#c6c6c6')
                        l1.config(bg='#c6c6c6')
                        l2.config(bg='#c6c6c6')
                        l3.config(bg='#c6c6c6')
                        l4.config(bg='#c6c6c6')
                        l5.config(bg='#c6c6c6')
                        Button_8.config(bg='#7ED5C5')
                def Create_columns():
                    var01=combobox_var2.get()
                    var02=combobox_var4.get()
                    var03=Entry_6.get()
                    var04=combobox_var3.get()
                    var05=combobox_var5.get()
                    var06=combobox_var6.get()
                    if var01 == 'INTEGER PRIMARY KEY AUTO_INCREMENT':
                        try:
                            Data=mysql.connector.connect(host=var1.get(),user=var2.get(),password=var3.get(),database=varr)
                            cursor=Data.cursor()                        
                            cursor.execute('ALTER TABLE {} ADD {} {} {}'.format(var02,var03,var01,var06))
                            cursor.close()
                            messagebox.showinfo('Add column','Column is created')
                            Entry_6.delete(0,'end')
                            combobox_var2.set('')
                            combobox_var3.set('')
                            combobox_var5.set('')
                            combobox_var6.set('')
                        except mysql.connector.Error as error:
                            messagebox.showerror('Error',error)
                    else:
                        try:
                            Data=mysql.connector.connect(host=var1.get(),user=var2.get(),password=var3.get(),database=varr)
                            cursor=Data.cursor()                
                            cursor.execute('ALTER TABLE {} ADD {} {}({}) {} {}'.format(var02,var03,var01,var04,var05,var06))
                            cursor.close()
                            messagebox.showinfo('Add column','Column is created')
                            Entry_6.delete(0,'end')
                            combobox_var2.set('')
                            combobox_var3.set('')
                            combobox_var5.set('')
                            combobox_var6.set('')
                        except mysql.connector.Error as error:
                            messagebox.showerror('Error',error)
                Button_8=Button(frame_Database1,command=Create_columns,text='Add column',bg=background_4.get(),width=20,padx=1,pady=1,bd=1,cursor='hand2')
                Button_8.place(x=80,y=210)
            else:
                messagebox.showerror('Error','select DB to get Tables in it ')     
        def Delete_Table():
            try:
                Data=mysql.connector.connect(host=var1.get(),user=var2.get(),password=var3.get(),database=combobox_var0.get())
                cursor=Data.cursor()
                cursor.execute(' drop Table {}'.format(combobox_var4.get()))
                combobox_var4.set('')
                cursor.close()
                messagebox.showinfo('Deleted','deleted seccesfuly')
            except mysql.connector.Error as r:
                messagebox.showerror('Error',r)
        def Table_Lest():       
            aa=Tk()
            aa.title('Table')
            aa.geometry('658x444+300+100')
            F10=Frame(aa,width=660,height=405)
            F10.place(x=0,y=40)
            def Col_Tabel_Info():
                B10.config(state=DISABLED)
                B11.config(state=NORMAL)
                for widget in F10.winfo_children():
                    widget.destroy()
                Data=mysql.connector.connect(host=var1.get(),user=var2.get(),password=var3.get(),database=combobox_var0.get())
                cursor=Data.cursor()
                cursor.execute(' describe {}'.format(combobox_var4.get()))  
                scrol2=Scrollbar(F10,orient=VERTICAL,width=15,)
                scrol2.place(x=642,y=1,height=401)
                scrol1=Scrollbar(F10,orient=HORIZONTAL,width=15,)
                scrol1.place(x=1,y=387,width=640)
                tv=ttk.Treeview(F10)
                tv.place(x=1,y=0,width=640)
                tv.configure(columns=('#0','#1','#2','#3','#4','#5'),height=18,yscrollcommand=scrol1.set,xscrollcommand=scrol2.set)
                tv.column('#0',width=50)
                tv.column('#1',width=100)
                tv.column('#2',width=100)
                tv.column('#3',width=100)
                tv.column('#4',width=100)
                tv.column('#5',width=80)
                tv.column('#6',width=100)
                tv.heading('#0',text='ID')
                tv.heading('#1',text='Name')
                tv.heading('#2',text='Type')
                tv.heading('#3',text='Null')
                tv.heading('#4',text='Key')
                tv.heading('#5',text='Default')
                tv.heading('#6',text='Extra')
                scrol1.config(command=tv.yview)
                scrol2.config(command=tv.xview)
                v=1
                for row in cursor:
                    tv.insert('','end',v,text=v)
                    tv.set(v,'#1', row[0])
                    tv.set(v,'#2', row[1])
                    tv.set(v,'#3', row[2])
                    tv.set(v,'#4', row[3])
                    tv.set(v,'#5', row[4])
                    tv.set(v,'#6', row[5])
                    if row[4]== None:
                        tv.set(v,'#5', 'None')
                    v+=1
                cursor.close()
            def Tabel_Info():
                B11.config(state=DISABLED)
                B10.config(state=NORMAL)
                for widget in F10.winfo_children():
                    widget.destroy()

                Data=mysql.connector.connect(host=var1.get(),user=var2.get(),password=var3.get(),database=combobox_var0.get())
                cursor1=Data.cursor()
                cursor1.execute('select * from {}'.format(combobox_var4.get())) 
                Data1=mysql.connector.connect(host=var1.get(),user=var2.get(),password=var3.get(),database=combobox_var0.get())
                cursor2=Data1.cursor()
                cursor2.execute(' describe {}'.format(combobox_var4.get())) 
                scrol1=Scrollbar(F10,orient=VERTICAL,width=15)
                scrol1.place(x=642,y=2,height=401)
                scrol2=Scrollbar(F10,orient=HORIZONTAL,width=15)
                scrol2.place(x=1,y=387,width=640)
                list_row=[]
                for row in cursor2:
                    list_row.append(row[0])
                cursor2.close()

                tv1=ttk.Treeview(F10)
                tv1.place(x=1,y=0,width=640)
                tv1.configure(yscrollcommand=scrol1.set,xscrollcommand=scrol2.set)
                row_col=[]
                xx=0
                for row in list_row:
                    row_col.append('#{}'.format(xx))
                    xx+=1

                tv1.configure(columns=row_col,height=18)
                xx1=0
                for row in list_row:
                    tv1.column('#{}'.format(xx1),width=100)
                    tv1.heading('#{}'.format(xx1),text=row)
                    xx1+=1

                scrol1.config(command=tv1.yview)
                scrol2.config(command=tv1.xview)

                rows=row_col
                rows.pop()
                v=1
                for row in cursor1:
                    tv1.insert('','end',v,text=v)  
                    rr=1
                    for row1 in rows:
                        tv1.set(v,'#{}'.format(rr), row[rr])
                        rr+=1
                    v+=1
                    
                cursor1.close()
                cursor2.close()
            B10=Button(aa,text='Col_Table_Info',width=45,bd=1,height=2,command=Col_Tabel_Info)
            B10.place(x=4,y=1)
            B11=Button(aa,text='Table_Info',width=46,bd=1,height=2,command=Tabel_Info)
            B11.place(x=328,y=1)
            Col_Tabel_Info()
            aa.mainloop()
            
        Button_9=Button(Add_Column_Frame,command=Delete_Table,text='Delete Table',width=10,bg=background_4.get(),padx=1,pady=1,bd=1,cursor='hand2')
        Button_9.place(x=10,y=90)
        Button_10=Button(Add_Column_Frame,command=create_col,text='Add col in table',width=12,bg=background_4.get(),padx=1,pady=1,bd=1,cursor='hand2')
        Button_10.place(x=100,y=90)
        Button_11=Button(Add_Column_Frame,command=Table_Lest,text='Show Table',width=10,bg=background_4.get(),padx=1,pady=1,bd=1,cursor='hand2')
        Button_11.place(x=200,y=90)
    except:
        messagebox.showerror(title='Error',message='Connect server ferst!')
def Close_frame_1():
    create_table_frame.destroy()
def Close_frame_2():
    Add_Column_Frame.destroy()
def Call_0():
    try:
        try:
            try:
                Add_Column_Frame.destroy()
                create_table_frame.destroy()
                Create_Table()     
            except:
                create_table_frame.destroy()
                Create_Table()
        except:
            Add_Column_Frame.destroy()
            Create_Table()
    except:
        Create_Table()
def Call_1():
    try:
        try:
            try:
                create_table_frame.destroy()
                Add_Column_Frame.destroy()
                Add_Columns()                
            except:
                Add_Column_Frame.destroy()
                Add_Columns()
        except:
            create_table_frame.destroy()
            Add_Columns()
    except:
        Add_Columns() 
def sheck_connect():
    V=Vx.get()
    if V=='True':
        DB_dsconnected()
    else:
        DBconect()
def light_theme():
    l1.config(bg='#ff948c')
    window.config(bg='whitesmoke')
    l1.config(bg='#ff948c',foreground='black')
    l2.config(bg='#ff948c',foreground='black')
    l3.config(bg='#c6c6c6',foreground='black')
    l4.config(bg='#c6c6c6',foreground='black')
    l5.config(bg='#c6c6c6',foreground='black')
    l6.config(bg='#ff948c',foreground='black')
    l7.config(bg='#c6c6c6',foreground='black')
    l8.config(bg='#c6c6c6',foreground='black')
    l9.config(bg='#c6c6c6',foreground='black')
    l10.config(bg='#ff948c',foreground='black')
    l11.config(bg='whitesmoke',foreground='black')
    lib1.config(bg='#c6c6c6')
    lib2.config(bg='#c6c6c6')
    Button_1.config(bg='whitesmoke')
    Button_2.config(bg='whitesmoke')
    Button_3.config(bg='whitesmoke')
    Button_4.config(bg='whitesmoke')
    Button_5.config(bg='whitesmoke')
    Button_6.config(bg='#f4dfb4')
    Button_7.config(bg='#f4dfb4')
    background_1.set('#c6c6c6')
    background_2.set('#ff948c')
    background_3.set('Light_mode')
    background_4.set('#7ED5C5')
    Frame_1.config(bg='#c6c6c6')
    Frame_2.config(bg='#c6c6c6')   
    try:
        frame_Database.config(bg='#c6c6c6')  
    except:
        pass    
    try:
        Df('Light_mode')
    except:
        pass
    try:
        Dcol('Light_mode')
    except:
        pass
    try:
        AA('Light_mode')
    except:
        pass    
def darck_theme():
    window.config(bg='#0F1025')
    l1.config(bg='#050847',foreground='#EAECEE')
    l2.config(bg='#050847',foreground='#EAECEE')
    l3.config(bg='#383B7A',foreground='#EAECEE')
    l4.config(bg='#383B7A',foreground='#EAECEE')
    l5.config(bg='#383B7A',foreground='#EAECEE')
    l6.config(bg='#050847',foreground='#EAECEE')
    l7.config(bg='#383B7A',foreground='#EAECEE')
    l8.config(bg='#383B7A',foreground='#EAECEE')
    l9.config(bg='#383B7A',foreground='#EAECEE')
    l10.config(bg='#050847',foreground='#EAECEE')
    l11.config(bg='#0F1025',foreground='#EAECEE')
    lib1.config(bg='#383B7A')
    lib2.config(bg='#383B7A')
    Button_1.config(bg='#178082')
    Button_2.config(bg='#178082')
    Button_3.config(bg='#178082')
    Button_4.config(bg='#178082')
    Button_5.config(bg='#178082')
    Button_6.config(bg='#706693')
    Button_7.config(bg='#706693')
    background_1.set('#383B7A')
    background_2.set('#050847')
    background_3.set('Darck_mode')
    background_4.set('#178082')
    Frame_1.config(bg='#383B7A')
    Frame_2.config(bg='#383B7A')
    try:
        frame_Database.config(bg='#383B7A') 
    except:
        pass    
    try:
        Df('Darck_mode')
    except:
        pass
    try:
        Dcol('Darck_mode')
    except:
        pass   
    try:
        AA('Darck_mode')
    except:
        pass     

def Ex():
    window.quit()

#__________________________________________Menu_______________________________________________________________________

menu_bar=Menu(window)
window.config(menu=menu_bar) 
menu_1=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='file',menu=menu_1)
menu_1.add_command(label='Exit',command=Ex)
menu_1.add_command(label='Sersh')

menu_2=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label='themes',menu=menu_2)
menu_2.add_command(label='Light Theme',command=light_theme)
menu_2.add_command(label='Darck Theme',command=darck_theme)

#__________________________________________commands_______________________________________________________________________

Button_1.config(command=sheck_connect)
Button_4.config(command=DBcreate)
Button_5.config(command=Delete_Database)
Button_2.config(command=Call_0)
Button_3.config(command=Call_1)
Button_6.config(command=Close_frame_1)
Button_7.config(command=Close_frame_2)

window.mainloop()