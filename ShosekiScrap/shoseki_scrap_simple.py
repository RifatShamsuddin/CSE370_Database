# Read the date range string from the first line of the input text file
with open('input_text.txt', 'r', encoding='utf-8') as input_file:
    date_range_str = input_file.readline().strip()

# Read the rest of the input data from the input text file
with open('input_text.txt', 'r', encoding='utf-8') as input_file:
    input_lines = input_file.readlines()[1:]  # Exclude the first line

# Process the input and append the date range
output_lines = []
for line in input_lines:
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

print("New data has been appended to the output file.")
