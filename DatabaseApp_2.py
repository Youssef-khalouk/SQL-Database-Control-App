
from tkinter import *
from ctypes import windll
from tkinter import messagebox
import mysql.connector
from tkinter import ttk

tk_title = "Database" 
root=Tk()
root.title(tk_title) 
root.overrideredirect(True) 
root.geometry('1200x650+20+5') 
root.config(bg='#050847')
root.iconbitmap('database_ico.ico')
root.minimized = False 
root.maximized = False 
 
LGRAY = StringVar()
LGRAY.set('#3e4042')
DGRAY = StringVar()
DGRAY.set('#050847') 
RGRAY = StringVar()
RGRAY.set('#10121f')
FGRAY = StringVar()
FGRAY.set('white')

title_bar = Frame(root, bg=RGRAY.get(), relief='raised', bd=0,highlightthickness=0)

def set_appwindow(mainWindow): 
    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    WS_EX_TOOLWINDOW = 0x00000080
    # Magic
    hwnd = windll.user32.GetParent(mainWindow.winfo_id())
    stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    stylew = stylew & ~WS_EX_TOOLWINDOW
    stylew = stylew | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
    mainWindow.wm_withdraw()
    mainWindow.after(10, lambda: mainWindow.wm_deiconify())

def minimize_me():
    root.attributes("-alpha",0) 
    root.minimized = True       
def deminimize(event):
    if root.minimized == True:
        root.minimized = False                              
        root.focus() 
        root.attributes("-alpha",1) 
def maximize_me():
    if root.maximized == False: 
        root.normal_size = root.geometry()
        expand_button.config(text=" 🗗 ")
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
        root.maximized = not root.maximized 
        
    else:
        expand_button.config(text=" 🗖 ")
        root.geometry(root.normal_size)
        root.maximized = not root.maximized
       
Var10=BooleanVar()
Var11=BooleanVar()
Var12=BooleanVar()
Var13=BooleanVar()
Var10.set(True)
Var11.set(True)
Var12.set(True)
Var13.set(True)
Menubar_color1=StringVar()
Menubar_color2=StringVar()
Menubar_color3=StringVar()
Menubar_color1.set('#252928')
Menubar_color2.set('#254928')
Menubar_color3.set('black')

def Minu_Frame():
    TT.config(bg=LGRAY.get(),fg='blue')
    TT1.config(bg=RGRAY.get(),fg=FGRAY.get())
    TT2.config(bg=RGRAY.get(),fg=FGRAY.get())  
    Var11.set(False)
    Var12.set(True)
    Var13.set(True)
    var01.set(1)
    global Frame01
    try:
        Frame01.destroy()
    except:
        pass 
    def Qt():
        root.quit()
    Frame01=Frame(root,bd=0,bg=Menubar_color1.get(),highlightbackground='blue',highlightthickness=1)
    Frame01.place(x=37,y=24)
    B1=Button(Frame01,bg=Menubar_color1.get(),text='  New text file',anchor=W,bd=0,cursor='hand2',width=25)
    B1.pack(padx=1,pady=3)
    B2=Button(Frame01,bg=Menubar_color1.get(),text='  New file',anchor=W,bd=0,cursor='hand2',width=25)
    B2.pack(padx=1,pady=3)
    B3=Button(Frame01,bg=Menubar_color1.get(),text='  New window',anchor=W,bd=0,cursor='hand2',width=25)
    B3.pack(padx=1,pady=3)
    Frame(Frame01,width=140,height=1,bg='blue').pack()
    B4=Button(Frame01,bg=Menubar_color1.get(),text='  Exit',anchor=W,bd=0,cursor='hand2',width=25,command=Qt)
    B4.pack(padx=1,pady=3)

    def Fook(event):
        B1.config(bg=Menubar_color2.get(),fg='blue')
    def Taht(event):
        B1.config(bg=Menubar_color1.get(),fg=Menubar_color3.get())    
    def Fook1(event):
        B2.config(bg=Menubar_color2.get(),fg='blue')
    def Taht1(event):
        B2.config(bg=Menubar_color1.get(),fg=Menubar_color3.get())
    def Fook2(event):
        B3.config(bg=Menubar_color2.get(),fg='blue')
    def Taht2(event):
        B3.config(bg=Menubar_color1.get(),fg=Menubar_color3.get())
    def Fook3(event):
        B4.config(bg='red',fg='blue')
    def Taht3(event):
        B4.config(bg=Menubar_color1.get(),fg=Menubar_color3.get())
       
    B1.bind('<Enter>',Fook)
    B1.bind('<Leave>',Taht)
    B2.bind('<Enter>',Fook1)
    B2.bind('<Leave>',Taht1)
    B3.bind('<Enter>',Fook2)
    B3.bind('<Leave>',Taht2)
    B4.bind('<Enter>',Fook3)
    B4.bind('<Leave>',Taht3)

