from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import Database
window = CTk()
window.title("Employee Management System")
window.configure(fg_color='#040e2e')
window.geometry("1080x700+100+0")
window.resizable(0,0)
imgl = CTkImage(Image.open('banner.jpeg'),size=(300,177))
img = CTkLabel(window,text='',image=imgl)
img.grid(row=0,column=0)
imgl2 = CTkImage(Image.open('banner4.jpeg'),size=(409,177))
img2 = CTkLabel(window,text='',image=imgl2)
img2.grid(row=0,column=1)
imgl1 = CTkImage(Image.open('banner1.jpeg'),size=(376,177))
img1 = CTkLabel(window,text='',image=imgl1)
img1.grid(row=0,column=2)
leftframe = CTkFrame(window,fg_color='#040e2e')
leftframe.grid(row=1,column=0)
idlabel = CTkLabel(leftframe,text='Id',font=("Times NewRoman",18,"bold"),text_color='white')
idlabel.grid(row=2,column=0,padx=(10),pady=20,sticky='w')
identry = CTkEntry(leftframe,font=("Times NewRoman",17),width=180,height=35)
identry.grid(row=2,column=1,padx=(10,0),pady=20,sticky='w')
namelabel = CTkLabel(leftframe,text='Name',font=("Times NewRoman",18,"bold"),text_color='white')
namelabel.grid(row=3,column=0,padx=(10),pady=20,sticky='w')
nameentry = CTkEntry(leftframe,font=("Times NewRoman",17),width=180,height=35)
nameentry.grid(row=3,column=1,padx=(10,0),pady=20,sticky='w')
phonelabel = CTkLabel(leftframe,text='Phone',font=("Times NewRoman",18,"bold"),text_color='white')
phonelabel.grid(row=4,column=0,padx=(10),pady=20,sticky='w')
phoneEntry = CTkEntry(leftframe,font=("Times NewRoman",17),width=180,height=35)
phoneEntry.grid(row=4,column=1,padx=(10,0),pady=20,sticky='w')
rolelabel = CTkLabel(leftframe,text='Role',font=("Times NewRoman",18,"bold"),text_color='white')
rolelabel.grid(row=5,column=0,padx=(10),pady=20,sticky='w')
values = ['Web developer','App developer','Backend developer','Frontend developer','Network Engineer','Software developer','UI/UX designer','Python developer']
roleEntry = CTkComboBox(leftframe,font=("Times NewRoman",17),width=180,values=values,state='readonly',height=35)
roleEntry.grid(row=5,column=1,padx=(10,0),pady=20,sticky='w')
roleEntry.set(values[0])
Genderlabel = CTkLabel(leftframe,text='Gender',font=("Times NewRoman",18,"bold"),text_color='white')
Genderlabel.grid(row=6,column=0,padx=(10),pady=20,sticky='w')
GenderEntry = CTkComboBox(leftframe,font=("Times NewRoman",17),height=35,width=180,values=['Male','Female'],state='readonly')
GenderEntry.grid(row=6,column=1,padx=(10,0),pady=20,sticky='w')
GenderEntry.set('Male')
sallabel = CTkLabel(leftframe,text='Salary',font=("Times NewRoman",18,"bold"),text_color='white')
sallabel.grid(row=7,column=0,padx=(10),pady=20,sticky='w')
salEntry = CTkEntry(leftframe,font=("Times NewRoman",17),width=180,height=35)
salEntry.grid(row=7,column=1,padx=(10,0),pady=20,sticky='w')
rhightframe = CTkFrame(window)
rhightframe.grid(row=1,column=1,columnspan=18,pady=(5,0))
search = ['Id','Name','Role','Salary','Gender','Phone']
#rightframe methods
def  showAll():
    displayall()
    searchBox.set('Search By')
    searchEntry.delete(0,END)
