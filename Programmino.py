import tkinter as tk
import time
root = tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def hello():
    label1 = tk.Label(root, text= 'Hello World!', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)

def numeri():
    i = 0
    while i < 10:
        time.sleep(0.5)
        label2 = tk.Label(root, text = i, fg='green', font=('helvetica', 12, 'bold'))
        canvas1.create_window(150, 220, window=label2)
        i += 1
        root.update_idletasks()

button1 = tk.Button(text='Click Me', command=hello, bg='brown', fg='white')
button2 = tk.Button(text='see numbers', command=numeri, bg='brown', fg='white')
canvas1.create_window(150, 150, window=button1)
canvas1.create_window(150, 180, window=button2)

root.mainloop()