def Minu_Frame1():
    TT1.config(bg=LGRAY.get(),fg='blue')
    TT.config(bg=RGRAY.get(),fg=FGRAY.get())
    TT2.config(bg=RGRAY.get(),fg=FGRAY.get())
    Var11.set(True)
    Var13.set(True)
    Var12.set(False)
    global Frame02
    try:
        Frame02.destroy()
    except:
        pass
    var02.set(1)
    Frame02=Frame(root,bd=0,bg=Menubar_color1.get(),highlightbackground='blue',highlightcolor='red',highlightthickness=1)
    Frame02.place(x=72,y=24)
    B1=Button(Frame02,text='  Light Mode',anchor=W,bg=Menubar_color1.get(),bd=0,cursor='hand2',width=25,command=light_theme)
    B1.pack(padx=1,pady=3)
    B2=Button(Frame02,text='  Darck Mode',anchor=W,bg=Menubar_color1.get(),bd=0,cursor='hand2',width=25,command=darck_theme)
    B2.pack(padx=1,pady=3)
    
    def Fook(event):
        B1.config(bg=Menubar_color2.get(),fg='blue')
    def Taht(event):
        B1.config(bg=Menubar_color1.get(),fg=Menubar_color3.get())     
    def Fook1(event):
        B2.config(bg=Menubar_color2.get(),fg='blue')
    def Taht1(event):
        B2.config(bg=Menubar_color1.get(),fg=Menubar_color3.get())
    B1.bind('<Enter>',Fook)
    B1.bind('<Leave>',Taht)
    B2.bind('<Enter>',Fook1)
    B2.bind('<Leave>',Taht1)



def Minu_Frame2():
    TT2.config(bg=LGRAY.get(),fg='blue')
    TT.config(bg=RGRAY.get(),fg=FGRAY.get())
    TT1.config(bg=RGRAY.get(),fg=FGRAY.get())
    Var11.set(True)
    Var12.set(True)
    Var13.set(False)
    var03.set(1)
    global Frame03
    try:
        Frame03.destroy()
    except:
        pass
    var03.set(1)
    Frame03=Frame(root,bd=0,bg=Menubar_color1.get(),highlightbackground='blue',highlightcolor='red',highlightthickness=1)
    Frame03.place(x=130,y=24)
    B100=Button(Frame03,text='  About Us',anchor=W,bg=Menubar_color1.get(),bd=0,cursor='hand2',width=25)
    B100.pack(padx=1,pady=3)
    B200=Button(Frame03,text='  Get Same infermation',anchor=W,bg=Menubar_color1.get(),bd=0,cursor='hand2',width=25)
    B200.pack(padx=1,pady=3)
    
    def Fook(event):
        B100.config(bg=Menubar_color2.get(),fg='blue')
    def Taht(event):
        B100.config(bg=Menubar_color1.get(),fg=Menubar_color3.get())     
    def Fook1(event):
        B200.config(bg=Menubar_color2.get(),fg='blue')
    def Taht1(event):
        B200.config(bg=Menubar_color1.get(),fg=Menubar_color3.get())
    B100.bind('<Enter>',Fook)
    B100.bind('<Leave>',Taht)
    B200.bind('<Enter>',Fook1)
    B200.bind('<Leave>',Taht1)



var01=StringVar()
var02=StringVar() 
var03=StringVar()
def Call_Minu():
    var=var01.get()
    if var=='':
        Minu_Frame()
        Var10.set(False)
    else:
        Frame01.destroy()
        TT.config(bg=RGRAY.get(),fg=FGRAY.get())   
        var01.set('')
        var02.set('')
        var03.set('') 
        Var10.set(True)
        Var11.set(True)
def Call_Minu1():
    var1=var02.get()
    if var1=='':
        Minu_Frame1()
        Var10.set(False)
    else:
        Frame02.destroy()
        TT1.config(bg=RGRAY.get(),fg=FGRAY.get())
        var01.set('')
        var02.set('')
        var03.set('')
        Var10.set(True)
        Var12.set(True)

