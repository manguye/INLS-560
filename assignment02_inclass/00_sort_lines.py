with open ('assignment02_inclass/names.txt', 'r') as f:
    lines = f.readlines()

sorted_lines = sorted(lines, key=lambda line: line[0].lower())

with open('00_results.txt', 'w') as f:
    f.writelines(sorted_lines)


