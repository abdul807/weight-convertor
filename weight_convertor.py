from tkinter import *
from tkinter import ttk



def calculate(*args):
    try:
        value=float(feet.get())
        meters.set((0.3048 * value * 10000 + 0.5)/10000)
    except ValueError:
        pass

root=Tk()

root.title('weight convertor')
mainframe=ttk.Frame(root)
mainframe.grid(column=0,row=0,sticky=('N,W,E,S'))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)


feet=StringVar()
meters=StringVar()

feet_entry=Entry(mainframe,width=7,textvariable=feet)
feet_entry.grid(column=2,row=1,sticky=(W,E))
feet_entry.focus()

ttk.Label(mainframe,textvariable=meters).grid(column=2,row=2,sticky=(N,W))
ttk.Button(mainframe,text='calculate',command=calculate).grid(column=3,row=3,sticky=W)




ttk.Label(mainframe,text='FEET').grid(column=3,row=1,sticky=W)
ttk.Label(mainframe,text='IS EQUIVALENT TO').grid(column=1,row=2,sticky=E)

ttk.Label(mainframe,text='METERS').grid(column=3,row=2,sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5,pady=5)

root.bind('<Return>',calculate)

root.mainloop()