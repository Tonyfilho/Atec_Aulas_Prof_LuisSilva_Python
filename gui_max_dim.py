from tkinter import *

root = Tk()

screen_width  = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

root.geometry(str(screen_width)+'x'+str(screen_height)+'+0+0')
root.title('Maximas dimensões do monitor')
root.resizable(False,False)

root.mainloop()
