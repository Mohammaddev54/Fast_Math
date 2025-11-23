from tkinter import Tk, Menu, Frame, Label, Entry, Button, Scrollbar, END

class MyWindow():
    def __init__(self, title:str="Test Window", width_bool:bool=True, height_bool:bool=True):
        self.root = Tk()
        self.root.title(title)
        # self.root.geometry(f"{width}x{height}") -Removed parameters
        self.root.resizable(width_bool, height_bool)
    
    def add_my_widgets(self):
        # Menus
        root_menu = Menu(self.root, tearoff=0)
        root_menu.add_command(label="Settings", command=lambda: print("Settings clicked!"))
        root_menu.add_command(label="Help", command=lambda:print("Help clicked!"))
        self.root.config(menu=root_menu)
        # Frames
        root_frame_0 = Frame(self.root, bg="#F03FF4")
        root_frame_0.grid(column=0, row=0, sticky="ew")
        root_frame_1 = Frame(self.root, bg="#8AF43F")
        root_frame_1.grid(column=1, row=0, sticky="ew")
        root_frame_2 = Frame(self.root, bg="#05E597", width=220, height=100)
        root_frame_2.grid(column=0, row=1, columnspan=2, sticky="nw")
        # Labels
        word_problem_label = Label(root_frame_0, text="word problem?")
        word_problem_label.grid(sticky="nw")

        mathmatical_expression = Label(root_frame_0, text="a^2 + b^2 = c^2")
        mathmatical_expression.grid()
        # Entries
        user_input_entery = Entry(root_frame_1)
        user_input_entery.grid()
        def returned(n):
            print(n.get())
            n.delete(0, END)
        user_input_entery.bind("<Return>", lambda event: returned(user_input_entery))
        # Buttons  
        next_button = Button(root_frame_2, text="Next")
        previous_button = Button(root_frame_2, text="Previous")
        previous_button.grid(column=0, row=0)
        next_button.grid(column=2, row=0)  
        # Scrollbars
        horizontal = Scrollbar(root_frame_2, orient="horizontal")
        horizontal.grid(column=1, row=0)


def main():
    window = MyWindow()
    root = window.root
    window.add_my_widgets()
    root.mainloop()


if __name__ == '__main__':
    main()