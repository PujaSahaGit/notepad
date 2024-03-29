from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled-Notepad")
    file= None
    TextArea.delete(1.0,END)
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"),("Textdocuments","*.txt")])
    if file =="":
        file=None
    else:
        root.title(os.path.basname(file)+ "-Notepad")
        TextArea.delete(1.0, END)
    f=open(file,"r")
    TextArea.insert(1.0,f.read())
    f.close()

def saveFile():
    global file
    if file==none:
        file=asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files","*.*"),("Textdocuments","*.txt")])
        if file=="":
            file=None

        else:
            f=open(file ,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file) + "-Notepad")
            print("File Saved")
    else:
        f=open(file ,"w")
        f.write(TextArea.get(1.0,END))
        f.close()


def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad" , "Notepad by Puja")

if __name__ == '__main__':
    root=Tk()
    root.title("Untitled-Notepad")
    #root.wm_iconbitmap("android-chrome-512x512.png")
    root.geometry("644x788")
    TextArea=Text(root , font="lucida 13")
    file=None
    TextArea.pack(expand=True, fill=BOTH)
    MenuBar=Menu(root)
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label="New", command=newFile)

    #To Open already existing file
    FileMenu.add_command(label="Open", command = openFile)

    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    MenuBar.add_cascade(label = "File", menu=FileMenu)

    Editmenu=Menu(MenuBar, tearoff=0)
    
    Editmenu.add_command(label="Cut", command=cut)
    Editmenu.add_command(label="Copy", command=copy)
    Editmenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit" , menu=Editmenu)


    Helpmenu=Menu(MenuBar, tearoff=0)
    Helpmenu.add_command(label="About Notepad",command=about)
    MenuBar.add_cascade(label="Help" , menu=Helpmenu)
    
    

    root.config(menu=MenuBar)
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT , fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    root.mainloop()