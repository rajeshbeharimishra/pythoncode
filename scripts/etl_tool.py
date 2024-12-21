import tkinter as tk
from tkinter import filedialog
import pandas as pd

def browse_file():
    filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    entry_file_path.delete(0, tk.END)
    entry_file_path.insert(tk.END, filepath)

def run_etl():
    filepath = entry_file_path.get()
    output_file = filedialog.asksaveasfilename(defaultextension=".csv")

    # ETL code goes here
    df = pd.read_csv(filepath)
    # Perform transformations on the data
    # ...

    # Save the transformed data to a new CSV file
    df.to_csv(output_file, index=False)
    tk.messagebox.showinfo("ETL Tool", "ETL process completed successfully!")

# Create the main window
window = tk.Tk()
window.title("ETL Tool")

# File Path Label and Entry
label_file_path = tk.Label(window, text="File Path:")
label_file_path.grid(row=0, column=0)
entry_file_path = tk.Entry(window, width=50)
entry_file_path.grid
(row=0, column=1)
button_browse = tk.Button(window, text="Browse", command=browse_file)
button_browse.grid(row=0, column=2)

# Run ETL Button
button_run_etl = tk.Button(window, text="Run ETL", command=run_etl)
button_run_etl.grid(row=1, column=1)

# Start the GUI event loop
window.mainloop()