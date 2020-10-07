from tkinter import *
from tkinter import Listbox
from tkinter import END


# functions..

def add(text):
    global entry
    lt.insert(END,text)
    entry.delete(0,END)


def remove():
    lt.delete(lt.curselection())

def text_into():
    obj=lt.curselection()
    for i in obj:
        temp=lt.get(i)
        with open ('todolist.txt','a') as new:
            new.write(temp)
            new.write('\n')

root=Tk()
# title of the page..
root.title('make your TO -DO - List')
# label of our app
label=Label(root,text='List out your things...')
label.pack()

# listbox of our app
lt=Listbox(root,width=50,borderwidth=10)
lt.pack()

# buttons
entry=Entry(root,width=50,borderwidth=5)
entry.pack()
add_button=Button(root,text='Add',command= lambda: add(entry.get()))
remove_button=Button(root,text='remove',command=remove)
add_button.pack()
remove_button.pack()
into_text=Button(root,text='.txt',command=text_into)
into_text.pack()

root.mainloop()