def Call_Minu2():
    var1=var03.get()
    if var1=='':
        Minu_Frame2()
        Var10.set(False)
    else:
        Frame03.destroy()
        TT2.config(bg=RGRAY.get(),fg=FGRAY.get())
        var01.set('')
        var02.set('')
        var03.set('')
        Var10.set(True)
        Var13.set(True)

def fon(event):
    checkvar=var01.get()
    checkvar1=var02.get()
    checkvar2=var03.get()

    if checkvar != '':
        Frame01.destroy()
        TT.config(bg=RGRAY.get(),fg=FGRAY.get())
        Var11.set(True)
        var01.set('')
        Var10.set(True)
    if checkvar1 != '':
        Frame02.destroy()
        TT1.config(bg=RGRAY.get(),fg=FGRAY.get())
        var02.set('')
        Var10.set(True)
        Var12.set(True)
    if checkvar2 != '':
        Frame03.destroy()
        TT2.config(bg=RGRAY.get(),fg=FGRAY.get())
        var03.set('')
        Var10.set(True)
        Var13.set(True)

close_button = Button(title_bar, text='〤',font=(12), command=root.destroy,bg=RGRAY.get(),padx=2,bd=0,fg='white')
expand_button = Button(title_bar, text='🗖', command=maximize_me,bg=RGRAY.get(),padx=2,bd=0,fg='white')
minimize_button = Button(title_bar, text='--',command=minimize_me,bg=RGRAY.get(),padx=2,bd=0,fg='white')
image2=PhotoImage(file='Untitled.png')
image3=PhotoImage(file='Untitled1.png')
title_bar_title = Label(title_bar, image=image3,bd=0, bg=RGRAY.get(),fg='white')
TT = Button(title_bar, text='File',command=Call_Minu,bg=RGRAY.get(),padx=2,pady=2,bd=0,fg='White')
TT1 = Button(title_bar, text='Theme',command=Call_Minu1,bg=RGRAY.get(),padx=2,pady=2,bd=0,fg='White')
TT2 = Button(title_bar, text='Help',command=Call_Minu2,bg=RGRAY.get(),padx=2,pady=2,bd=0,fg='White')
title_bar_title1 = Label(title_bar, text='_Database_Control_',bd=0, bg=RGRAY.get(),fg='white')

title_bar.pack(fill=X)
close_button.pack(side=RIGHT,ipadx=8,ipady=0)
expand_button.pack(side=RIGHT,ipadx=10,ipady=3)
minimize_button.pack(side=RIGHT,ipadx=10,ipady=3)
title_bar_title.pack(side=LEFT, padx=5)
TT.pack(side=LEFT, padx=5)
TT1.pack(side=LEFT, padx=5)
TT2.pack(side=LEFT, padx=5)
title_bar_title1.pack( pady=5)

def changex_on_hovering(event):
    close_button['bg']='red'
def returnx_to_normalstate(event):
    close_button['bg']=RGRAY.get()
def change_size_on_hovering(event):  
    expand_button['bg']=LGRAY.get()
def return_size_on_hovering(event):
    expand_button['bg']=RGRAY.get() 
def changem_size_on_hovering(event):
    minimize_button['bg']=LGRAY.get()
def returnm_size_on_hovering(event):
    minimize_button['bg']=RGRAY.get()
def changem_size_on_hovering1(event):
    TT['bg']=LGRAY.get()
    TT['fg']='blue'
    v=Var10.get()
    if not v:
        try:
            Frame02.destroy()
            Minu_Frame()
        except:
            pass     
        try:
            Frame03.destroy()
            Minu_Frame()
        except:
            pass
def returnm_size_on_hovering1(event):
    vaar=Var11.get()
    if vaar == True :
        TT['bg']=RGRAY.get()
        TT['fg']=FGRAY.get()
    else:
        pass
def changem_size_on_hovering2(event):
    TT1['bg']=LGRAY.get()
    TT1['fg']='blue'
    v=Var10.get()
    if not v:
        try:
            Frame01.destroy()
            Minu_Frame1()
        except:
            pass     
        try:
            Frame03.destroy()
            Minu_Frame1()
        except:
            pass
def returnm_size_on_hovering2(event):
    vaar1=Var12.get()
    if vaar1 == True:
        TT1['bg']=RGRAY.get()
        TT1['fg']=FGRAY.get()
    else:
        pass
def changem_size_on_hovering3(event):
    TT2['bg']=LGRAY.get()
    TT2['fg']='blue'
    v=Var10.get()
    if not v:
        try:
            Frame01.destroy()
            Minu_Frame2()
        except:
            pass     
        try:
            Frame02.destroy()
            Minu_Frame2()
        except:
            pass
