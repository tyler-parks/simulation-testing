import tkinter as tk
import random

# --- functions ---

def on_canvas_click(event):
    print('on canvas click')

    print('event:', event)
    print('x, y :', event.x, event.y)

    #Draw an Oval in the canvas
    canvas.create_oval(event.x,event.x,event.y,event.y)
    
    print('-----')

# --- main ---

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

canvas.bind('<Button-1>', on_canvas_click)

root.mainloop()  