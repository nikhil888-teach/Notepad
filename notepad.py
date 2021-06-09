from  tkinter import *
import os
import tkinter.messagebox as tsmg
from tkinter.filedialog import askopenfilename,asksaveasfilename

def help():
    a=tsmg.showinfo('Notpad','Sir ! Apko took Samy Me Email Ke Jariye Help Milegi')

def cut():
    textarea.event_generate(('<<Cut>>'))

def copy():
    textarea.event_generate(('<<Copy>>'))

def paste():
    textarea.event_generate('<<Paste>>')

def exit():
    a=tsmg.askyesno('Notpad','Are You Sure ?')
    if a==True:
        root.destroy()
    else:
        pass

def new():
    global file
    root.title('Untitled -Notpad')
    file=None
    textarea.delete(1.0,END)

def open1():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "  -Notepad")
        textarea.delete(1.0, END)
        f = open(file, encoding ="utf8")
        textarea.insert(1.0, f.read())
        f.close()
def savefile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile='Untitled.txt',defaultextension='.txt',
                       filetypes=[('All File','*.*'),('Text Document','.txt')])
        if file=='':
            file=None
        else:
            f=open(file,'w')
            f.write(textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+'-Notpad')
    else:
        f = open(file, 'w')
        f.write(textarea.get(1.0, END))
        f.close()



if __name__ == '__main__':
    root=Tk()
    root.geometry('600x600')
    root.title('Untitled -Notpad')
    root.wm_iconbitmap('notepad.ico')
    scroll=Scrollbar(root)
    scroll.pack(side=RIGHT,fill=Y)


    textarea=Text(root,font='Timesnewroman 13',undo=True,yscrollcommand=scroll.set)
    file=None
    textarea.pack(expand=True,fill=BOTH)
    scroll.config(command=textarea.yview)

    menubar=Menu(root)
    filemenu=Menu(menubar,tearoff=0)
    filemenu.add_command(label='New',command=new)
    filemenu.add_command(label='Open',command=open1)
    filemenu.add_separator()
    filemenu.add_command(label='Save',command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label='Exit',command=exit)
    root.config(menu=menubar)
    menubar.add_cascade(label='File',menu=filemenu)



    editmenu=Menu(menubar,tearoff=0)
    editmenu.add_command(label='Undo',command=textarea.edit_undo)
    editmenu.add_command(label='Redo',command=textarea.edit_redo)
    editmenu.add_separator()
    editmenu.add_command(label='Cut',command=cut)
    editmenu.add_command(label='Copy',command=copy)
    editmenu.add_command(label='Paste',command=paste)
    root.config(menu=menubar)
    menubar.add_cascade(label='Edit',menu=editmenu)

    helpmenu=Menu(menubar,tearoff=0)
    helpmenu.add_command(label='Help',command=help)
    root.config(menu=menubar)
    menubar.add_cascade(label='Help',menu=helpmenu)




    root.mainloop()