def returnm_size_on_hovering3(event):
    vaar1=Var13.get()
    if vaar1 == True:
        TT2['bg']=RGRAY.get()
        TT2['fg']=FGRAY.get()
    else:
        pass

def get_pos(event): 
    if root.maximized == False:
        xwin = root.winfo_x()
        ywin = root.winfo_y()
        startx = event.x_root
        starty = event.y_root
        ywin = ywin - starty
        xwin = xwin - startx

        def move_window(event): 
            root.config(cursor="fleur")
            root.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')
        def release_window(event): 
            root.config(cursor="arrow")    
            
        title_bar.bind('<B1-Motion>', move_window)
        title_bar.bind('<ButtonRelease-1>', release_window)
        title_bar_title.bind('<B1-Motion>', move_window)
        title_bar_title.bind('<ButtonRelease-1>', release_window)
    else:
        expand_button.config(text=" 🗖 ")
        root.maximized = not root.maximized
        expand_button.config(text=" 🗖 ")
        root.geometry(root.normal_size)
       
title_bar.bind('<Button-1>', get_pos)
title_bar_title.bind('<Button-1>', get_pos) 
close_button.bind('<Enter>',changex_on_hovering)
close_button.bind('<Leave>',returnx_to_normalstate)
expand_button.bind('<Enter>', change_size_on_hovering)
expand_button.bind('<Leave>', return_size_on_hovering)
minimize_button.bind('<Enter>', changem_size_on_hovering)
minimize_button.bind('<Leave>', returnm_size_on_hovering)

TT.bind('<Enter>', changem_size_on_hovering1)
TT.bind('<Leave>', returnm_size_on_hovering1)
TT1.bind('<Enter>', changem_size_on_hovering2)
TT1.bind('<Leave>', returnm_size_on_hovering2)
TT2.bind('<Enter>', changem_size_on_hovering3)
TT2.bind('<Leave>', returnm_size_on_hovering3)

root.bind("<FocusIn>",deminimize)
root.after(10, lambda: set_appwindow(root)) 

# ========================================================================================================================

window=Frame(root,bg='#0F1025')
window.place(x=2,y=28,width=1300,height=662)
window.bind("<ButtonRelease-1>",fon) 

#__________________________________________Frames__________________________________________________________

Frame_1=Frame(window,background='#383B7A',width=304,height=625,highlightbackground='blue',highlightcolor='red',highlightthickness=1)
Frame_1.place(x=5,y=35)
Frame_2=Frame(window,background='#383B7A',width=304,height=200,highlightbackground='blue',highlightcolor='red',highlightthickness=1)
Frame_2.place(x=315,y=35)
Frame_1.bind("<ButtonRelease-1>",fon) 
Frame_2.bind("<ButtonRelease-1>",fon) 

#__________________________________________Labels_________________________________________________________

l1=Label(window,text='Database',background='#050847',foreground='#EAECEE',font=('tajawal',15,'bold'))
l1.pack(fill=X)

                               #===========Frame_1============
l2=Label(Frame_1,text='Connect Database',width=42,background='#050847',foreground='#EAECEE') 
l2.place(x=0,y=0)
l3=Label(Frame_1,text='Server Name :',width=11,anchor=E,background='#383B7A',foreground='#EAECEE')
l3.place(x=5,y=30)
l4=Label(Frame_1,text='User :',width=11,anchor=E,background='#383B7A',foreground='#EAECEE')
l4.place(x=5,y=60)
l5=Label(Frame_1,text='password :',width=11,anchor=E,background='#383B7A',foreground='#EAECEE')
l5.place(x=5,y=90)
lib1=Label(Frame_1,text='',background='#383B7A')
lib1.place(x=5,y=140)
lib2=Label(Frame_1,text='[Vide]',background='#383B7A')
lib2.place(x=130,y=200)

                               #===========Frame_2============
l6=Label(Frame_2,text='Create Database',width=42,background='#050847',foreground='#EAECEE')
l6.place(x=0,y=0)
l7=Label(Frame_2,text=' DB Name :',background='#383B7A',foreground='#EAECEE')
l7.place(x=5,y=30)
l8=Label(Frame_2,text='Table cols :',background='#383B7A',foreground='#EAECEE')
l8.place(x=5,y=130)
l9=Label(Frame_2,text='  Add cols :',background='#383B7A',foreground='#EAECEE')
l9.place(x=5,y=160)
l10=Label(Frame_1,text='Database Founds',width=42,background='#050847',foreground='#EAECEE')
l10.place(x=0,y=175)

