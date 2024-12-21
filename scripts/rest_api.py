import tkinter as tk
import requests

def api_request():
    url = url_entry.get()
    method = method_var.get()
    payload = payload_entry.get()
    headers = {"Content-Type": "application/json"}

    try:
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=payload)
        elif method == "PUT":
            response = requests.put(url, headers=headers, json=payload)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        else:
            response_text.insert(tk.END, "Invalid Request Method")
            return
        
        response_text.delete(1.0, tk.END)
        response_text.insert(tk.END, response.text)

    except requests.exceptions.RequestException as e:
        response_text.delete(1.0, tk.END)
        response_text.insert(tk.END, str(e))

# Create the GUI window
window = tk.Tk()
window.title("REST API Client")

# URL Entry
url_label = tk.Label(window, text="URL:")
url_label.grid(row=0, column=0, sticky=tk.W)
url_entry = tk.Entry(window)
url_entry.grid(row=0, column=1)

# Request Method Dropdown
method_label = tk.Label(window, text="Method:")
method_label.grid(row=1, column=0, sticky=tk.W)
method_var = tk.StringVar(window)
method_var.set("GET")  # Default value
method_options = ["GET", "POST", "PUT", "DELETE"]
method_dropdown = tk.OptionMenu(window, method_var, *method_options)
method_dropdown.grid(row=1, column=1)

# Payload Entry (for POST and PUT requests)
payload_label = tk.Label(window, text="Payload:")
payload_label.grid(row=2, column=0, sticky=tk.W)
payload_entry = tk.Entry(window)
payload_entry.grid(row=2, column=1)

# Send Button
send_button = tk.Button(window, text="Send Request", command=api_request)
send_button.grid(row=3, column=0, columnspan=2)

# Response Text
response_text = tk.Text(window, height=10, width=50)
response_text.grid(row=4, column=0, columnspan=2)

window.mainloop()
