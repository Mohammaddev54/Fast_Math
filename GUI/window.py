from tkinter import Tk, Menu, Frame, Label, Entry, Button, Scrollbar, END

class MyWindow():
    def __init__(self, title:str="Test Window", width_bool:bool=True, height_bool:bool=True):
        self.root = Tk()
        self.root.title(title)
        # self.root.geometry(f"{width}x{height}") -Removed parameters
        self.root.resizable(width_bool, height_bool)
        self.root.grid
    
    def add_my_widgets(self):
        root = self.root
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        
        # Frames
        root_frame = Frame(root, bg="#BEB369")
        root_frame.grid(sticky="ewns")

        root_frame.grid_columnconfigure(0, weight=1)
        root_frame.grid_rowconfigure(0, weight=1)

        root_frame.grid_columnconfigure(0, weight=1)
        root_frame.grid_rowconfigure(1, weight=1)

        root_frame.grid_columnconfigure(0, weight=1)
        root_frame.grid_rowconfigure(2, weight=1)

        top_frame = Frame(root_frame, bg="#FF0000")
        top_frame.grid(row=0, column=0, columnspan=3, sticky="ewns")

        top_frame.grid_columnconfigure(0, weight=1)
        top_frame.grid_rowconfigure(1, weight=1)

        middle_frame = Frame(root_frame, bg="#FFFF00")
        middle_frame.grid(row=1, column=0, columnspan=3, sticky="ewns")

        bottom_frame = Frame(root_frame, bg="#FFFFFF")
        bottom_frame.grid(row=2, column=0, columnspan=3, sticky="ewns")

        timer_frame = Frame(middle_frame)
        timer_frame.grid(row=0, column=0)

        timer_buttons_frame = Frame(middle_frame)
        timer_buttons_frame.grid(row=0, column=1)

        # Labels
        math_expression_question_label = Label(top_frame, text="QUESTION!")
        math_expression_question_label.grid(row=0, column=0, columnspan=3)

        math_expression = Label(top_frame, text="a^2 + b^2 = c^2")
        math_expression.grid(row=1, column=0, columnspan=2)

        

        # Entries
        user_answer_entry = Entry(top_frame)
        user_answer_entry.grid(row=1, column=3, columnspan=2)





def main():
    window = MyWindow(title="MATH PRACTICE")
    root = window.root
    root.geometry("350x250")
    window.add_my_widgets()
    root.mainloop()


if __name__ == '__main__':
    main()