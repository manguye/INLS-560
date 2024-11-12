# Not required.
def sort_file_by_columns(input_file, output_file, primary_index=0, secondary_index=0, delimiter=',', reverse=False):
    # Open the input file and read all lines.
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Separate the first two lines (unsorted) and the rest (to be sorted).
    header = lines[:2]
    body = lines[2:]

    # Sort the body by primary and secondary columns (case-insensitive).
    sorted_body = sorted(
        body,
        key=lambda line: (
            line.split(delimiter)[primary_index].lower(),
            line.split(delimiter)[secondary_index].lower()
        ),
        reverse=reverse
    )

    # Combine the header and sorted body.
    sorted_lines = header + sorted_body

    # Write the result to the output file.
    with open(output_file, 'w') as f:
        f.writelines(sorted_lines)

# Specify input and output file names.
input_file = 'assignment02_inclass/battlemechs_year_class.csv'
output_file = 'assignment02_inclass/04_results.csv'

sort_file_by_columns(input_file, output_file, primary_index=0, delimiter=',', reverse=False)