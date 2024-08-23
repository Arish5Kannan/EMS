from customtkinter import *
from PIL  import Image
from tkinter import messagebox
root = CTk()
root.geometry("930x478")
root.resizable(0,0)
root.title("Login page")
# root.state("zoomed")
image =  CTkImage(Image.open('login.jpg'),size=(930,478))
imglab = CTkLabel(root,image=image,text='')
imglab.place(x=0,y=0)
txtlabel = CTkLabel(root,text="Employee Management System",font=("Times New Roman",29,"bold"),bg_color='#FFFFFF')
txtlabel.place(x=180,y=50)
def login():
    if txtentry.get()=='' or txtentry1.get()=='':
        messagebox.showerror('Error','All Fields are required')
        txtentry.delete(0, END)
        txtentry1.delete(0, END)
    elif  txtentry.get()=='Arish' or txtentry1.get()=='AK@2006' :
        messagebox.showinfo('Success', 'Logined Successfully !')
        root.destroy()
        import ems
    else:
        messagebox.showerror('Error', 'Wrong Credentials')
        txtentry.delete(0, END)
        txtentry1.delete(0, END)
txtentry = CTkEntry(root,placeholder_text="Enter your name",width=230,height=35,font=("Times New Roman",19))
txtentry.place(x=180,y=110)
txtentry1 = CTkEntry(root,placeholder_text="Enter your Password",width=230,height=35,show="*",font=("Times New Roman",19))
txtentry1.place(x=180,y=170)
txtbutton = CTkButton(root,command=login,text='Login',cursor='hand2',width=160,height=38,font=('Arial',16,'bold'))
txtbutton.place(x=220,y=220)
root.mainloop()