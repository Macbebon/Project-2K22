import webbrowser
import tkinter as tk
from tkinter.messagebox import *
import mysql.connector as mysql



mycon = mysql.connect(
    host="localhost",
    user="root",
    password="",
    database="todo"
)

def link():
    webbrowser.open("https://github.com/AmanDhimanD")



def add_to_db(task):
    mycur = mycon.cursor()
    mycur.execute('INSERT INTO tasks (task) VALUES ("{}")'.format(task))
    mycon.commit()


def delete_from_dp(task):
    mycur = mycon.cursor()
    mycur.execute('DELETE FROM tasks WHERE task = "{}"'.format(task))
    mycon.commit()


def add_task():
    task = task_entry.get()
    if task != '':
        tasks_list.insert(tk.END, task)
        add_to_db(task)
        task_entry.delete(0, tk.END)
    else:
        showwarning(title='Warning', message='You must enter a task.')


def del_task():
    try:
        selection = tasks_list.curselection()[0]
        task = tasks_list.get(selection)
        delete_from_dp(task)
        tasks_list.delete(selection)
    except:
        showwarning(title='Warning', message='You must select a task.')


def load_task():
    tasks_list.delete(0, tk.END)
    mycur = mycon.cursor()
    mycur.execute('SELECT task FROM tasks')
    tasks = mycur.fetchall()
    if len(tasks) == 0:
        showwarning(title='Warning', message='No Tasks Found.')
    for task in tasks:
        tasks_list.insert(tk.END, task[0])


root = tk.Tk()
root.configure(bg='#FFFFFF')
root.title('To-Do List - # RayneCoder')
root.geometry('400x400')
# root.iconbitmap('icn.ico')

bgpic = tk.PhotoImage(file='icn.png')
bgpic = tk.Label(root, image=bgpic)
bgpic.place(x=0, y=0)

tasks_list = tk.Listbox(root, height=10, width=50, bg='#FFFFFF')
tasks_list.pack(pady=20)

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=20)

add_task_btn = tk.Button(root, text='Add Task', fg='white',
                         bg='#00FF3A', relief=tk.FLAT, command=add_task, foreground="white")
add_task_btn.pack(pady=5)

del_task_btn = tk.Button(root, text='Delete Task', fg='white',
                         bg='#FF0000', relief=tk.FLAT, command=del_task, foreground="white")
del_task_btn.pack(pady=5)

clear_task_btn = tk.Button(root, text='Clear All', fg='white',
                           bg='#6D81FF', relief=tk.FLAT, command=load_task, foreground="white")
clear_task_btn.pack(pady=5)


hyperlink = tk.Button(root, text='Github : RayneCoder', fg='Blue',command=link, font="LUCIDA 10 bold")
hyperlink.pack(pady=5,padx=10)


root.mainloop()
