import tkinter as tk


def run_code():
    input_data = input_text.get("1.0", tk.END)  # Get text from the input text box
    input_lines = input_data.strip().split('\n')  # Split input into lines

    if not input_lines:
        print("No input data.")
        return

    # Read the date range string from the first line of input
    date_range_str = input_lines[0].strip()

    # Process the input and append the date range
    output_lines = []
    for line in input_lines[1:]:
        line = line.strip()  # Remove leading/trailing whitespaces
        if line:
            line_with_date = f"{date_range_str}\t{line}"
            output_lines.append(line_with_date)

    # Append the processed data to the output text file
    with open('output_text.txt', 'a', encoding='utf-8') as output_file:
        # Add a separator between the last line of previous text and the new data
        if output_lines:
            output_file.write('\n')
        output_file.write('\n'.join(output_lines))

    # Clear the input text box
    input_text.delete(1.0, tk.END)

    # Display a prompt in the output text box
    output_text.config(state=tk.NORMAL)  # Enable editing
    output_text.delete(1.0, tk.END)  # Clear previous content
    output_text.insert(tk.END, "Data processed and input cleared. Enter new data here...")
    output_text.config(state=tk.DISABLED)  # Disable editing

    print("New data has been appended to output.txt, and input cleared.")


# Create a GUI window
window = tk.Tk()
window.title("Manga Sales Analyzer")

# Create "Run Code" button
run_button = tk.Button(window, text="Run Code", command=run_code)

# Create input text box
input_text = tk.Text(window, height=10, width=40)
input_text.insert(tk.END, "Enter your data here...")

# Create output text box
output_text = tk.Text(window, height=10, width=40)
output_text.config(state=tk.DISABLED)  # Disable editing initially

# Pack widgets
run_button.pack()
input_text.pack()
output_text.pack()

# Start the GUI event loop
window.mainloop()
