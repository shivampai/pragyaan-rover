import json
import matplotlib.pyplot as plt

def read_json_data(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return data

def create_line_chart(data):
    labels = list(data.keys())
    values = list(data.values())

    plt.plot(labels, values, marker='o')  # Create a line chart with markers
    plt.xlabel("X-axis Label")
    plt.ylabel("Y-axis Label")
    plt.title("Line Chart from JSON Data")
    plt.grid(True)  # Add grid lines
    plt.show()

if __name__ == "__main__":
    file_path = "data.json"  # Replace with your JSON file path
    loaded_data = read_json_data(file_path)

    create_line_chart(loaded_data)
