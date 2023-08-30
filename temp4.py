import tkinter as tk
from PIL import Image, ImageTk


def draw_arc():
  hl = 'On'
  o_l = '1'
  o_r = '1'
  image_path = "pragyaan.png"
  pil_image = Image.open(image_path)
  tkinter_image = ImageTk.PhotoImage(pil_image)
  canvas.create_image(-20, 50, anchor=tk.NW, image=tkinter_image)
  canvas.image = tkinter_image
  if hl == 'On':
    canvas.create_arc(10,
                      50,
                      80,
                      120,
                      start=45,
                      extent=100,
                      fill="yellow",
                      outline="")

    canvas.create_arc(80,
                      50,
                      150,
                      120,
                      start=45,
                      extent=100,
                      fill="yellow",
                      outline="")
  if o_l == '1':
      canvas.create_oval(50, 50, 65, 65, fill="red", outline="")
  if o_r == '1':
      canvas.create_oval(85, 50, 100, 65, fill="red", outline="")

root = tk.Tk()
root.title("Canvas Arc Example")
root.geometry('500x350')
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

arc_button = tk.Button(root, text="Draw Arc", command=draw_arc)
arc_button.pack()

root.mainloop()
