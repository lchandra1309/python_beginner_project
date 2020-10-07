from tkinter import *
from random import *
from tkinter import messagebox

com_guess=randint(1,10)
print(com_guess)
chances=0
def guess(num):
    global chances
    if num > com_guess:
        messagebox.showwarning('Wrong','You guessed too high')
    elif num< com_guess:
        messagebox.showerror('poor','too low')
    else:
        messagebox.showinfo('Winner','you guessed right')
        root.quit()
    chances+=1
    if chances>=3:
        messagebox.showinfo('LOSE THE GAME','BETTER LUCK NEXT TIME')
        root.quit()       

root=Tk()
root.title('guessing game')
label=Label(root,text='Guess any number between 1 and 10')
label.pack()
entry=Entry(root,width=35,borderwidth=10)
entry.pack()
button=Button(root,text='Click me',command=lambda: guess(int(entry.get())))
button.pack()

root.mainloop()