import os
import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Andrupad:
    #variabel
    __main=Tk()
    __defaultWidth=600
    __defaultHeight=400
    __defaultTextArea=Text(__main)
    __defaultMenuBar=Menu(__main)
    __FileMenu=Menu(__defaultMenuBar,tearoff=0)
    __EditMenu=Menu(__defaultMenuBar,tearoff=0)
    __HelpMenu=Menu(__defaultMenuBar,tearoff=0)
    __defaultScrollbar=Scrollbar(__defaultTextArea)
    __file=None

    def __init__(self,**kwargs):
        
        #kalimat di header
        self.__main.title("Tanpajudul - Andrupad")

        #penyesuaian jendela
        WindowWidth=self.__main.winfo_screenwidth()
        WindowHeight=self.__main.winfo_screenheight()

        kiri=(WindowWidth/2)-(self.__defaultWidth/2)
        atas=(WindowHeight/2)-(self.__defaultHeight/2)

        self.__main.geometry('%dx%d+%d+%d' %(self.__defaultWidth, self.__defaultHeight, kiri, atas))

        #auto resize text
        self.__main.grid_rowconfigure(0,weight=1)
        self.__main.grid_columnconfigure(0,weight=1)

        
        self.__defaultTextArea.grid(sticky=N+E+S+W)
        self.__FileMenu.add_command(label="Baru",command=self.__fileBaru)
        self.__FileMenu.add_command(label="Buka",command=self.__bukaFile)
        self.__FileMenu.add_command(label="Simpan",command=self.__simpanFile)
        self.__FileMenu.add_command(label="Keluar",command=self.__keluar)
        self.__defaultMenuBar.add_cascade(label="File",menu=self.__FileMenu)

        #widget ubah
        self.__EditMenu.add_command(label="Potong",command=self.__cut)
        self.__EditMenu.add_command(label="Salin",command=self.__copy)
        self.__EditMenu.add_command(label="Tempel",command=self.__paste)
        self.__defaultMenuBar.add_cascade(label="Ubah",menu=self.__EditMenu)
        self.__HelpMenu.add_command(label="Versi",command=self.__showAbout)
        self.__defaultMenuBar.add_cascade(label="Tentang",menu=self.__HelpMenu)
        
        self.__main.config(menu=self.__defaultMenuBar)

        #konfigurasi scrollbar
        self.__defaultScrollbar.pack(side=RIGHT,fill=Y) #letak ny ada di kanan dan full vertikal
        self.__defaultScrollbar.config(command=self.__defaultTextArea.yview)
        self.__defaultTextArea.config(yscrollcommand=self.__defaultScrollbar.set)

    def __fileBaru(self):
        self.__main.title("Tak_Berjudul - Andrupad")
        self.__file=None
        self.__defaultTextArea.delete(1.0,END)

    def __bukaFile(self):
        self.__file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if self.__file=="":
            self.__file=None
        else:
            self.__main.title(os.path.basename(self.__file) + " - Andrupad")
            self.__defaultTextArea.delete(1.0,END)

            file=open(self.__file,"r")
            self.__defaultTextArea.insert(1.0,file.read())

            file.close()
    
    def __simpanFile(self):
        if self.__file == None:
            self.__file=asksaveasfilename(initialfile="Tak_Berjudul.txt", defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
            
            if self.__file=="":
                self.__file=None
            else:
                file=open(self.__file,"w")
                file.write(self.__defaultTextArea.get(1.0,END))
                file.close()
                self.__main.title(os.path.basename(self.__file) + " - Andrupad")

        else:
            file=open(self.__file,"w")
            file.write(self.__defaultTextArea.get(1.0,END))
            file.close()

    def __keluar(self):
        self.__main.destroy()

    def __cut(self):
        self.__defaultTextArea.event_generate("<<Cut>>")
    
    def __copy(self):
        self.__defaultTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__defaultTextArea.event_generate("<<Paste>>")

    def run(self):

        #run main application
        self.__main.mainloop()
    
    def __showAbout(self):
        showinfo("Andrupad v1.0","Created by: Andru Baskara Putra\nFollow my Instagram @Filsuf_mengembara")
    





#run
app=Andrupad()
app.run()




