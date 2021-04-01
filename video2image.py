from tkinter import *
import tkinter.messagebox
import tkinter.ttk
from tkinter import *
from tkinter.ttk import *
import cv2
import os
from tkinter import filedialog
class video2image():
    def help(self):
        tkinter.messagebox.showinfo(title="Help", message="Only One By One Video Insert ")
    def About(self):
        tkinter.messagebox.showinfo(title="About", message="Developed By Azhar ! \n https://github.com/azhar-py ")
    def Exit(self):
        exit()
    def file(self):
        pass

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select Video", filetype=
        (("*mp4", "*.mkv"), ("all files", "*.*")))
        self.label = Label(self.root)
        self.label.place(x=80,y=48)
        self.label.configure(text=self.filename[100:10])


    def convert(self):
        try:
            if not os.path.exists("data"):
                os.mkdir("data")
            if self.filename != "":
                i = 1
                tkinter.messagebox.showinfo("Wait","converting video to images  \n Press Ok ! ")
                cap = cv2.VideoCapture(self.filename)
                while(cap.isOpened()):
                    ret, frame = cap.read()
                    if ret == False:
                        break
                    cv2.imwrite("./data/Frame"+str(i)+".jpg",frame)
                    i+=1
                    if cv2.waitKey(1) == ord("q"):
                        break

                tkinter.messagebox.showinfo("Sucess", "conversion Completed")
                cap.release()
                cv2.destroyAllWindows()
        except:
            tkinter.messagebox.showerror("Error","Please Select the Video")




    def __init__(self):
        self.root = Tk()
        self.root.geometry("512x200")
        self.root.title("Video To Image Converter ")
        self.menubar = Menu(self.root)
        self.filemenu = Menu(self.menubar)
        self.menubar.add_cascade(label="Help", command=self.help)
        self.menubar.add_cascade(label="About", command=self.About)
        self.menubar.add_cascade(label="Exit",command=self.Exit)
        self.root.config(menu=self.menubar)

        self.lab = Label(self.root, text="Video To Image Converter ",font=("Courier", 20))
        self.lab.place(x=80, y=5)

        self.pt = Label(self.root,text="PATH :")
        self.pt.place(x=25,y=48)

        self.select = Button(self.root,text="Select Video",width=20,command=self.fileDialog)
        self.select.place(x=250,y=40)

        self.conver = Button(self.root,text="Convert",width=20,command=self.convert)
        self.conver.place(x=250, y=90)

        self.close = Button(self.root, text="Close",width=20,command=self.Exit)
        self.close.place(x=250, y=140)

        self.root.mainloop()


if __name__ == '__main__':
    video2image()