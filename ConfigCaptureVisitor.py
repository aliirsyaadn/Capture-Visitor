import cv2 as cv
from tkinter import *
from tkinter import messagebox
import os

class GUI :
    '''Class untuk membuat GUI yang berguna mengonfigurasi target dari Capture Visitor yang diinginkan'''
    def __init__(self):
        '''Method inisiasi untuk membuat GUI root dan memanggil method lain'''
        self.root = Tk()
        self.root.title("Capture Visitor by Ali Irsyaad N")
        self.root.geometry("350x150")
        self.make_widget()
        self.pack_widget()
        self.root.mainloop()
        
    def make_widget(self):
        '''Method untuk membuat widget pada GUI'''
        self.label_dir_target = Label(self.root, text='Enter directory of your target application: ')
        self.dir_target = Entry(self.root)
        self.label_file_name = Label(self.root, text='Enter your folder and file name: ')
        self.file_name = Entry(self.root)
        self.enter_button = Button(self.root, text='Create', command=self.make_folder_py_vbs)
        
    def pack_widget(self):
        '''Method untuk mengepack widget pada GUI'''
        self.label_dir_target.pack()
        self.dir_target.pack()
        self.label_file_name.pack()
        self.file_name.pack()
        self.enter_button.pack()

    def make_folder_py_vbs(self):
        '''Method untuk membuat folder dan file baru pada directory main program'''
        try:
            name = self.file_name.get()
            target = self.dir_target.get().strip('"')
            dir_folder_cv = os.getcwd()[2:]
            os.mkdir(name)
            dir_folder = f'{os.getcwd()}\{name}'
            dir_py = f'{dir_folder}\{name}.py'
            dir_vbs = f'{dir_folder}\{name}.vbs'
            name_pict = f'{name}.png'

            # Untuk membuat file python dan vbs
            with open(f'{dir_py}', 'w') as file:
                file.write(f'import sys\nsys.path.insert(0,r"{dir_folder_cv}")\nfrom ConfigCaptureVisitor import Capture\nrun = Capture(r"{dir_folder}","{name_pict}")')
                      
            with open(f'{dir_vbs}', 'w') as file:
                file.write(f'Set WshShell = CreateObject("WScript.Shell")\nWshShell.Run chr(34) & "{target}" & chr(34), 0\nWshShell.Run chr(34) & "{dir_py}" & chr(34), 0\nSet WshShell = Nothing')

            self.root.clipboard_append(f'{dir_vbs}')
            self.root.update()
            messagebox.showinfo(title='Information To Do', message=f'This directory :\n{dir_vbs} has been copied to your clipboard\nYou should paste them in target of your shorcut application target')
            self.root.destroy()

        # Except untuk menghandle jika user tidak memasukkan sesuatu ke entry  
        except FileNotFoundError:
            messagebox.showerror(message='Please fill your folder and file name')

        # Except untuk menghandle jika user memasukkan entry yang sudah ada dan ada contain special karakter
        except OSError:
            messagebox.showerror(message='Your folder and file name already exist or can\'t contain any of the following characters:\n \ / : * ? " < > | ')
       

        
class Capture:
    '''Class untuk menangkap foto dan menyimpannya pada suatu directory'''
    def __init__(self,dir_folder,file_name):
        '''Method untuk menginisiasi lokasi folder dan nama folder serta memanggil method capture'''
        self.dir_folder = dir_folder
        self.file_name = file_name
        self.capture(self.dir_folder, self.file_name)
        
    def capture(self,dir_folder,file_name):
        '''Method untuk menangkap foto dan menyimpannya pada suatu directory'''
        cam = cv.VideoCapture(0)
        img_counter = 0
        while True:
            frame = cam.read()[1]
            cv.waitKey(1)
            if img_counter == 25 :
                img_directory = f"{dir_folder}\{file_name}"
                cv.imwrite(img_directory, frame)
                cam.release()
                cv.destroyAllWindows()
                break
            img_counter += 1
        
def main():      
    run = GUI()
                         
if __name__ == "__main__":
    main()

