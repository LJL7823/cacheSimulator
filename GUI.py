import tkinter as tk
from tkinter import ttk 

def create_table_gui(data):
    # Create the main application window
    root = tk.Tk()
    root.title("2D Matrix Table")

    # Create a frame to contain the table
    frame = tk.Frame(root)
    frame.pack(pady=15, padx=15)
    root.geometry("1000x1000+0+300")

    # Loop through the rows and columns of the matrix and create label widgets
    for row_index, row in enumerate(data):
        for col_index, value in enumerate(row):
            # Create a label with the matrix value
            label = tk.Label(frame, text=str(value), borderwidth=1, relief="solid", width=10, height=2, padx= 10)
            # Use grid geometry manager to position the label in the correct location
            label.grid(row=row_index, column=col_index, padx=1, pady=5)

    # Start the Tkinter event loop
    return root


# Call the function to create the GUI
#create_table_gui(cache.cache)