image1=PhotoImage(file='database.png',width=700,height=630)
l11=Label(window,image=image1,background='#0F1025',foreground='#EAECEE')
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

                               #===========Frame_2============
Entry_10=StringVar()                               
Entry_4=Entry(Frame_2,justify='center',textvariable=Entry_10,bd=1)
Entry_4.place(x=90,y=30)

#__________________________________________Buttons_________________________________________________________
                               #===========Frame_1============
Button_1=Button(Frame_1,text='Connect',height=3,bd=1,cursor='hand2',bg='#178082')
Button_1.place(x=220,y=42)

                               #===========Frame_2============
Button_2=Button(Frame_2,text='Create Table',width=15,bd=1,cursor='hand2',bg='#178082')
Button_2.place(x=100,y=130)
Button_3=Button(Frame_2,text='Add Columns',width=15,bd=1,cursor='hand2',bg='#178082')
Button_3.place(x=100,y=160)
Button_4=Button(Frame_2,text='Create',background='#178082',bd=1,cursor='hand2',width=10,bg='whitesmoke')
Button_4.place(x=160,y=70)
Button_5=Button(Frame_2,text='Delete',background='#178082',bd=1,cursor='hand2',width=10,bg='whitesmoke')
Button_5.place(x=70,y=70)
Button_6=Button(Frame_2,text='Hide',background='#706693',bd=1,cursor='hand2',foreground='blue',width=7)
Button_6.place(x=240,y=130)
Button_7=Button(Frame_2,text='Hide',background='#706693',bd=1,cursor='hand2',foreground='blue',width=7)
Button_7.place(x=240,y=160)

#__________________________________________Fonctions_________________________________________________________

global background_1
background_1=StringVar()
background_2=StringVar()
background_3=StringVar()
background_4=StringVar()
background_1.set('#383B7A')
background_2.set('#050847')
background_4.set('#178082')
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
        create_table_frame=Frame(window,background=background_1.get(),highlightbackground='blue',highlightcolor='red',highlightthickness=1)
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
        Add_Column_Frame=Frame(window,background=background_1.get(),highlightbackground='blue',highlightcolor='red',highlightthickness=1)
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
                tv.heading('#1',text='Field')
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
    try:
        create_table_frame.destroy()
    except:
        pass
def Close_frame_2():
    try:
        Add_Column_Frame.destroy()
    except:
        pass
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
    root.config(bg='whitesmoke')
    Call_Minu1()
    title_bar.config(bg='white')
    title_bar_title1.config(bg='white',fg='black')
    title_bar_title.config(image=image2)
    close_button.config(bg='white',fg='black')
    expand_button.config(bg='white',fg='black')
    minimize_button.config(bg='white',fg='black')
    LGRAY.set('#F2F3F4')
    RGRAY.set('white')
    DGRAY.set('white')
    FGRAY.set('black')
    TT.config(bg='white',fg='black')
    TT1.config(bg='white',fg='black')
    TT2.config(bg='white',fg='black')
    Menubar_color1.set('white')
    Menubar_color2.set('#F2F3F4')
    Menubar_color3.set('black')
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
    Call_Minu1()
    root.config(bg='#050847')
    title_bar.config(bg='#10121f')
    title_bar_title1.config(bg='#10121f',fg='white')
    title_bar_title.config(image=image3)
    close_button.config(bg='#10121f',fg='white')
    expand_button.config(bg='#10121f',fg='white')
    minimize_button.config(bg='#10121f',fg='white')
    LGRAY.set('#3e4042')
    RGRAY.set('#10121f')
    DGRAY.set('#050847')
    FGRAY.set('white')
    TT.config(bg='#10121f',fg='white')
    TT1.config(bg='#10121f',fg='white')
    TT2.config(bg='#10121f',fg='white')
    Menubar_color1.set('#252928')
    Menubar_color2.set('#254928')
    Menubar_color3.set('black')
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
#__________________________________________commands_______________________________________________________________________

Button_1.config(command=sheck_connect)
Button_4.config(command=DBcreate)
Button_5.config(command=Delete_Database)
Button_2.config(command=Call_0)
Button_3.config(command=Call_1)
Button_6.config(command=Close_frame_1)
Button_7.config(command=Close_frame_2)

# ========================================================================================================================
root.mainloop()