import tkinter as tk
from tkinter import scrolledtext
import os


def submit_text():
    text = input_box.get("1.0", "end-1c")  # Get the text from input box
    input_data.append(text)  # Add the text to the input_data list
    input_box.delete("1.0", tk.END)  # Clear the input box

    output_box.insert(tk.END, text + "\n")  # Print the text in the output box

    # Write the text to output.txt file
    with open('output.txt', 'a') as file:
        file.write(text + "\n")


def clear_text():
    input_data.clear()  # Clear the input data list
    output_box.delete("1.0", tk.END)  # Clear the output box


# Create the main window
window = tk.Tk()
window.title("Text Box Example")

# Create the input box
input_box = tk.Text(window, height=10, width=50)  # Increase the height and width here
input_box.pack(pady=10)  # Add padding between the input box and other elements

# Create the button frame
button_frame = tk.Frame(window)
button_frame.pack()

# Create the Submit button
submit_button = tk.Button(button_frame, text="Submit", command=submit_text)
submit_button.pack(side=tk.LEFT, padx=5)

# Create the Clear button
clear_button = tk.Button(button_frame, text="Clear", command=clear_text)
clear_button.pack(side=tk.LEFT, padx=5)

# Create the output box with a scrollbar
output_frame = tk.Frame(window)
output_frame.pack()
scrollbar = tk.Scrollbar(output_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_box = scrolledtext.ScrolledText(output_frame, height=10, width=50, state=tk.DISABLED,
                                       yscrollcommand=scrollbar.set)
output_box.pack()
scrollbar.config(command=output_box.yview)

# Initialize the input data list
input_data = []

# Create output.txt file if it doesn't exist
if not os.path.exists('output.txt'):
    open('output.txt', 'w').close()

# Read existing data from output.txt file and display in the output box
with open('output.txt', 'r') as file:
    output_data = file.read()
    output_box.configure(state=tk.NORMAL)
    output_box.insert(tk.END, output_data)
    output_box.configure(state=tk.DISABLED)

# Start the Tkinter event loop
window.mainloop()
