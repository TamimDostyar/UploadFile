from tkinter import *
from controller.controller import Uploader 
from model.model import processModel  

class MainView:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("600x400")
        title = self.root.title("Interface")

        self.uploader = Uploader(self.root)

        button = Button(self.root, text="Upload Here", command=self.upload_image)
        button.config(
            font=("Arial", 12),
            bg="#e0e0e0",
            fg="#333333",
            padx=20,
            pady=10,
            relief=RAISED,
            borderwidth=2
        )
        button.pack(pady=20)
        self.root.mainloop()
    
    def upload_image(self):
        file_path = self.uploader.imageUploader() 
        if file_path:
            processModel(file_path)

    def main(self):
        return None