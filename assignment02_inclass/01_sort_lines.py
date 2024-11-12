def sort_lines(input_file, output_file):
    '''This is a function that lets us put the file names in easier.'''
    with open(input_file, 'r') as f:
        lines = f.readlines()

    sorted_lines = sorted(lines, key=lambda line: line[31].lower())
    
    with open (output_file, 'w') as f:
        f.writelines(sorted_lines)

input_file = 'assignment02_inclass/md_list_unsorted.md'
output_file = 'assignment02_inclass/01_results_31.md'

sort_lines(input_file, output_file)