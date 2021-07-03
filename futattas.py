import tkinter as tk


class Keep(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.shared_data ={
            "email": tk.StringVar(),
            "password": tk.StringVar()
        }

        self.frames = {
            'StartPage': StartPage(self, self),
            'PageTwo': PageTwo(self, self),
        }

        self.current_frame = None
        self.show_frame('StartPage')

    def show_frame(self, name):
        if self.current_frame:
            self.current_frame.forget()
        self.current_frame = self.frames[name]
        self.current_frame.pack()

        self.current_frame.update_widgets() # <-- update data in widgets


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.entry1 = tk.Entry(self, textvariable=self.controller.shared_data["email"])
        self.entry1.pack()
        entry2 = tk.Entry(self, show='*')
        entry2.pack()
        button = tk.Button(self, text="Submit", command=lambda:controller.show_frame("PageTwo"))
        button.pack()

    def update_widgets(self):
        pass

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.label = tk.Label(self, text="") # <-- create empty label
        self.label.pack()

    def update_widgets(self):
        self.label["text"] = "Welcome, {}".format(self.controller.shared_data["email"].get()) # <-- update text in label


if __name__ == "__main__":
    keep = Keep()
    keep.mainloop()