def search_employee():
    if searchEntry.get() == "":
        messagebox.showerror('Error','Give value to search')
    elif searchBox.get() == 'Search By':
        messagebox.showerror('Error','please select category')
    else:
        res = Database.search(searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        if not res:
            messagebox.showinfo('Oops','No search matched')
        for e in res:
            tree.insert('',END,values=e)
searchBox = CTkComboBox(rhightframe,values=search,width=150,height=40,font=('Arial',17))
searchBox.set('Search By')
searchBox.grid(row=0,column=0,padx=(10),pady=10)
searchEntry = CTkEntry(rhightframe,width=150,height=40,font=('Arial',17))
searchEntry.grid(row=0,column=1,padx=(10),pady=10)
searchButton = CTkButton(rhightframe,text='Search',width=180,height=40,font=('Arial',17),command=search_employee,cursor='hand2')
searchButton.grid(row=0,column=2,padx=(10),pady=10)
searchAll = CTkButton(rhightframe,text='Show All',width=180,height=40,font=('Arial',17),cursor='hand2',command=showAll)
searchAll.grid(row=0,column=3,padx=(10),pady=10)
tree = ttk.Treeview(rhightframe,height=13)
tree.grid(row=1,column=0,columnspan=6)
tree['columns'] = ('Id','Name','Phone','Role','Gender','Salary')
tree.heading('Id',text='ID')
tree.heading('Name',text='Name')
tree.heading('Phone',text='Phone')
tree.heading('Role',text='Role')
tree.heading('Gender',text='Gender')
tree.heading('Salary',text='Salary')
tree.configure(show='headings')
tree.column('Id',width=60)
tree.column('Name',width=170)
tree.column('Phone',width=150)
tree.column('Role',width=190)
tree.column('Gender',width=80)
tree.column('Salary',width=110)
sty = ttk.Style()
sty.configure('Treeview.Heading',font=("Arial",12,'bold'))
sty.configure('Treeview',font=('Arial',12,'bold'),rowheight=25,background ='#040e2e',foreground='white')
scroll = ttk.Scrollbar(rhightframe,orient=VERTICAL,command=tree.yview)
scroll.grid(row=1,column=4,sticky='NS')
tree.configure(yscrollcommand=scroll.set)
#methods

def add_employee():
    if identry.get() == '' or nameentry.get() == '' or phoneEntry.get() == '' or roleEntry.get() == '' or salEntry.get() == '' or GenderEntry.get() == '':
        messagebox.showerror('Error','All fields cannot be empty')
    elif Database.id_exist(identry.get()):
        messagebox.showerror('Error','id already exist')  
        identry.delete(0,END)  
    else:
        Database.insert(identry.get() , nameentry.get() , phoneEntry.get() , roleEntry.get() , GenderEntry.get() , salEntry.get())
        messagebox.showinfo("SUCCESS",'Employee Added .....') 
        clearall()
        displayall()
def update_employee():
    selected = tree.selection()
    if not selected:
        messagebox.showerror('Error','No rows are selected')   
    else:
        Database.update(identry.get(),nameentry.get(),phoneEntry.get(),roleEntry.get(),GenderEntry.get(),salEntry.get()) 
        clearall()
        displayall()


def displayall():
    tree.delete(*tree.get_children())
    for row in Database.fetch():
        tree.insert('',END,values=row)
def delete_employee():
    selected = tree.selection()
    if selected:
        row = tree.item(selected)['values']
        Database.delete(row[0])
        clearall()
        displayall() 
    else:
        messagebox.showerror('ERROR','No rows are selected...')           
def clearall(value=False):
    if value:
        tree.selection_remove(tree.focus())
    identry.delete(0,END)     
    roleEntry.set("Web developer")
    phoneEntry.delete(0,END)
    nameentry.delete(0,END)   
    salEntry.delete(0,END)
    GenderEntry.set('Male')
def selection(event):
    selected = tree.selection()
    if selected:
        row = tree.item(selected)['values']
        clearall()
        identry.insert(0,row[0])
        nameentry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        roleEntry.set(row[3])
        GenderEntry.set(row[4])
        salEntry.insert(0,row[5])
def deleteAll():
    res = messagebox.askyesnocancel('Confirmation','Do you want to continue?')
    Database.delete_all(res)
    displayall()

Buttonframe = CTkFrame(window,fg_color='#040e2e')
Buttonframe.grid(row=2,column=0,columnspan=6,sticky='w')
b1 = CTkButton(Buttonframe,width=170,height=38,font=("Arial",17),corner_radius=17,text='New Employee',command=lambda:clearall(True),cursor='hand2')
b1.grid(row=0,column=0,padx=(15,35),pady=20)
b2 = CTkButton(Buttonframe,width=170,height=38,font=("Arial",17),corner_radius=17,command=add_employee,text='Add Employee',cursor='hand2')
b2.grid(row=0,column=1,padx=(0,35),pady=20)
b5 = CTkButton(Buttonframe,width=170,height=38,font=("Arial",17),corner_radius=17,text='Update Employee',command=update_employee,cursor='hand2')
b5.grid(row=0,column=2,padx=(0,35),pady=20)
b3 = CTkButton(Buttonframe,width=170,height=38,font=("Arial",17),corner_radius=17,text='Delete Employee',command=delete_employee,cursor='hand2')
b3.grid(row=0,column=3,padx=(0,35),pady=20)
b4 = CTkButton(Buttonframe,width=170,height=38,font=("Arial",17),corner_radius=17,text='Delete All',cursor='hand2',command=deleteAll)
b4.grid(row=0,column=4,padx=(0,35),pady=20)
window.bind('<ButtonRelease>',selection)
displayall()
window.mainloop()