import json
import time

def update_json_data(data):
    # Update the JSON data
    data["counter"] = data.get("counter", 0) + 1
    return data

def write_json_to_file(file_path, data):
    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    file_path = "data.json"
    data = {"counter": 0}

    try:
        while True:
            updated_data = update_json_data(data)
            write_json_to_file(file_path, updated_data)
            print("JSON data updated:", updated_data)
            time.sleep(1)  # Wait for 1 second
    except KeyboardInterrupt:
        print("Stopped updating JSON data.")
