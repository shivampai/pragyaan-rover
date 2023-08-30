import tkinter as tk
from PIL import Image, ImageTk


def draw_arc():
  image_path = "pragyaan_left.png"
  pil_image = Image.open(image_path)
  tkinter_image = ImageTk.PhotoImage(pil_image)
  canvas.create_image(-20, 50, anchor=tk.NW, image=tkinter_image)
  canvas.image = tkinter_image
  
def resize_image(image_path, desired_width, desired_height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((desired_width, desired_height), Image.ANTIALIAS)
    return ImageTk.PhotoImage(resized_image)

root = tk.Tk()
root.title("Canvas Arc Example")
root.geometry('500x350')
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

arc_button = tk.Button(root, text="Draw Arc", command=draw_arc)
arc_button.pack()

root.mainloop()
