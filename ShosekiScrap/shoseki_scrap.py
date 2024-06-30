import re
import csv

with open('input_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Define the regular expression pattern to match the data
pattern = re.compile(r"[\d]*+[ \t][0-9]{13}[ \t][\S]*[ \t][\S]*[ \t][\S]*[ \t][\d]*.[\d]+.[\d]+[ \t][\S]*", re.MULTILINE)

# Find all matches of the pattern in the data
matches = pattern.findall(text)
print(matches)
# Define the CSV file name
csv_filename = 'book_data.csv'

# Write the data to a CSV file
with open(csv_filename, 'w', newline='', encoding='utf-8') as csv_file:  # Specify encoding here
    csv_writer = csv.writer(csv_file)

    # Write header row
    csv_writer.writerow(["Index", "ISBN", "Title", "Publisher", "Author", "Date", "Price"])

    # Write data rows
    for match in matches:
        # Replace unsupported characters with a placeholder
        sanitized_match = [item.encode('utf-8', 'replace').decode('utf-8') if isinstance(item, str) else item for item in match]
        csv_writer.writerow(sanitized_match)

print("CSV file has been created successfully!")
