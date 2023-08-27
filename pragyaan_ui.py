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

chart_data = [600]
sm_ch_data = [1000]
data = [{"location":'vikramlander','moisture_found':False}]
#
#
ser = serial.Serial('COM3', 9600)

def setInterval(func, interval):
    while True:
        func()
        time.sleep(interval)
 
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
def deploy_flag():
    print("Ok")
def soil_sensor_toggle():
    message="f"
    ser.write(message.encode())  # Encode the message as bytes before sending
    print(f"Sent message: {message}")
    data = ser.readline().decode().strip()
    print("Received data:", data)

    if data=='2001':
        messagebox.showinfo('Success','Soil Moisture Sensor Deployed Successfully!')
    elif data=='2002':
        messagebox.showinfo('Success','Soil Moisture Sensor Retracted Successfully!')
def soil_sensor_toggle():
    message="m"
    ser.write(message.encode())  # Encode the message as bytes before sending
    print(f"Sent message: {message}")
    data = ser.readline().decode().strip()
    print("Received data:", data)

    if data=='2001':
        messagebox.showinfo('Success','Soil Moisture Sensor Deployed Successfully!')
    elif data=='2002':
        messagebox.showinfo('Success','Soil Moisture Sensor Retracted Successfully!')
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
def hud_data():
     message="a"
     ser.write(message.encode())
     print(f"Sent message: {message}")
    
     data = ser.readline().decode().strip()
    #while True:
     if data:
      data_list = data.split(",")
      data_list.remove('all')
      if data_list[5] == "0":
         data_list[5] = 'Off'
      else:
         data_list[5] = 'On'
      if data_list[6] == "0":
        data_list[6] = 'Retracted'
      else:
        data_list[6] = 'Deployed'
      if data_list[7] == "0":
         data_list[7] = 'Retracted'
      else:
         data_list[7] = 'Deployed'
       
      ter_label.config(text=data_list[0]+"cm")
      cel_label.config(text=data_list[1]+"℃")
      soil_moisture_label.config(text=data_list[2]+"%")
      hum_label.config(text=data_list[3]+"%")
      com_label.config(text=data_list[4])
      hl_label.config(text=data_list[5])
      sm_label.config(text=data_list[6])
      fa_label.config(text=data_list[7])
      ofl_label.config(text=data_list[8])
      ofr_label.config(text=data_list[9])
     
      chart_data.append(200-(int(data_list[0])))
      draw_ter_line_chart(chart_data)
     
      sm_ch_data.append(int(data_list[2]))
      draw_soil_moisture_line_chart(sm_ch_data)
    
#def display_image():    
 #   image_path = "assets/map_marked.png"  # Replace with the path to your image
  #  image = Image.open(image_path)
#
 #   tk_image = ImageTk.PhotoImage(image)
  #  label5 = Label(root, image=tk_image)
   # label5.place(relx=0.5,rely=0.65,anchor=CENTER)

    #label5.image = tk_image
    #root.mainloop()
def draw_ter_line_chart(data):
    ter_canvas.delete("all")  # Clear previous drawings
    
    chart_width = 250
    chart_height = 150
    x_scale = chart_width / (len(data) - 1)
    y_scale = chart_height / max(data)
    ter_canvas.delete("text")  # Clear previous text
    ter_canvas.create_text(125, 14, text="Terrain Map", font=("Arial", 8), fill="white", tag="text")

    for i in range(len(data) - 1):
        x0 = i * x_scale
        y0 = chart_height - data[i] * y_scale
        x1 = (i + 1) * x_scale
        y1 = chart_height - data[i + 1] * y_scale
        
        ter_canvas.create_line(x0, y0, x1, y1, fill="white")

def draw_soil_moisture_line_chart(data):
    soil_moist_canvas.delete("all")  # Clear previous drawings
    
    chart_width = 250
    chart_height = 150
    x_scale = chart_width / (len(data) - 1)
    y_scale = chart_height / max(data)
    soil_moist_canvas.delete("text")  # Clear previous text
    soil_moist_canvas.create_text(125, 14, text="Soil Moisture(%) v/s Time(s)", font=("Arial", 8), fill="white", tag="text")

    for i in range(len(data) - 1):
        x0 = i * x_scale
        y0 = chart_height - data[i] * y_scale
        x1 = (i + 1) * x_scale
        y1 = chart_height - data[i + 1] * y_scale
        
        soil_moist_canvas.create_line(x0, y0, x1, y1, fill="white")

def headlights_toggle():
    message="h"
    ser.write(message.encode())  # Encode the message as bytes before sending
    print(f"Sent message: {message}")
    data = ser.readline().decode().strip()
    print("Received data:", data)

    if data=='2001':
        messagebox.showinfo('Success','Headlight Turned On Successfully!')
    elif data=='2002':
        messagebox.showinfo('Success','Headlight Turned Off Successfully!')
def hud_data1():
    '''
    hud_data()
    time.sleep(3)
    hud_data()
    time.sleep(2)
    '''
    setInterval(hud_data, 5)
    #'''
# Create the main application window

root = Tk()
root.title("Pragyaan Telemetrics")
root.geometry('1920x1080')


