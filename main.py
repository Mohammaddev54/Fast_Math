from Logic.main import main
from GUI.window import MyWindow as win


def run():
    # main()
    window_obj = win("MATH PRACTICE")
    root = window_obj.root
    root.geometry("350x250")
    window_obj.add_my_widgets()
    root.mainloop()
    

if __name__ == "__main__":
    run()
