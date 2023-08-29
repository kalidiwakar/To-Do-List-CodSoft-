from tkinter import *
from tkinter import messagebox

def  myTask():
    task= my_entry.get()
    if task!="":
        lisbox.insert(END,task)
        my_entry.delete(0,"end")
    else:
        messagebox.showwarning("warning","Enter some task")
def  deleteTask():
    lisbox.delete(ANCHOR)
window = Tk()
window.geometry('600x500+400+30')
window.title("MY TODO LIST")
window.config(bg='#1B1919')
window.resizable(width=False,height=False)

frame= Frame(window)
frame.pack(pady=10)

lisbox = Listbox(frame,width=30,height=9,font=('Bold italic',12),bd=1,fg='#D22761',selectbackground='#202526',activestyle="none",)
lisbox.pack(side=LEFT,fill=BOTH)
task_list=['GET UP']
for item in task_list:
    lisbox.insert(END,item)
scb = Scrollbar(frame)
scb.pack(side=RIGHT,fill= BOTH)

lisbox.config(yscrollcommand=scb.set)
scb.config(command=lisbox.yview)

my_entry = Entry(
    window,font=('times',24)
)
my_entry.pack(pady=20)
button_frame=Frame(window)
button_frame.pack(pady=20)

addTask_btn=Button(
    button_frame,
    text= 'ADD TASK',
    font=("times"),
    bg='#C8C8C8',
    padx=10,
    pady=10,
    command=myTask
)
addTask_btn.pack(fill=BOTH,expand=True,side=LEFT)

delTask_btn =Button(
    button_frame,
    text='DELTE TASK',
    font=("times"),
    bg='#C8C8C8',
    padx=10,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH,expand=True,side=LEFT)

window.mainloop()