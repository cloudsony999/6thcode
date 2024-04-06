from tkinter import *


w=Tk()


w.title('MY GUI...')

def tog():
    if w.cget('bg')=='yellow':
        w.configure(bg='gray')
    else:
        w.configure(bg='yellow')


b=Button(w,text='Click Me for exit!!!',command=exit)
b2=Button(w,text='Click Me for color!!!',command=tog)




b.pack(padx=120,pady=40)
b2.pack(padx=120,pady=40)

w.mainloop()




