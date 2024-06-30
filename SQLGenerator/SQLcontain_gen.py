def generate_google_sheets_sql(table_range, column, search_value):
    sql_code = f"=QUERY({table_range}, \"SELECT * WHERE {column} CONTAINS '{search_value}'\", 0)"
    return sql_code

# Example usage:
table_range = "'Sheet1'!A1:H10"  # Replace with your desired range
column = "D"  # Replace with the column you want to search in
search_value = "example"  # Replace with the search value
sql_code = generate_google_sheets_sql(table_range, column, search_value)
print(sql_code)
