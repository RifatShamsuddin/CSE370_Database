import tkinter as tk
import openpyxl

def format():
    # # Load the Excel workbook
    # workbook = openpyxl.Workbook()
    #
    # # Select the active sheet
    # sheet = workbook.active
    #
    # # Result to be pasted
    # result = "This is the result."
    #
    # # Paste the result in cell A1
    # sheet['A1'] = result
    #
    # # Save the workbook to a file
    # workbook.save("output.xlsx")
    pass

def main():
    # Create the main Tkinter window
    window = tk.Tk()
    window.title("Website Formatting")

    # Create a label for the link entry
    link_label = tk.Label(window, text="Enter website link:")
    link_label.pack()

    # Create a text entry field for the link
    link_entry = tk.Entry(window)
    link_entry.pack()

    def format_button_click():
        # Call the format function when the button is clicked
        format()

    # Create a button to trigger the format function
    format_button = tk.Button(window, text="Format", command=format_button_click)
    format_button.pack()

    # Start the Tkinter event loop
    window.mainloop()

if __name__ == "__main__":
    main()