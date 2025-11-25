from tkinter import Tk, Menu, Frame, Label, Entry, Button, Scrollbar, END

class MyWindow():
    def __init__(self, title:str="Test Window", width_bool:bool=True, height_bool:bool=True):
        self.root = Tk()
        self.root.title(title)
        # self.root.geometry(f"{width}x{height}") -Removed parameters
        self.root.resizable(width_bool, height_bool)
    
    def add_my_widgets(self):
        root = self.root
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        
        # Frames
        root_frame = Frame(root)
        root_frame.grid(sticky="ewns")

        # Math Expression Label
        expression = Label(root_frame, text="0")
        expression.grid(sticky="wn")



def main():
    window = MyWindow(title="MATH PRACTICE")
    root = window.root
    root.geometry("350x250")
    window.add_my_widgets()
    root.mainloop()


if __name__ == '__main__':
    main()