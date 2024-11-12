def sort_lines(input_file, output_file):
    # Open the input file and read all lines.
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Separate the first two lines (unsorted) and the rest (to be sorted).
    header = lines[:2]
    body = lines[2:]

    # Sort the remaining lines by the first character if 0 (case-insensitive).
    sorted_body = sorted(body, key=lambda line: line[0].lower(), reverse=True)

    # You want to sort the file not reversed, just delete the ', reverse=True'.
    
    # Combine the header and sorted body.
    sorted_lines = header + sorted_body

    # Write the result to the output file.
    with open(output_file, 'w') as f:
        f.writelines(sorted_lines)

# Specify input and output file names.
input_file = 'assignment02_inclass/md_list.md'
output_file = 'assignment02_inclass/02_results.md'

# Call the function to sort lines.
sort_lines(input_file, output_file)