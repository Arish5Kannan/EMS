import  mysql.connector
from tkinter import messagebox

def connect_database():
    global con
    global cur
    try:
         con = mysql.connector.connect(host="localhost",username="Arish",password="Arish@2004",database="Employee")
         cur = con.cursor()
    except:
        messagebox.showerror('Error','Database not connected successfully....')
        return
    cur.execute("CREATE DATABASE IF NOT EXISTS Employee;")
    cur.execute("USE Employee;")
    cur.execute("CREATE TABLE IF NOT EXISTS Data(id integer auto_increment primary key,name varchar(50),phone integer,role varchar(50),gender varchar(30),salary VARCHAR(40));")    

def insert(id,name,phone,role,gender,salary):
    try:
        sql = f"INSERT INTO Data VALUES({int(id)},'{name}','{phone}','{role}','{gender}','{salary}'); "
        cur.execute(sql)
        con.commit()
    except:
        messagebox.showerror('Error','Wrong credential...')    
        return
def fetch():
    sql = "SELECT * FROM Data;"  
    cur.execute(sql)  
    return cur.fetchall()
def id_exist(id):
    cur.execute(f"SELECT COUNT(*) FROM Data WHERE id={id}")
    res = cur.fetchone()
    return res[0] > 0   
def update(id,name,phone,role,gen,sal):
   
        cur.execute(f"UPDATE Data SET name='{name}',phone='{phone}',role='{role}',gender='{gen}',salary='{sal}' WHERE id={id}")  
        con.commit()
        messagebox.showinfo('success','Data updated successfully....')   
def delete(id):
    cur.execute(f"DELETE FROM Data WHERE id={id};")
    con.commit()
    messagebox.showinfo('success','Employee deleted successfully.....')
def search(category,value):
    cur.execute(f"SELECT * FROM Data WHERE {category} = '{value}';")
    res = cur.fetchall()
    return res
def delete_all(val):
    if val:
        cur.execute('TRUNCATE TABLE Data')
        con.commit()

        messagebox.showinfo('Success','All Data are deleted')


connect_database()
