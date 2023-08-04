import tkinter as tk
from tkinter import messagebox
import serial
import json
data = [{"location":'vikramlander','moisture_found':False}]
#
#
def file_new():
    messagebox.showinfo("New", "New File")

def soil_sensor_toggle():
    if 1==1:
        messagebox.showinfo('Success','Soil Moisture Sensor Deploy Success!')
    else:
        messagebox.showerror('Failure','Soil Moisture Sensor Deploy Failure!')
def file_save():
    messagebox.showinfo("Save", "Save File")

def moisture_json():
    data.append({
    "location": (69.367621, 32.348126),
    "moisture_found": True
    })
    file_path = "moisture.json"
    with open(file_path, 'w') as json_file:
      json.dump(data, json_file, indent=4)
    messagebox.showinfo('File Save Success','Saved As moisture.json file')
def headlights_toggle():
    if 1 == 1:
        messagebox.showinfo("Success","Headlight Start Success!")

# Create the main application window

root = tk.Tk()
root.title("Chandrayaan 3 Rover")
root.geometry('600x600')
# Create the Menu Bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create the File menu with sub-items
rover_controls_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Controls", menu=rover_controls_menu)
rover_controls_menu.add_command(label="Headlights Toggle", command=headlights_toggle)
rover_controls_menu.add_command(label="Soil Sample Testing Bar Toggle", command=soil_sensor_toggle)
rover_controls_menu.add_command(label="Save", command=file_save)
rover_controls_menu.add_separator()
rover_controls_menu.add_command(label="Exit", command=root.quit)

# Create the Help menu with sub-items

data_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Data", menu=data_menu)
data_menu.add_command(label="Save moisture as .json", command=moisture_json)

root.mainloop()