# Create the Menu Bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Create the File menu with sub-items
rover_controls_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Controls", menu=rover_controls_menu)
rover_controls_menu.add_command(label="Headlights Toggle", command=headlights_toggle)
rover_controls_menu.add_command(label="Soil Sample Testing Bar Toggle", command=soil_sensor_toggle)
rover_controls_menu.add_command(label="Deploy Flag", command=deploy_flag)
rover_controls_menu.add_command(label="Humidity & Temperature", command=start_temp_hum)
rover_controls_menu.add_separator()
rover_controls_menu.add_command(label="Exit", command=root.quit)

# Create the Help menu with sub-items

data_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Data", menu=data_menu)
data_menu.add_command(label="Save moisture as .json", command=moisture_json)


hud_btn = Button(root,text="Establish Communication",command=hud_data)
hud_btn.place(relx=0.1,rely=0)

hud1_btn = Button(root,text="Update Loop",command=hud_data1)
hud1_btn.place(relx=0.6,rely=0)

label1 = Label(root, text="Terrain (-cm) (ChaTeS)")
label1.place(relx=0.1,rely=0.05,anchor=CENTER)
    
ter_label_text = "0cm"
ter_label = Label(root,font=("Helvetica", 24), text=ter_label_text)
ter_label.place(relx=0.1,rely=0.09,anchor=CENTER)
   
label1 = Label(root, text="Temperature (℃)")
label1.place(relx=0.3,rely=0.05,anchor=CENTER)
    
cel_label_text = "0℃"
cel_label = Label(root,font=("Helvetica", 24), text=cel_label_text)
cel_label.place(relx=0.3,rely=0.09,anchor=CENTER)
    
label1 = Label(root, text="Soil Moisture (PraSoM)")
label1.place(relx=0.5,rely=0.05,anchor=CENTER)
    
soil_moisture_label_text = ""
soil_moisture_label = Label(root,font=("Helvetica", 24), text=soil_moisture_label_text)
soil_moisture_label.place(relx=0.5,rely=0.09,anchor=CENTER)
    
label1 = Label(root, text="Humidity (%)")
label1.place(relx=0.7,rely=0.05,anchor=CENTER)
    
hum_label_text = ""
hum_label = Label(root,font=("Helvetica", 24), text=hum_label_text)
hum_label.place(relx=0.7,rely=0.09,anchor=CENTER)
    
label1 = Label(root, text="Communication")
label1.place(relx=0.9,rely=0.05,anchor=CENTER)
    
com_label_text = ""
com_label = Label(root,font=("Helvetica", 24), text=com_label_text,fg="green")
com_label.place(relx=0.9,rely=0.09,anchor=CENTER)
    
label1 = Label(root, text="PraSoM Sensor Arm")
label1.place(relx=0.1,rely=0.15,anchor=CENTER)
  
sm_label_text = ""#Deployed
sm_label = Label(root,font=("Helvetica", 24), text=sm_label_text)
sm_label.place(relx=0.1,rely=0.19,anchor=CENTER)
    
label1 = Label(root, text="Flag Arm")
label1.place(relx=0.3,rely=0.15,anchor=CENTER)
  
fa_label_text = ""#"Deployed"
fa_label = Label(root,font=("Helvetica", 24), text=fa_label_text)
fa_label.place(relx=0.3,rely=0.19,anchor=CENTER)
    
label1 = Label(root, text="Obstacle (FL)")
label1.place(relx=0.5,rely=0.15,anchor=CENTER)
  
ofl_label_text = ""
ofl_label = Label(root,font=("Helvetica", 24), text=ofl_label_text)
ofl_label.place(relx=0.5,rely=0.19,anchor=CENTER)
    
label1 = Label(root, text="Obstacle (FR)")
label1.place(relx=0.7,rely=0.15,anchor=CENTER)
  
ofr_label_text = ""
ofr_label = Label(root,font=("Helvetica", 24), text=ofr_label_text)
ofr_label.place(relx=0.7,rely=0.19,anchor=CENTER)
    
#label1 = Label(root, text="Location Relative")
#label1.place(relx=0.9,rely=0.15,anchor=CENTER)
  
#lr_label_text = "14m"
#lr_label = Label(root,font=("Helvetica", 24), text=lr_label_text)
#lr_label.place(relx=0.9,rely=0.19,anchor=CENTER)
label1 = Label(root, text="Headlights")
label1.place(relx=0.9,rely=0.15,anchor=CENTER)

hl_label_text = "On"
hl_label = Label(root,font=("Helvetica", 24), text=hl_label_text)
hl_label.place(relx=0.9,rely=0.175)

ter_canvas = Canvas(root, width=250, height=150,bg="black")
ter_canvas.place(x=50,y=175)

soil_moist_canvas = Canvas(root, width=250, height=150,bg="black")
soil_moist_canvas.place(x=50,y=325)
#canvas.place(relx=0.1,y=0.25)
#data = [123,122,124,123,123,123,125,120,121,123,124,126,130,134,124,110,91,84,84,84,84,84,86,88,96,104,113,120,121,123,124,123]  # Sample data for the line chart
#draw_button = tk.Button(root, text="Draw Line Chart", command=lambda: draw_line_chart(chart_data))
#draw_button.pack()
  
'''
for i in range(100):
   hud_data()
   timer.sleep(1)
   '''
  
root.mainloop()
    
