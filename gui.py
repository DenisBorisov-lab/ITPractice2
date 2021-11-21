from tkinter import *

root = Tk()
root.title("encoding")
root.geometry("400x200+300+250")
root.resizable(width=False, height=False)


def select():
    pass


modes = [("encoding", 1), ("decoding", 2)]
mode = IntVar

x = 10
y = 50
for txt, val in modes:
    Radiobutton(text=txt, value=val, variable=modes, padx=15, pady=10, command=select).place(x=x, y=y)
    y += 30

btn = Button(text="Start", font=20)
choose_file_btn = Button(text="Choose file", font=20)
choose_file_btn.pack()
btn.pack()

btn.place(x=170, y=150)
choose_file_btn.place(x=230, y=30)
root.mainloop()
