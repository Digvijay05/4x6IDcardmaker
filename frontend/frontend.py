from tkinter import *
from tkinter import filedialog


class Window:
    def __init__(self):
        self.root = Tk()

        self.root.wm_title("Aadhar card print")
        self.root.geometry("%dx%d+%d+%d" % (self.root.winfo_screenwidth()/2, self.root.winfo_screenheight()/2, self.root.winfo_screenwidth()/4, self.root.winfo_screenheight()/4))
        self.frame = Frame(self.root, bd=8, bg="black", relief="groove")
        self.frame.pack(side=TOP, fill="x")
        self.title_label = Label(self.frame, text="Aadhar card print",
                            font=("times new roman", 20, "bold"), bg="black", fg="white", pady=5)
        self.title_label.pack()
        self.browse_btn = Button(self.root, text="Browse", command=self.browse_file)
        self.browse_btn.pack()
        self.filename = ""
        self.password = StringVar()
        self.password_box = Entry(self.root, width=20, font="arial 15", bd=5,
                               textvariable=self.password)
        self.password_box.pack()
        self.root.mainloop()

    def browse_file(self):
        self.filename = filedialog.askopenfilename(title="Select a file", filetypes=[("PDF files", "*.pdf"),
                                                                                     ("All files", "*.*")])




if __name__ == "__main__":
    Window()
