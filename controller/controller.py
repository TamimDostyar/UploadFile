import tkinter as tk
from tkinter import Label, filedialog, ttk
import os
import shutil
from PIL import Image, ImageTk
from model.model import processModel
class Uploader:
    def __init__(self, parent):
        self.labelFrame = ttk.Frame(parent)
        self.labelFrame.pack()

    def imageUploader(self):
        self.fileName = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("jpeg", "*.jpg"), ("png", "*.png")))
        
        if self.fileName:
            self.label = ttk.Label(self.labelFrame, text="")
            self.label.grid(column=1, row=2)
            self.label.configure(text=self.fileName)

            
            os.chdir(os.path.expanduser('~/Desktop')) 
            os.makedirs('BACKUP', exist_ok=True) 
            shutil.move(self.fileName, 'BACKUP')
            return processModel(self.fileName)
            
        else:
            print("No file selected.")
            return None 
    def defaultImageCatcher(self):
        return None