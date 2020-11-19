import tkinter

window = tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x400+100+100")
window.resizable(True, True)

text = tkinter.Text(window)

text.insert(tkinter.CURRENT, "안녕하세요.\n")

text.pack()

window.mainloop()
