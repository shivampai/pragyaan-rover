import tkinter as tk

def draw_line_chart(data):
    canvas.delete("all")  # Clear previous drawings
    
    chart_width = 400
    chart_height = 300
    x_scale = chart_width / (len(data) - 1)
    y_scale = chart_height / max(data)
    
    for i in range(len(data) - 1):
        x0 = i * x_scale
        y0 = chart_height - data[i] * y_scale
        x1 = (i + 1) * x_scale
        y1 = chart_height - data[i + 1] * y_scale
        
        canvas.create_line(x0, y0, x1, y1, fill="blue")

root = tk.Tk()
root.title("Line Chart Example")

canvas = tk.Canvas(root, width=400, height=300)
canvas.place(relx=0.5,rely=0.2,anchor='center')
canvas.pack()
data = [123]
#data = [123,122,124,123,123,123,125,120,121,123,124,126,130,134,124,110,91,84,84,84,84,84,86,88,96,104,113,120,121,123,124,123]  # Sample data for the line chart
draw_button = tk.Button(root, text="Draw Line Chart", command=lambda: draw_line_chart(data))
draw_button.pack()

root.mainloop()
