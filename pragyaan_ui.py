from tkinter import *
from tkinter import messagebox
import serial
import json
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import itertools
from PIL import Image, ImageTk


data = [{"location":'vikramlander','moisture_found':False}]
#
#
ser = serial.Serial('COM6', 9600)


def create_terrain_chart():
    ter_x_data = [1]
    ter_y_data = [0]

    fig, ax = plt.subplots()

    ax.plot(ter_x_data, ter_y_data, marker='o')

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Terrain (Centimeters)")
    ax.set_title("Terrain (Pragyaan)")

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()
def create_hum_chart():
    hum_x_data = [1]
    hum_y_data = [0]

    fig, ax = plt.subplots()

    ax.plot(hum_x_data, hum_y_data, marker='o')

    ax.set_xlabel("Time (Seconds)")
    ax.set_ylabel("Percentage (%)")
    ax.set_title("Humidity (Pragyaan)")

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()
def create_temp_chart():
    temp_x_data = [1]
    temp_y_data = [0]

    fig, ax = plt.subplots()

    ax.plot(temp_x_data, temp_y_data, marker='o')

    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature(Celsius)")
    ax.set_title("Temperature (℃) (Pragyaan)")

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

def file_new():
    messagebox.showinfo("New", "New File")

def start_temp_hum():
    #while True:
    #for i in 10:
        temp_hum_start()
        time.sleep(1)
        create_hum_chart()

def temp_hum_start():
    message="t"
    ser.write(message.encode())
    print(f"Sent message: {message}")
    data = ser.readline().decode().strip()
    data_list = data.split(",")
    print("temp:",data_list[0],"hum:",data_list[1])

def soil_sensor_toggle():
    message="m"
    ser.write(message.encode())  # Encode the message as bytes before sending
    print(f"Sent message: {message}")
    data = ser.readline().decode().strip()
    print("Received data:", data)

    if data=='2001':
        messagebox.showinfo('Success','Soil Moisture Sensor Deployed Successfully!')
    elif data=='2002':
        messagebox.showerror('Success','Soil Moisture Sensor Retracted Successfully!')
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
    message="h"
    ser.write(message.encode())  # Encode the message as bytes before sending
    print(f"Sent message: {message}")
    data = ser.readline().decode().strip()
    print("Received data:", data)

    if data=='2001':
        messagebox.showinfo('Success','Headlight Turned On Successfully!')
    elif data=='2002':
        messagebox.showerror('Success','Headlight Turned Off Successfully!')

# Create the main application window

root = Tk()
root.title("Chandrayaan 3 Rover")
root.geometry('600x600')
# Create the Menu Bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Create the File menu with sub-items
rover_controls_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Controls", menu=rover_controls_menu)
rover_controls_menu.add_command(label="Headlights Toggle", command=headlights_toggle)
rover_controls_menu.add_command(label="Soil Sample Testing Bar Toggle", command=soil_sensor_toggle)
rover_controls_menu.add_command(label="Humidity & Temperature", command=start_temp_hum)
rover_controls_menu.add_command(label="Save", command=file_save)
rover_controls_menu.add_separator()
rover_controls_menu.add_command(label="Exit", command=root.quit)

# Create the Help menu with sub-items

data_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Data", menu=data_menu)
data_menu.add_command(label="Save moisture as .json", command=moisture_json)



label1 = Label(root, text="Terrain (-cm) (ChaTeS)")
label1.place(relx=0.1,rely=0.05,anchor=CENTER)
    
ter_label_text = "90cm"
ter_label = Label(root,font=("Helvetica", 24), text=ter_label_text)
ter_label.place(relx=0.1,rely=0.09,anchor=CENTER)
   
label1 = Label(root, text="Temperature (℃)")
label1.place(relx=0.3,rely=0.05,anchor=CENTER)
    
cel_label_text = "12℃"
cel_label = Label(root,font=("Helvetica", 24), text=cel_label_text)
cel_label.place(relx=0.3,rely=0.09,anchor=CENTER)
    
label1 = Label(root, text="Soil Moisture (PraSoM)")
label1.place(relx=0.5,rely=0.05,anchor=CENTER)
    
soil_moisture_label_text = "0.1%"
soil_moisture_label = Label(root,font=("Helvetica", 24), text=soil_moisture_label_text)
soil_moisture_label.place(relx=0.5,rely=0.09,anchor=CENTER)
    
label1 = Label(root, text="Humidity (%)")
label1.place(relx=0.7,rely=0.05,anchor=CENTER)
    
hum_label_text = "0.6558%"
hum_label = Label(root,font=("Helvetica", 24), text=hum_label_text)
hum_label.place(relx=0.7,rely=0.09,anchor=CENTER)
    
label1 = Label(root, text="Communication")
label1.place(relx=0.9,rely=0.05,anchor=CENTER)
    
com_label_text = "Healthy"
com_label = Label(root,font=("Helvetica", 24), text=com_label_text,fg="green")
com_label.place(relx=0.9,rely=0.09,anchor=CENTER)
    
label1 = Label(root, text="Headlights")
label1.place(relx=0.1,rely=0.15,anchor=CENTER)
  
hl_label_text = "On"
hl_label = Label(root,font=("Helvetica", 24), text=hl_label_text)
hl_label.place(relx=0.1,rely=0.19,anchor=CENTER)
    
label1 = Label(root, text="PraSoM Sensor Arm")
label1.place(relx=0.1,rely=0.15,anchor=CENTER)
  
sm_label_text = "Retracted"#Deployed
sm_label = Label(root,font=("Helvetica", 24), text=sm_label_text)
sm_label.place(relx=0.1,rely=0.19,anchor=CENTER)
    
label1 = Label(root, text="Flag Arm")
label1.place(relx=0.3,rely=0.15,anchor=CENTER)
  
fa_label_text = "Retracted"#"Deployed"
fa_label = Label(root,font=("Helvetica", 24), text=fa_label_text)
fa_label.place(relx=0.3,rely=0.19,anchor=CENTER)
    
label1 = Label(root, text="Obstacle (FL)")
label1.place(relx=0.5,rely=0.15,anchor=CENTER)
  
ofl_label_text = "True"
ofl_label = Label(root,font=("Helvetica", 24), text=ofl_label_text)
ofl_label.place(relx=0.5,rely=0.19,anchor=CENTER)
    
label1 = Label(root, text="Obstacle (FR)")
label1.place(relx=0.7,rely=0.15,anchor=CENTER)
  
ofr_label_text = "False"
ofr_label = Label(root,font=("Helvetica", 24), text=ofr_label_text)
ofr_label.place(relx=0.7,rely=0.19,anchor=CENTER)
    
label1 = Label(root, text="Location Relative")
label1.place(relx=0.9,rely=0.15,anchor=CENTER)
  
lr_label_text = "14m"
lr_label = Label(root,font=("Helvetica", 24), text=lr_label_text)
lr_label.place(relx=0.9,rely=0.19,anchor=CENTER)
        


root.mainloop()
